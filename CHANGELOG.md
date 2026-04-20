# Changelog

## v0.1.0 - 2026-04-20

- LP: 「このAI、うちで使って大丈夫？」を 30 秒で 10 GL × 13 列から引ける静的サイト。
- Trust Bar / 監修者募集 / 更新履歴を Hero 直下に配置。
- 使い方シナリオ (5 場面) + 用語集 + Evidence Pack (5 テンプレ) 同梱。
- 4 サーフェス展開: npm `@cursorversinc/guidescope-medical-corpus` (corpus.json) / `@cursorversinc/medgov-cli` (`medgov` コマンド) / `@cursorversinc/medgov-mcp` (Claude Desktop / Cursor 用 MCP server, 5 tools)。
- CI: `validate_corpus` + `mkdocs --strict` を push/PR で実行、月次 `source-freshness` で原文 drift を Issue 自動起票。
- 130/130 セル充填、引用 URL + 節 + 取得日 + 信頼度 (low 16%) を全セルに付与。
