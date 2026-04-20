# Final Review (2026-04-20)

**Reviewer**: Codex (Kernel orchestration)
**Status**: conditional — Pilot v0.1 (5本) 配布可能、SPEC v2 完全版は Wave 2 完了後

---

# Final Review

## 修正内容
- mkdocs.yml: `docs_dir: site/docs`、`site_dir: site/public` に変更し、`docs_dir: .` と `exclude_docs` を削除。nav は Home (`index.md`)、マトリクス (`matrix.md`)、ガイドライン一覧 (`guidelines/index.md`)、列定義 (`columns.md`) に整理。
- scripts/build_site.py: nav 対象の `site/docs/guidelines/index.md` を生成するよう修正。
- scripts/build_site.py: `site/docs/matrix.md` の表が 1 行に潰れていたため、マトリクスを行単位で生成する実装に修正。
- scripts/validate_corpus.py: FDA/WHO の URL チェックで独自 User-Agent が false positive を起こしていたため、URL 検証用 User-Agent を `curl/8.7.1` に変更。

## `mkdocs build --strict` 結果
- pass
- 実行: `.venv/bin/python scripts/validate_corpus.py && .venv/bin/python scripts/build_site.py && .venv/bin/mkdocs build --strict`
- エラーなし。Material for MkDocs から MkDocs 2.0 に関する upstream warning が出るが、build は成功。
- MkDocs info: `guidelines/*.md` は nav 直下には含まれないが、`guidelines/index.md` からリンクされている。指定 nav には合致。
- 追加確認: `.venv/bin/python scripts/validate_corpus.py --check-urls` も pass。

## Review スコア (10点満点)
- 引用品質: 8/10, 5 本の guideline YAML すべてで 13 cell があり、全 cell に `citation.url`, `citation.section`, `citation.retrieved`, `citation.confidence` がある。URL チェックも pass。ただし深リンクではない PDF/ページ単位 URL が多く、PMDA/WHO に `not_assessed` cell が残る。
- 要求強度妥当性: 7/10, EU AI Act の `must`、FDA PCCP/Action Plan の `should`、MHLW の `none`/`mention` は概ねルーブリックと整合。明らかな捏造は見当たらない。一方、PMDA の相談ページ由来 cell は `should` とするには弱い可能性があり、WHO 倫理原則の一部 `should` は規制要求ではなく原則/推奨としての注意書きが必要。
- disclaimer: 8/10, README 冒頭、LICENSE、生成ページすべてに disclaimer がある。生成ページの各 cell 末尾には SPEC G1 の「原文を必ず参照」に相当する固定文はなく、ページ冒頭 disclaimer で代替している。
- CC-BY スコープ: 9/10, LICENSE で第三者 guideline text は各権利者帰属で CC-BY 対象外と明記されている。生成ページ側には同じ CC-BY スコープ脚注がないため満点ではない。
- schema 一貫性: 8/10, 5 本すべてが同じ cell schema で `scripts/validate_corpus.py` を pass し、13 列も揃っている。ただし SPEC G3 の `source_hash` は `eu-ai-act.yml` と `fda-aiml-saamd-ap.yml` で未設定で、validator の必須項目にも入っていない。
- SPEC AC 充足: 5.5/10
  - AC1: fail。`corpus/guidelines/` は 5 本で、SPEC の 10 本に未達。ただし 5 本は schema validate pass。
  - AC2: pass。`scripts/build_site.py` が `site/docs` を生成し、`mkdocs build --strict` 成功。
  - AC3: partial/pass。現存 5 本の全 cell は URL、節/段落、取得日、信頼度を持つ。10 本未達と `not_assessed` 残存が減点。
  - AC4: partial。README 冒頭 disclaimer、CC-BY、PR 受理基準、GuideScope 関係はあるが、10 分セットアップ手順がない。
  - AC5: pass。site top に 3 レイヤー地図がある。
  - AC6: fail/未証跡。今回の Final Review は作成したが、Copilot review ≥7/10 の実ファイル証跡は確認できない。
  - AC7: pass。README に GuideScope 本家との関係と Phase 2 MCP 化計画がある。
**総合: 7.2/10**

## 残課題 (優先順)
1. SPEC AC1 を満たすため、Pilot v0.1 以外の 5 YAML を追加するか、SPEC を 5 本初版に明示的に変更する。
2. PMDA/WHO の `not_assessed` cell を評価完了し、必要に応じて requirement と confidence を更新する。
3. `source_hash` を全 guideline YAML で必須化し、`scripts/validate_corpus.py` の `TOP_REQUIRED` に追加する。
4. README に 10 分セットアップ手順を追加する。
5. 生成ページ末尾に CC-BY スコープと第三者引用対象外の短い脚注を追加する。
6. Copilot review ≥7/10 の証跡を `docs/` または review artifact として保存する。

## 配布可能性判定
- conditional
- 理由: build、schema validate、URL validate は通り、5 本 pilot としては配布可能。ただし SPEC v2 の 10 本要件、README 10 分セットアップ、Copilot review 証跡、未評価 cell が残っているため、SPEC 完全充足版としては未完了。
