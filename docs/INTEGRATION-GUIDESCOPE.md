# Guidescope 統合ガイド

## Status

- Guidescope repository: https://github.com/cursorvers/guidescope
- Local checkout: ~/Dev/guidescope
- MCP tool count: 4 (`generate` / `generatePrompt` / `generateSearchQueries` / `listPresets`)
- Corpus npm package: 未公開
- Guidescope corpus imports: 0件

## シナリオ A: Guidescope MCP tool extension (推奨)

`@cursorversinc/guidescope-mcp` に `query_governance_crosswalk(persona, query)` tool を追加し、既存 MCP client から医療 AI ガバナンス横断表を検索できるようにします。UI と既存 prompts には触らず、MCP tool surface の純加算に留めます。

```ts
import { guidelines } from "@cursorversinc/guidescope-medical-corpus";
import { z } from "zod";

const inputSchema = z.object({
  persona: z.enum(["clinician", "regulator", "developer", "researcher"]),
  query: z.string().min(1),
  limit: z.number().int().positive().max(20).default(8)
});

export function registerGovernanceCrosswalkTool(server: McpServer) {
  server.tool(
    "query_governance_crosswalk",
    "Search medical AI governance crosswalk cells by persona and query.",
    inputSchema.shape,
    async ({ persona, query, limit }) => {
      const terms = query.toLowerCase().split(/\s+/).filter(Boolean);
      const rows = guidelines.flatMap((guideline) =>
        guideline.cells.map((cell) => ({ guideline, cell }))
      );
      const matches = rows
        .filter(({ guideline, cell }) => {
          const haystack = [
            persona,
            guideline.name_en,
            guideline.name_ja,
            cell.column,
            cell.requirement,
            cell.summary_ja,
            cell.notes_ja ?? ""
          ].join(" ").toLowerCase();
          return terms.every((term) => haystack.includes(term));
        })
        .slice(0, limit);

      return {
        content: [{ type: "text", text: JSON.stringify(matches, null, 2) }]
      };
    }
  );
}
```

Pros: 最小diff、純加算、既存MCPクライアント全対応。

Cons: UI なし。

## シナリオ B: Guidescope UI panel

Guidescope の UI に引用パネルを追加し、検索結果セル、要求水準、引用、source URL を視覚的に確認できるようにします。

```tsx
import type { Cell, Guideline } from "@cursorversinc/guidescope-medical-corpus";

type CitationPanelProps = {
  guideline: Guideline;
  cell: Cell;
};

export function CitationPanel({ guideline, cell }: CitationPanelProps) {
  return (
    <aside className="citation-panel" aria-label="Governance citation">
      <header>
        <p>{guideline.name_en}</p>
        <strong>{cell.column}</strong>
      </header>
      <p>{cell.summary_ja}</p>
      <dl>
        <dt>Requirement</dt>
        <dd>{cell.requirement}</dd>
        <dt>Confidence</dt>
        <dd>{cell.citation.confidence ?? "unknown"}</dd>
      </dl>
      {cell.citation.url ? (
        <a href={cell.citation.url} target="_blank" rel="noreferrer">
          {cell.citation.section ?? "Source"}
        </a>
      ) : null}
    </aside>
  );
}
```

```text
+--------------------------------------------------------------+
| Prompt / preset workspace                                    |
|                                                              |
|  Query: IRB review for clinical AI                           |
|                                                              |
|  +--------------------------+  +---------------------------+  |
|  | Generated guidance       |  | Governance citations      |  |
|  |                          |  | PMDA SaMD                 |  |
|  | - clinical evaluation    |  | Column: clinical_eval     |  |
|  | - risk management        |  | Requirement: must         |  |
|  |                          |  | Source: PMDA URL          |  |
|  +--------------------------+  +---------------------------+  |
+--------------------------------------------------------------+
```

Pros: 視覚的。

Cons: UI改修必要、bundle肥大。

## シナリオ C: Static asset bundling

Guidescope の build step で corpus を fetch し、静的 JSON asset として bundle に同梱します。runtime の npm dependency を避けたい場合に有効です。

```ts
import { writeFile } from "node:fs/promises";

const sourceUrl =
  "https://raw.githubusercontent.com/cursorvers/medical-ai-governance-crosswalk/main/packages/guidescope-medical-corpus/dist/corpus.json";

const response = await fetch(sourceUrl);
if (!response.ok) {
  throw new Error(`Failed to fetch corpus: ${response.status}`);
}

await writeFile("src/generated/medical-governance-corpus.json", await response.text());
```

Pros: offline対応。

Cons: 105KB bundle肥大、build時依存。

## 推奨

Scenario A を推奨します。理由は、最小diff、ゼロbreaking、低friction で Guidescope MCP の既存利用者に横断表検索を提供できるためです。
