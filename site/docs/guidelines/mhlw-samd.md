# 厚労省 医療機器プログラムに関する取扱い

> **DISCLAIMER**: 本資料は公開ガイドラインの参照用コンパイルです。法的助言、規制適合性の保証、診療判断ではありません。利用前に必ず原文を参照してください。

| 項目 | 値 |
|---|---|
| ID | `mhlw-samd` |
| English | MHLW Handling of Software as a Medical Device |
| 発行主体 | Ministry of Health, Labour and Welfare |
| 管轄 | jp |
| 種別 | regulatory |
| Version | 2023-03-31 partial revision |
| Published | 2023-03-31 |
| Last reviewed | 2026-04-20 |
| Source | [official source](https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/0000179749_00004.html) |

## Summary

厚労省が医療機器プログラムの該当性、除外例、判断手順、リスク分類、相談窓口を示す公式情報。


## Cells

| 列 | 要求 | 要約 | Citation |
|---|---|---|---|
| A 適用対象 | 🔴 `must` | 医療目的と生命健康リスクで医療機器プログラム該当性を判断。 | [1 はじめに / 2(1) 医療機器プログラムの範囲 / high](https://www.mhlw.go.jp/content/11120000/001082227.pdf) |
| B リスク分類 | 🔴 `must` | クラスIからIVとGHTFルールでリスク程度を判定。 | [6 人の生命及び健康に影響を与えるリスクの程度の考え方 / high](https://www.mhlw.go.jp/content/11120000/001082227.pdf) |
| C 透明性 | 🟠 `should` | 非医療機器表示や根拠の検証可能性で誤認防止を求める。 | [5(1) 事前準備 / 8(1) 標ぼうの留意事項 / high](https://www.mhlw.go.jp/content/11120000/001082227.pdf) |
| D 監査ログ | 🔵 `mention` | 個人健康記録の収集・ログ作成は非該当例として言及。 | [4(3) 使用者が自らの医療・健康情報を閲覧等するプログラム / high](https://www.mhlw.go.jp/content/11120000/001082227.pdf) |
| E Human oversight | 🔵 `mention` | 医療関係者の管理下かを使用者分類で確認。 | [5(1) 事前準備（使用目的、処理方法などの明確化・整理） / high](https://www.mhlw.go.jp/content/11120000/001082227.pdf) |
| F データ品質バイアス | 🟠 `should` | 根拠情報とアルゴリズム妥当性の検証可能性を整理。 | [5(1) 判断のために明確にすべき項目の例示 / high](https://www.mhlw.go.jp/content/11120000/001082227.pdf) |
| G PCCP市販後 | ⚪ `none` | PCCPや市販後監視の明示的扱いは確認できず。 | [全文確認（該当記述なし） / medium](https://www.mhlw.go.jp/content/11120000/001082227.pdf) |
| H 責任 | 🟠 `should` | 事業者・開発者が使用者、目的、処理方法を確認整理。 | [5(1) 事前準備 / 8(2) 適正使用のための周知啓発 / high](https://www.mhlw.go.jp/content/11120000/001082227.pdf) |
| I 同意プライバシー | 🔵 `mention` | 個人健康記録の保存・共有例はあるが同意義務は未確認。 | [4(3) 使用者が自らの医療・健康情報を閲覧等するプログラム / high](https://www.mhlw.go.jp/content/11120000/001082227.pdf) |
| J セキュリティ | ⚪ `none` | セキュリティ要求の明示的扱いは確認できず。 | [全文確認（該当記述なし） / medium](https://www.mhlw.go.jp/content/11120000/001082227.pdf) |
| K 臨床評価 | 🔵 `mention` | 治験・臨床研究での提供と適用関係に言及。 | [7 臨床研究等における取扱いについて / high](https://www.mhlw.go.jp/content/11120000/001082227.pdf) |
| L 国際整合 | 🔵 `mention` | GHTF分類を用い、IMDRF分類因子は参考可能と記載。 | [6 人の生命及び健康に影響を与えるリスクの程度の考え方 脚注11 / high](https://www.mhlw.go.jp/content/11120000/001082227.pdf) |
| M ライフサイクル | 🔵 `mention` | 規制範囲は今後変更可能で、適正使用周知にも言及。 | [2(2) 基本的考え方 / 8(2) 適正使用のための周知啓発 / high](https://www.mhlw.go.jp/content/11120000/001082227.pdf) |

## Notes

### A 適用対象

疾病診断・治療・予防目的とリスクを該当性判断の中核としている。

### B リスク分類

SaMDも有体物にインストールされた状態を想定し、原則同様に判定する。

### C 透明性

「望ましい」記述を含むためshould判定。

### D 監査ログ

監査ログ義務ではなく、記録・ログ作成を行う非該当例としての言及。

### E Human oversight

Human oversight義務ではなく、該当性判断の使用者分類として確認。

### F データ品質バイアス

バイアスを直接扱う記述ではなく、根拠・妥当性確認として判定。

### G PCCP市販後

本ガイドラインは医療機器該当性判断が主題。

### H 責任

「確認、整理、精査等すること」や周知啓発の重要性からshould判定。

### I 同意プライバシー

プライバシーや同意の要求としてではなく、非該当例の説明として確認。

### J セキュリティ

本ガイドラインは該当性判断が主題で、サイバー要件は扱っていない。

### K 臨床評価

臨床評価手法の要求ではなく、臨床研究での法適用関係への言及。

### L 国際整合

GHTFはリスク分類で直接使用、IMDRFは参考可能とされる。

### M ライフサイクル

ライフサイクル全体の管理要求ではなく、変更可能性と適正使用への言及。

---

**License / 引用スコープ**: 本サイトのオリジナル編集物 (マトリクス構造・要求強度判定・列定義・要約) は CC-BY 4.0。第三者ガイドライン原文の引用は各権利者帰属 (fair use / 著作権法第32条「引用」の範囲) で、CC-BY 対象外。詳細は [LICENSE](https://github.com/cursorvers-inc/medical-ai-governance-crosswalk/blob/main/LICENSE) 参照。
