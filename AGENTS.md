# CLAUDE.md -- medical-paper-governance (medgov)

Medical AI Governance Crosswalk: cited requirement-level matrix across 10 international
guidelines x 13 governance columns. Targets AI USERS (clinicians, clinical researchers,
hospital IT/safety, IRB). SaMD manufacturer approval workflows are OUT OF SCOPE.

## Positioning

This project serves people who USE medical AI, not those who BUILD/manufacture it.
Never frame outputs as SaMD submission artifacts or regulatory filings.

## Tech stack

- Corpus (SSOT): `corpus/guidelines/*.yml` + `corpus/columns/columns.yml`
- Site generator: Python scripts (`scripts/build_site.py`) + MkDocs Material
- Evidence Pack: Jinja2 templates in `templates/*.md.j2` -> `build/evidence/`
- JS/TS packages (pnpm workspace): `packages/cli`, `packages/mcp`, `packages/guidescope-medical-corpus`
- CI: GitHub Actions (`.github/workflows/ci.yml`, `source-freshness.yml`)

## Key directories

- `corpus/` -- YAML source of truth for all guideline cells
- `scripts/` -- Python build/validation/freshness tooling
- `templates/` -- Jinja2 Evidence Pack templates (archived SaMD template in `_archived/`)
- `packages/cli/` -- `@cursorversinc/medgov-cli` npm package
- `packages/mcp/` -- `@cursorversinc/medgov-mcp` MCP server
- `site/docs/` -- generated MkDocs source; `site/public/` -- built output
- `state/` -- source-freshness baseline JSON
- `docs/` -- SPEC, SCHEMA, RUBRIC, ROADMAP, maintenance docs

## Commands

```bash
# Python (activate venv first)
.venv/bin/python scripts/validate_corpus.py        # YAML schema validation
.venv/bin/python scripts/build_site.py             # generate site/docs + site/public
.venv/bin/python scripts/generate_evidence_pack.py # generate Evidence Pack
.venv/bin/python -m mkdocs build --strict          # strict MkDocs build
.venv/bin/mkdocs serve                             # dev server at localhost:8000

# JS/TS packages
pnpm build:all                                     # build CLI + MCP
pnpm build:mcp                                     # build MCP server only
pnpm build:cli                                     # build CLI only
```

## Constraints

- Corpus YAML is the single source of truth. Every cell requires: source URL, section/paragraph number, retrieval date, confidence level.
- `build_site.py` uses selective file writes (not destructive rmtree). Edit with care.
- The `samd-consultation-prep` template is archived; excluded from default generation.
- License: CC BY 4.0.
