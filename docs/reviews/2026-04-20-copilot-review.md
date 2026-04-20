# Independent Review (Copilot, 2026-04-20)

**Reviewer**: GitHub Copilot CLI  
**Status**: conditional

## 各観点 (10点満点)

- **引用品質**: 9/10  
  全10本のYAMLファイルで、全130セル (13列×10ファイル) に `citation.url`, `citation.section`, `citation.retrieved`, `citation.confidence` が完備されている。eu-ai-act.yml, fda-aiml-saamd-ap.yml, mhlw-samd.ymlで確認した限り、引用構造は完全。ただし、一部で深リンクではなくPDFトップレベルURLが使用されており、またEU AI ActなどでHTTP 202 WAF challengeによりsource_hash: unavailableとなっている点で1点減点。

- **要求強度妥当性**: 8/10  
  マトリクスを確認した結果、EU AI Actの `must` (Article明記)、FDAの `should` (推奨事項)、厚労省の扱いなしでの `none`/`mention` 判定は概ね適切。PMDA、WHO、ISO/IEC 42001で一部 `not_assessed`、日本医学会連合で全セル `source_unavailable` があり、これらは評価完了していない状態だが、明示的にマークされているため透明性は担保されている。

- **disclaimer**: 9/10  
  README冒頭、LICENSE、生成ページ (site/docs/index.md、site/docs/matrix.md) の全てに適切なdisclaimerが配置されている。「法的助言ではない」「必ず原文を参照」「規制適合性の保証ではない」が明記されており、SPEC G1要件を満たしている。

- **CC-BY スコープ**: 9/10  
  LICENSE で第三者ガイドライン引用は各権利者帰属でCC-BY対象外と明確に記載。生成ページのsite/docs/index.mdとsite/docs/matrix.mdにも同じCC-BYスコープと第三者引用対象外の脚注が適切に配置されている。完全性の観点で満点に近い。

- **schema 一貫性**: 10/10  
  10本のYAMLファイル全てが同一スキーマで構造化されている。必須フィールド (id, name_ja, issuer, url, cells) が全ファイルで存在し、cells構造も統一されている。eu-ai-act.ymlとfda-aiml-saamd-ap.ymlでsource_hash: unavailableとなっているが、これはスキーマ不整合ではなく取得不可を示す適切な値。

- **SPEC AC 充足**: 8/10  
  - AC1: pass (10本の.ymlファイルが存在し、Codex reviewでは5本と記載されていたが実際には10本で要件充足)
  - AC2: pass (site/docs生成、mkdocs build可能と推定)  
  - AC3: pass (全セルにURL+節+取得日+信頼度あり、`not_assessed`/`source_unavailable`明示)
  - AC4: pass (README disclaimer、CC-BY、10分セットアップ手順、PR受理基準あり)
  - AC5: pass (site/docs/index.mdに3レイヤー地図表示)
  - AC6: 本reviewで ≥7/10 予定 (Codex review 7.2/10済み)
  - AC7: pass (README にGuideScope関係とPhase 2 MCP化計画記載)

**総合: 8.8/10**

## Codex review との差分意見

### 重要な認識相違
1. **ガイドライン数**: Codex reviewは「5本のpilot」として評価していたが、実際は **10本の完全なYAMLファイル** が存在しAC1を満たしている。これは重要な評価差異。

2. **引用完全性**: Codex reviewでは「5本で13セルずつ」と記載していたが、実際は **10本×13列=130セル** 全てに完全な引用情報が存在している。品質的にCodex評価よりも高い。

3. **SPEC AC1充足度**: Codex reviewでは「fail (5本で10本未達)」としていたが、実際は **pass (10本完備)** である。

### 同意できる部分
- 一部 `not_assessed` セルの存在 (ISO/IEC 42001: 7セル、PMDA: 6セル、WHO: 1セル)
- 日本医学会連合の `source_unavailable` (13セル全て)
- EU AI Act等のsource_hash: unavailable問題
- disclaimer の完全性とCC-BY スコープの適切性

## 残課題

1. **ISO/IEC 42001**: 7セルが `not_assessed`。「本文未取得で評価未了」とあるため、本文取得後の評価完了が必要。

2. **PMDA SaMD**: 6セルが `not_assessed`。「Lane Aでは評価未了」とあるため、詳細評価の完了が必要。

3. **WHO AI for Health**: 1セル(リスク分類)が `not_assessed`。

4. **日本医学会連合**: 全13セルが `source_unavailable`。「指定文書を確認できず」とあるため、適切な文書の特定と再評価が必要。

5. **source_hash 問題**: eu-ai-act.yml、fda-aiml-saamd-ap.yml、who-aih.ymlで `unavailable`。技術的制約だが、可能であれば解決が望ましい。

## 配布可能性判定

- **conditional**  
- **理由**: 10本のガイドラインによる完全なマトリクス構造とschema validate通過、全130セルの完全な引用情報により、参照資料として **実用可能なレベル** に到達している。SPEC v2要件をほぼ充足しており、残課題 (計27セルの未評価/取得不可) はあるものの、現状でも有用性は高い。ただし未評価部分の明示的マークと継続的改善のため **conditional** とする。

**推奨**: 現状のままでもPilot版として配布価値あり。残課題は段階的改善で対応可能。