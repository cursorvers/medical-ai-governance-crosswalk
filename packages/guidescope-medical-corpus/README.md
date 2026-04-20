# @cursorversinc/guidescope-medical-corpus

公開ガイドライン10本×論点13列=130セルの構造化コーパスです。GuideScope や MCP tools から、医療 AI ガバナンスの横断論点、要求水準、引用情報を型付きデータとして参照できます。

## Install

```sh
npm install @cursorversinc/guidescope-medical-corpus
```

## Quickstart

### List guideline names

```ts
import { guidelines } from "@cursorversinc/guidescope-medical-corpus";

for (const guideline of guidelines) {
  console.log(guideline.name_en);
}
```

### Find a cell by guideline and column

```ts
import { guidelines, type Cell } from "@cursorversinc/guidescope-medical-corpus";

function findCell(guideline_id: string, column_id: string): Cell | undefined {
  return guidelines
    .find((guideline) => guideline.id === guideline_id)
    ?.cells.find((cell) => cell.column === column_id);
}

const cell = findCell("pmda-samd", "clinical_evaluation");
console.log(cell?.summary_ja);
```

### Filter must-level cells

```ts
import { guidelines } from "@cursorversinc/guidescope-medical-corpus";

const mustCells = guidelines.flatMap((guideline) =>
  guideline.cells
    .filter((cell) => cell.requirement === "must")
    .map((cell) => ({ guideline, cell }))
);

for (const { guideline, cell } of mustCells) {
  console.log(guideline.id, cell.column, cell.summary_ja);
}
```

## Schema reference

```ts
export interface Guideline {
  id: string;
  name_ja: string;
  name_en: string;
  issuer: string;
  jurisdiction: string;
  type: string;
  url: string;
  source_documents?: Array<{ url: string; note_ja?: string; note_en?: string }>;
  tags?: string[];
  summary_ja?: string;
  cells: Cell[];
}

export interface Cell {
  column: string;
  requirement: "must" | "should" | "mention" | "none" | "not_assessed" | "source_unavailable";
  summary_ja: string;
  citation: Citation;
  notes_ja?: string;
}

export interface Citation {
  url: string;
  section?: string;
  retrieved?: string;
  confidence?: "high" | "medium" | "low";
}
```

## Source

The source corpus YAML files are maintained at:

https://github.com/cursorvers/medical-ai-governance-crosswalk/tree/main/corpus/guidelines

## License

CC-BY-4.0 for corpus content and MIT for package code.

## Versioning policy

This package follows semver.

- Patch: typo fixes, citation corrections, or non-schema content refinements.
- Minor: new guideline sources or governance columns.
- Major: schema changes that require consumer code updates.
