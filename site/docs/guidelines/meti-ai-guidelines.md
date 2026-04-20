# 経済産業省 AI事業者ガイドライン

> **DISCLAIMER**: 本資料は公開ガイドラインの参照用コンパイルです。法的助言、規制適合性の保証、診療判断ではありません。利用前に必ず原文を参照してください。

| 項目 | 値 |
|---|---|
| ID | `meti-ai-guidelines` |
| English | AI Guidelines for Business |
| 発行主体 | 経済産業省 |
| 管轄 | jp |
| 種別 | governmental_guideline |
| Version | 1.2 |
| Published | 2026-03-31 |
| Last reviewed | 2026-04-20 |
| Source | [official source](https://www.meti.go.jp/shingikai/mono_info_service/ai_shakai_jisso/index.html) |

## Summary

AI開発者・提供者・利用者向けに、人間中心、リスクベース、透明性等を示す日本政府指針。


## Cells

| 列 | 要求 | 要約 | Citation |
|---|---|---|---|
| A 適用対象 | 🟠 `should` | AI開発者、提供者、利用者を主対象にする。 | [第1部 2. 対象 / high](https://www.meti.go.jp/shingikai/mono_info_service/ai_shakai_jisso/pdf/20260331_1.pdf) |
| B リスク分類 | 🟠 `should` | 危害の大きさと蓋然性に応じたリスクベース対応を重視。 | [第1部 はじめに; リスクベースアプローチ / high](https://www.meti.go.jp/shingikai/mono_info_service/ai_shakai_jisso/pdf/20260331_1.pdf) |
| C 透明性 | 🟠 `should` | ステークホルダーへの情報提供で透明性を高める。 | [第2部 B. 6) 透明性 / high](https://www.meti.go.jp/shingikai/mono_info_service/ai_shakai_jisso/pdf/20260331_1.pdf) |
| D 監査ログ | 🟠 `should` | 判断過程、判断根拠等のログ記録・保存を求める。 | [第2部 B. 6) 透明性 / high](https://www.meti.go.jp/shingikai/mono_info_service/ai_shakai_jisso/pdf/20260331_1.pdf) |
| E Human oversight | 🟠 `should` | 人間中心の考え方に基づく開発・提供・利用を求める。 | [第2部 A. 基本理念; B. 1) 人間中心 / high](https://www.meti.go.jp/shingikai/mono_info_service/ai_shakai_jisso/pdf/20260331_1.pdf) |
| F データ品質バイアス | 🟠 `should` | データの正確性・最新性と回避不能なバイアス認識を求める。 | [第2部 B. 2) 安全性; 3) 公平性 / high](https://www.meti.go.jp/shingikai/mono_info_service/ai_shakai_jisso/pdf/20260331_1.pdf) |
| G PCCP市販後 | 🟠 `should` | ライフサイクル全体でリスク対策と環境変化対応を行う。 | [第1部 はじめに; 第2部 B. 共通の指針 / high](https://www.meti.go.jp/shingikai/mono_info_service/ai_shakai_jisso/pdf/20260331_1.pdf) |
| H 責任 | 🟠 `should` | 各主体の役割に応じ合理的範囲で説明責任を果たす。 | [第2部 B. 7) アカウンタビリティ / high](https://www.meti.go.jp/shingikai/mono_info_service/ai_shakai_jisso/pdf/20260331_1.pdf) |
| I 同意プライバシー | 🟠 `should` | 個人情報保護法等を踏まえプライバシー保護を検討する。 | [第2部 B. 4) プライバシー保護 / high](https://www.meti.go.jp/shingikai/mono_info_service/ai_shakai_jisso/pdf/20260331_1.pdf) |
| J セキュリティ | 🟠 `should` | 不正操作や外部攻撃に備えセキュリティを確保する。 | [第2部 B. 5) セキュリティ確保 / high](https://www.meti.go.jp/shingikai/mono_info_service/ai_shakai_jisso/pdf/20260331_1.pdf) |
| K 臨床評価 | ⚪ `none` | 医療AI固有の臨床評価要求は本編確認範囲で扱いなし。 | [本編確認範囲; 医療固有臨床評価なし / medium](https://www.meti.go.jp/shingikai/mono_info_service/ai_shakai_jisso/pdf/20260331_1.pdf) |
| L 国際整合 | 🔵 `mention` | NIST、ISO、EU AI法等の海外原則・標準を参照する。 | [第1部 はじめに; 第2部 B. 6) 透明性 / high](https://www.meti.go.jp/shingikai/mono_info_service/ai_shakai_jisso/pdf/20260331_1.pdf) |
| M ライフサイクル | 🟠 `should` | AIライフサイクル全体で自主的な対策実行を促す。 | [第1部 はじめに; 第2部 B. 共通の指針 / high](https://www.meti.go.jp/shingikai/mono_info_service/ai_shakai_jisso/pdf/20260331_1.pdf) |

## Notes

### A 適用対象

業務外利用者やデータ提供者は対象外だが、必要な対応には言及する。

### B リスク分類

医療機器分類ではなく、AI利用形態に伴う社会的リスクの大きさに対応する考え方。

### C 透明性

出力過程、根拠、判断根拠等の説明可能性・解釈可能性にも触れる。

### D 監査ログ

ログ保存は原因究明やトレーサビリティ、説明責任と接続して説明される。

### E Human oversight

AIに単独判断させず適切なタイミングで人が関与する趣旨の記述を含む。

### F データ品質バイアス

学習等に用いるデータの適切性、バイアス要因、技術要素と利用者振る舞いを扱う。

### G PCCP市販後

PCCP用語はないが、AIの開発・提供・利用と実運用後の変化対応を扱う。

### H 責任

責任者の設定、方針策定・公表、リスク対応状況の説明を扱う。

### I 同意プライバシー

プライバシーポリシー、国際的個人データ保護原則、越境移転にも言及。

### J セキュリティ

AIシステムの振る舞い改変、停止、プロンプト等への攻撃を含むリスクに触れる。

### K 臨床評価

安全性評価や品質には触れるが、医療機器の臨床評価要求としては確認できない。

### L 国際整合

NIST AI RMF、ISO/IEC JTC1/SC42、EU AI法等を参考情報として扱う。

### M ライフサイクル

AI開発、提供、利用、実運用後、更新・再学習を含む継続的対応を前提にする。

---

**License / 引用スコープ**: 本サイトのオリジナル編集物 (マトリクス構造・要求強度判定・列定義・要約) は CC-BY 4.0。第三者ガイドライン原文の引用は各権利者帰属 (fair use / 著作権法第32条「引用」の範囲) で、CC-BY 対象外。詳細は [LICENSE](https://github.com/cursorvers/medical-ai-governance-crosswalk/blob/main/LICENSE) 参照。
