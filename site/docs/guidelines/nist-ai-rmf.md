# NIST AIリスクマネジメントフレームワーク

> **DISCLAIMER**: 本資料は公開ガイドラインの参照用コンパイルです。法的助言、規制適合性の保証、診療判断ではありません。利用前に必ず原文を参照してください。

| 項目 | 値 |
|---|---|
| ID | `nist-ai-rmf` |
| English | NIST Artificial Intelligence Risk Management Framework 1.0 and Generative AI Profile |
| 発行主体 | National Institute of Standards and Technology |
| 管轄 | us |
| 種別 | framework |
| Version | AI RMF 1.0 + NIST AI 600-1 |
| Published | 2023-01-26 |
| Last reviewed | 2026-04-20 |
| Source | [official source](https://www.nist.gov/itl/ai-risk-management-framework) |

## Summary

NISTの任意AIリスク管理枠組み。Govern/Map/Measure/Manageと生成AIプロファイルを示す。


## Cells

| 列 | 要求 | 要約 | Citation |
|---|---|---|---|
| A 適用対象 | 🟠 `should` | AIの設計・開発・利用・評価で信頼性リスク管理を促す。 | [Overview of the AI RMF / high](https://www.nist.gov/itl/ai-risk-management-framework#main-content) |
| B リスク分類 | 🟠 `should` | 文脈に応じてリスク許容度、優先度、影響を評価する。 | [Section 3; MAP 4-5; MANAGE 1 / high](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf#page=32) |
| C 透明性 | 🟠 `should` | 透明性、説明可能性、解釈可能性を信頼性特性に含める。 | [Section 4; MEASURE 2.8 / high](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf#page=35) |
| D 監査ログ | 🟠 `should` | 文書化、インベントリ、来歴、監視結果の記録を求める。 | [GOVERN 1.5-1.6; MEASURE 2.8 / high](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf#page=20) |
| E Human oversight | 🟠 `should` | 人間判断とHuman-AI構成の役割を明確化する。 | [GOVERN 3.2; MAP 3.4 / high](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf#page=30) |
| F データ品質バイアス | 🟠 `should` | 公平性、有害バイアス、データ代表性を測定・管理する。 | [Section 4; MEASURE 2.11 / high](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf#page=23) |
| G PCCP市販後 | 🟠 `should` | 展開後監視、改善、事故・エラー連絡を管理機能に含める。 | [MANAGE 4.1-4.3 / high](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf#page=38) |
| H 責任 | 🟠 `should` | 役割、責任、説明責任メカニズムを組織に求める。 | [GOVERN 2.1-2.3; Section 3.4 / high](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf#page=28) |
| I 同意プライバシー | 🟠 `should` | プライバシー強化と同意等の生成AIプライバシーリスクを扱う。 | [GAI Risks: Data Privacy; MEASURE 2.10 / high](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf#page=24) |
| J セキュリティ | 🟠 `should` | セキュアでレジリエントなAIと情報セキュリティを評価する。 | [GAI Risks: Information Security; MEASURE 2.7 / high](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf#page=21) |
| K 臨床評価 | 🟠 `should` | TEVV、妥当性、信頼性、性能限界を測定・文書化する。 | [MEASURE 2.1-2.6 / high](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf#page=34) |
| L 国際整合 | 🔵 `mention` | 他のリスク管理努力との整合と国際的利用を意図する。 | [Overview of the AI RMF; AIRC / high](https://www.nist.gov/itl/ai-risk-management-framework#main-content) |
| M ライフサイクル | 🟠 `should` | Govern/Map/Measure/ManageをAIライフサイクル全体に適用する。 | [Section 5; Tables 1-4 / high](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf#page=26) |

## Notes

### A 適用対象

任意利用の枠組みであり、医療AI専用ではなくAI製品・サービス・システム全般を対象にする。

### B リスク分類

法的クラス分類ではなく、組織の文脈・影響・リスク許容度に基づくリスクベース管理。

### C 透明性

Generative AI Profileも来歴、生成物透明性、文書化のプロセスを扱う。

### D 監査ログ

生成AIプロファイルはデータ来歴、インシデント監視、改変履歴の追跡可能性を具体化する。

### E Human oversight

自動化バイアス、過信、擬人化など人間とAIの相互作用リスクを扱う。

### F データ品質バイアス

AI RMFは公平性と有害バイアス管理を信頼性特性に含める。

### G PCCP市販後

PCCP固有用語ではないが、展開後の監視計画と継続改善を扱う。

### H 責任

組織コミットメント、責任、意思決定ラインをAIリスク管理の前提とする。

### I 同意プライバシー

個人データ、目的特定、個人参加、同意、機微データ露出をリスクとして扱う。

### J セキュリティ

プロンプト注入、データポイズニング、モデル抽出等の生成AI脅威も含む。

### K 臨床評価

医療AI固有の臨床評価ではないが、試験・評価・検証・妥当性確認を扱う。

### L 国際整合

NISTページはAI RMFが他者のAIリスク管理努力と整合・支援することを説明する。

### M ライフサイクル

GOVERNは全段階、MAP/MEASURE/MANAGEは各ライフサイクル段階で適用可能とされる。

---

**License / 引用スコープ**: 本サイトのオリジナル編集物 (マトリクス構造・要求強度判定・列定義・要約) は CC-BY 4.0。第三者ガイドライン原文の引用は各権利者帰属 (fair use / 著作権法第32条「引用」の範囲) で、CC-BY 対象外。詳細は [LICENSE](https://github.com/cursorvers-inc/medical-ai-governance-crosswalk/blob/main/LICENSE) 参照。
