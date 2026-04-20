# 日本医師会 AIの臨床利用答申

> **DISCLAIMER**: 本資料は公開ガイドラインの参照用コンパイルです。法的助言、規制適合性の保証、診療判断ではありません。利用前に必ず原文を参照してください。

| 項目 | 値 |
|---|---|
| ID | `jmsf-ai-medical` |
| English | Japan Medical Association report on clinical use of AI and bioethics |
| 発行主体 | 日本医師会 |
| 管轄 | jp |
| 種別 | professional_guideline |
| Version | 2026.04.15 |
| Published | 2026-04-15 |
| Last reviewed | 2026-04-20 |
| Source | [official source](https://www.med.or.jp/dl-med/teireikaiken/20260415_3.pdf) |

## Summary

日本医師会のAI臨床利用に関する答申。医師主導、人間中心、情報管理、責任、生命倫理上の課題を整理する。


## Cells

| 列 | 要求 | 要約 | Citation |
|---|---|---|---|
| A 適用対象 | 🔵 `mention` | 医療AIの臨床利用全般と医師・患者・AIの関係を対象にする。 | [第1章 総論：医療AIの現状と課題 / medium](https://www.med.or.jp/dl-med/teireikaiken/20260415_3.pdf#page=1) |
| B リスク分類 | 🔵 `mention` | 臨床利用を3類型に分け、悪用や制度的リスクも整理する。 | [第3章 3.3.1 AIの臨床利用の3類型 / medium](https://www.med.or.jp/dl-med/teireikaiken/20260415_3.pdf#page=68) |
| C 透明性 | 🟠 `should` | AI使用の患者通知、透明性措置、医師確認を重視する。 | [第3章 3.3.2 記録・文書作成の補助 / medium](https://www.med.or.jp/dl-med/teireikaiken/20260415_3.pdf#page=69) |
| D 監査ログ | 🔵 `mention` | エラー報告、データ保存、AIモニタリングの必要性に触れる。 | [第3章 3.3.2; 第2章 2.8.7 / low](https://www.med.or.jp/dl-med/teireikaiken/20260415_3.pdf#page=69) |
| E Human oversight | 🟠 `should` | 医師参加型原則により医師が確認し最終判断を行う。 | [第3章 3.1.2 WMAが示す医師参加型原則 / medium](https://www.med.or.jp/dl-med/teireikaiken/20260415_3.pdf#page=53) |
| F データ品質バイアス | 🟠 `should` | バイアス、データセットシフト、精度劣化への注意を求める。 | [第3章 3.3.3 診断・治療の補助 / medium](https://www.med.or.jp/dl-med/teireikaiken/20260415_3.pdf#page=71) |
| G PCCP市販後 | 🔵 `mention` | 展開後の能力維持やAIによるAI監視を課題に挙げる。 | [第2章 2.8.7 さいごに / low](https://www.med.or.jp/dl-med/teireikaiken/20260415_3.pdf#page=51) |
| H 責任 | 🟠 `should` | 医師、開発者、行政を含む責任分担の必要性を示す。 | [第3章 3.3.3 診断・治療の補助 / medium](https://www.med.or.jp/dl-med/teireikaiken/20260415_3.pdf#page=72) |
| I 同意プライバシー | 🟠 `should` | 機微な診療情報の機密性、不正アクセス防止、同意を重視する。 | [第3章 3.1.2 WMAが示す医師参加型原則 / medium](https://www.med.or.jp/dl-med/teireikaiken/20260415_3.pdf#page=54) |
| J セキュリティ | 🟠 `should` | 診療情報の情報セキュリティとAI攻撃対策を慎重に検討する。 | [第3章 3.1.1 はじめに; 第2章 2.8.4 / medium](https://www.med.or.jp/dl-med/teireikaiken/20260415_3.pdf#page=53) |
| K 臨床評価 | 🔵 `mention` | 診断・治療補助では性能、透明性、医師判断への影響を検討する。 | [第3章 3.3.3 診断・治療の補助 / medium](https://www.med.or.jp/dl-med/teireikaiken/20260415_3.pdf#page=70) |
| L 国際整合 | 🔵 `mention` | WMA声明、日本AI法、国際倫理と国内戦略の整合を整理する。 | [第3章 3.1 医療AIを巡る国際倫理と日本の戦略 / medium](https://www.med.or.jp/dl-med/teireikaiken/20260415_3.pdf#page=53) |
| M ライフサイクル | 🔵 `mention` | 医師会の継続的関与と新たなガバナンス体制を求める。 | [第3章 3.1.4 まとめ; 第2章 2.8.7 / medium](https://www.med.or.jp/dl-med/teireikaiken/20260415_3.pdf#page=56) |

## Notes

### A 適用対象

答申全体の対象は臨床利用・生命倫理であり、規制上の適用範囲定義ではない。

### B リスク分類

要確認: 形式的なリスク分類表ではなく、倫理論点整理としての分類。

### C 透明性

AI使用の患者への通知、臨床医による確認、元データ保存が対策として挙げられる。

### D 監査ログ

要確認: 監査ログ要求そのものではなく、記録保存・エラー報告・監視体制への言及。

### E Human oversight

Physician-in-the-Loopとして、医学的専門性を持つ医師の介在と最終判断を説明する。

### F データ品質バイアス

診断・治療補助でバイアス、一般化可能性、データセットシフトを課題として整理する。

### G PCCP市販後

要確認: PCCPや市販後管理の制度要求ではなく、AIモニタリング体制の必要性としての言及。

### H 責任

WMA声明に関連し、ステークホルダー間の連携と責任分担の必要性を述べる。

### I 同意プライバシー

患者データの取扱いで機密性、不正アクセス防止、透明性、各国法令遵守に言及する。

### J セキュリティ

診療情報の情報セキュリティ、敵対的攻撃、データポイズニングを課題として扱う。

### K 臨床評価

要確認: 承認申請用の臨床評価要求ではなく、臨床利用上の倫理・性能課題として確認。

### L 国際整合

国際倫理と国内制度を人間中心AIの方向性として対比・接続している。

### M ライフサイクル

ライフサイクル要求ではなく、医療DXとAI臨床利用に関する継続的な制度・倫理対応として確認。

---

**License / 引用スコープ**: 本サイトのオリジナル編集物 (マトリクス構造・要求強度判定・列定義・要約) は CC-BY 4.0。第三者ガイドライン原文の引用は各権利者帰属 (fair use / 著作権法第32条「引用」の範囲) で、CC-BY 対象外。詳細は [LICENSE](https://github.com/cursorvers/medical-ai-governance-crosswalk/blob/main/LICENSE) 参照。
