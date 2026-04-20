# FDA AI/ML SaMDアクションプラン・PCCPガイダンス

> **DISCLAIMER**: 本資料は公開ガイドラインの参照用コンパイルです。法的助言、規制適合性の保証、診療判断ではありません。利用前に必ず原文を参照してください。

| 項目 | 値 |
|---|---|
| ID | `fda-aiml-saamd-ap` |
| English | Artificial Intelligence/Machine Learning (AI/ML)-Based Software as a Medical Device (SaMD) Action Plan and PCCP Guidance |
| 発行主体 | U.S. Food and Drug Administration |
| 管轄 | us |
| 種別 | regulatory |
| Version | 2025.08 |
| Published | 2021-01-12 |
| Last reviewed | 2026-04-20 |
| Source | [official source](https://www.fda.gov/medical-devices/software-medical-device-samd/artificial-intelligence-and-machine-learning-software-medical-device) |

## Summary

FDAのAI/ML SaMD監督方針とPCCP提出推奨を整理し、TPLC・透明性・性能監視を示す。


## Cells

| 列 | 要求 | 要約 | Citation |
|---|---|---|---|
| A 適用対象 | 🟠 `should` | AI-DSFを含む医療機器と510(k)等の提出が主対象。 | [PCCP Guidance, Section III Scope / high](https://www.fda.gov/media/166704/download#page=9) |
| B リスク分類 | 🟠 `should` | IMDRFリスク分類やFDA便益リスクを踏まえた監督を想定。 | [Introduction &amp; Background; Action 1 / high](https://www.fda.gov/files/medical%20devices/published/AIML-SaMD-Action-Plan.pdf#page=2) |
| C 透明性 | 🟠 `should` | 学習データ、入力、ロジック、性能根拠等の透明性を推奨。 | [Action 3 Patient-Centered Approach Incorporating Transparency to Users / high](https://www.fda.gov/files/medical%20devices/published/AIML-SaMD-Action-Plan.pdf#page=5) |
| D 監査ログ | 🟠 `should` | PCCPではデータ管理、更新手順、追跡表で変更根拠を残す。 | [PCCP Guidance, Section VII.C Traceability / high](https://www.fda.gov/media/166704/download#page=33) |
| E Human oversight | 🔵 `mention` | 手動更新や臨床ワークフローで人の入力・判断の役割に触れる。 | [PCCP Guidance, Section III Scope / high](https://www.fda.gov/media/166704/download#page=9) |
| F データ品質バイアス | 🟠 `should` | バイアス識別・低減と頑健性評価の方法開発を重視。 | [Action 4 Regulatory Science Methods Related to Algorithm Bias &amp; Robustness / high](https://www.fda.gov/files/medical%20devices/published/AIML-SaMD-Action-Plan.pdf#page=6) |
| G PCCP市販後 | 🟠 `should` | PCCPは予定変更、実装方法、影響評価を提出に含める。 | [PCCP Guidance, Section V Policy for Predetermined Change Control Plans / high](https://www.fda.gov/media/166704/download#page=14) |
| H 責任 | 🟠 `should` | 製造業者がPCCPを作成し品質システムで影響評価する。 | [PCCP Guidance, Section VIII Impact Assessment / high](https://www.fda.gov/media/166704/download#page=34) |
| I 同意プライバシー | 🔵 `mention` | 患者中心の信頼・透明性を扱うが同意手続は主題外。 | [Action 3 Patient-Centered Approach Incorporating Transparency to Users / medium](https://www.fda.gov/files/medical%20devices/published/AIML-SaMD-Action-Plan.pdf#page=5) |
| J セキュリティ | 🔵 `mention` | GMLPを医療機器サイバーセキュリティ施策と連携すると記載。 | [Action 2 Good Machine Learning Practice (GMLP) / high](https://www.fda.gov/files/medical%20devices/published/AIML-SaMD-Action-Plan.pdf#page=4) |
| K 臨床評価 | 🟠 `should` | PCCPの性能評価・検証妥当性確認で安全有効性を示す。 | [PCCP Guidance, Section VII.B(3) Performance evaluation / high](https://www.fda.gov/media/166704/download#page=31) |
| L 国際整合 | 🔵 `mention` | GMLP標準化やIMDRF等との国際調和を推進。 | [Action 2 Good Machine Learning Practice (GMLP) / high](https://www.fda.gov/files/medical%20devices/published/AIML-SaMD-Action-Plan.pdf#page=4) |
| M ライフサイクル | 🟠 `should` | 開発前から市販後までTPLC監督とRWP監視を重視。 | [Introduction &amp; Background; Action 5 Real-World Performance (RWP) / high](https://www.fda.gov/files/medical%20devices/published/AIML-SaMD-Action-Plan.pdf#page=7) |

## Notes

---

**License / 引用スコープ**: 本サイトのオリジナル編集物 (マトリクス構造・要求強度判定・列定義・要約) は CC-BY 4.0。第三者ガイドライン原文の引用は各権利者帰属 (fair use / 著作権法第32条「引用」の範囲) で、CC-BY 対象外。詳細は [LICENSE](https://github.com/cursorvers/medical-ai-governance-crosswalk/blob/main/LICENSE) 参照。
