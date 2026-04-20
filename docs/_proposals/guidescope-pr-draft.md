# feat(mcp): add medical-paper-governance crosswalk lookup tool

## Summary

Add the corpus npm package as a dependency and implement `query_governance_crosswalk` in the MCP package.

## Changes

- `packages/mcp/package.json`: add dependency on `@cursorversinc/guidescope-medical-corpus`.
- `packages/mcp/src/index.ts`: add tool registration.
- `packages/mcp/src/tools/governance-crosswalk.ts`: add crosswalk query tool implementation.

## Test plan

- [ ] `tools/list` returns 5 tools (was 4).
- [ ] `query_governance_crosswalk("clinician", "IRB")` returns matching cells.
- [ ] エラー時 graceful fallback.
- [ ] バンドルサイズ < +150 KB.
- [ ] 既存4 tools 動作変わらず.

## Backwards compat

純加算、breaking なし。

## Related

https://github.com/cursorvers/medical-ai-governance-crosswalk
