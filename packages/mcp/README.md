# @cursorversinc/medgov-mcp

Model Context Protocol (MCP) server exposing the **medical AI governance crosswalk** — 13 columns × 10 guidelines (PMDA, FDA, EU AI Act, WHO, IMDRF, ISO/IEC 42001, NIST AI RMF, 厚労省, 経産省, 日本医師会).

Lets Claude Desktop / Cursor / any MCP host look up governance requirements, citations, and strength levels (`must` / `should` / `mention` / `none`) directly from your dev loop.

## Install (Claude Desktop / Cursor)

Add to your MCP config:

```json
{
  "mcpServers": {
    "medgov": {
      "command": "npx",
      "args": ["-y", "@cursorversinc/medgov-mcp"]
    }
  }
}
```

Restart the host. The following tools become available:

| Tool | Description |
| ---- | ----------- |
| `search_medical_governance` | Free-text search across columns, keywords, and cell summaries. |
| `get_column` | Full detail for one column (A–M). |
| `get_guideline` | All 13 cells belonging to one guideline. |
| `list_guidelines` | 10 guidelines (id + display name). |
| `list_columns` | 13 columns (id + ja/en name + cell count). |

## Local development

```
pnpm install
pnpm -F @cursorversinc/medgov-mcp build
node packages/mcp/dist/index.js   # server listens on stdio
```

The `prebuild` step copies the latest `site/docs/assets/lookup-index.json` into `src/` so the server always ships with the current corpus.

## Data source

Corpus is generated from `corpus/*.yml` in the parent repo and emitted to `site/docs/assets/lookup-index.json`. Schema:

```
{
  "columns": {
    "A".."M": {
      "name": "<ja>",
      "name_en": "<en>",
      "cells": [
        { "guideline", "guideline_id", "strength", "summary", "citation_url", "confidence" }
      ]
    }
  },
  "keywords": { "<kw>": ["<column_id>", ...] }
}
```

## License

CC-BY-4.0 — corpus is a curated citation overlay, not a regulatory filing.
