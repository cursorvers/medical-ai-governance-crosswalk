# PCCP (Predetermined Change Control Plan) 骨子テンプレート

> **目的**: AI/ML SaMD の予定変更を、対象定義、変更計画、変更プロトコル、影響評価、検証戦略、報告/通知計画に分けて整理する。
> **対象**: AI/ML SaMD、臨床意思決定支援、モデル更新を伴う医療AI製品の開発・薬事・品質保証チーム。

## いつ使う？

**シーン 3: アルゴリズム更新リスクの判定** — 運用中AI医療機器のベンダー更新通知を受けたとき、PMDA / FDA / EU AI Act の PCCP 関連条項を横断比較し、更新前後のリスク差分・モニタリング項目・再評価トリガーをこの骨子に整理して院内AI委員会の承認文書とします。詳しい流れは [使い方シナリオ #3](../usage.md#3) を参照。

## 基本情報 (利用者記入欄)

| 項目 | 記入欄 |
|---|---|
| 製品名 / モデル名 |  |
| モデルバージョン / リリース単位 |  |
| 意図する使用 / 対象患者 |  |
| 入力データ |  |
| 出力 / 推奨 / 判定 |  |
| 変更管理責任者 |  |
| 品質システム上の承認経路 |  |
| PCCP対象外とする変更 |  |

## 参照ガイドライン

| ガイドライン | 要約 | 原文 |
|---|---|---|
| FDA | FDAのAI/ML SaMD監督方針とPCCP提出推奨を整理し、TPLC・透明性・性能監視を示す。 | [official source](https://www.fda.gov/medical-devices/software-medical-device-samd/artificial-intelligence-and-machine-learning-software-medical-device) |
| PMDA | PMDAがSaMDの該当性、相談、承認審査、QMS、審査ポイント、DASH施策を集約する公式情報ページ。 | [official source](https://www.pmda.go.jp/english/review-services/reviews/0009.html) |
| EU | EUのAI包括規則。医療機器AI等の高リスク分類、提供者義務、監視・透明性を定める。 | [official source](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R1689) |

## ① 対象製品/モデルの定義

**確認観点**: PCCPの対象となる製品、モデル、入力、出力、意図する使用、固定境界を明確にする。

### 記入欄

- 対象製品、モデルバージョン、構成要素を特定する。
- PCCP対象に含める変更と、承認・認証後に別途申請する変更を分ける。
- 使用者、患者集団、利用環境、モデル出力の臨床的位置づけを記録する。
- 未解決論点:
- 次回レビュー日:

### 根拠セル要約

#### ④ PCCP計画 (corpus cell G)

**セル定義**: Predetermined Change Control Plan、市販後監視、再評価、変更管理を整理する。


| ガイドライン | 要求強度 | セル要約 | 該当条項リンク |
|---|---|---|---|
| FDA | `should` | PCCPは予定変更、実装方法、影響評価を提出に含める。 | [PCCP Guidance, Section V Policy for Predetermined Change Control Plans / high](https://www.fda.gov/media/166704/download#page=14) |
| PMDA | `mention` | 再評価・再審査の臨床研究相談への言及あり。 | [PMDA Consultation on SaMD / high](https://www.pmda.go.jp/english/review-services/reviews/0009.html#consultation) |
| EU | `must` | 市販後監視を置き、重大インシデントを報告する義務。 | [Article 72(1)-(4); Article 73(1) / medium](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R1689#art-72) |

#### データ品質・バイアス (corpus cell F)

**セル定義**: 学習・評価・入力データの品質、代表性、偏り、根拠、検証可能性を整理する。


| ガイドライン | 要求強度 | セル要約 | 該当条項リンク |
|---|---|---|---|
| FDA | `should` | バイアス識別・低減と頑健性評価の方法開発を重視。 | [Action 4 Regulatory Science Methods Related to Algorithm Bias &amp; Robustness / high](https://www.fda.gov/files/medical%20devices/published/AIML-SaMD-Action-Plan.pdf#page=6) |
| PMDA | `not_assessed` | Lane Aではデータ品質・バイアス要求の評価未了。 | [未評価（Lane A） / low](https://www.pmda.go.jp/english/review-services/reviews/0009.html#contents) |
| EU | `must` | 訓練・検証・試験データの品質とバイアス対策を要求。 | [Article 10(1)-(5) / medium](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R1689#art-10) |

#### 国際整合・通知導線 (corpus cell L)

**セル定義**: GHTF、IMDRF、ISO、海外規制、国際展開、国際調和への言及を整理する。


| ガイドライン | 要求強度 | セル要約 | 該当条項リンク |
|---|---|---|---|
| FDA | `mention` | GMLP標準化やIMDRF等との国際調和を推進。 | [Action 2 Good Machine Learning Practice (GMLP) / high](https://www.fda.gov/files/medical%20devices/published/AIML-SaMD-Action-Plan.pdf#page=4) |
| PMDA | `mention` | 国際調和、DASH 2の国際展開、Science Board資料に言及。 | [Software as a Medical Device / DASH for SaMD 2 / high](https://www.pmda.go.jp/english/review-services/reviews/0009.html#dash) |
| EU | `mention` | 整合規格・共通仕様と既存EU整合法令との接続を規定。 | [Article 8(2); Article 40; Article 41 / medium](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R1689#art-40) |

### レビュー質問

- このセクションの記載は、PCCP対象変更とPCCP対象外変更を区別できるか。
- 変更後の安全性・有効性・透明性・データ品質を説明できるか。
- 変更時の利用者通知、規制当局報告、内部承認が追跡可能か。

## ② 変更計画 (modification plan)

**確認観点**: 予定される変更の種類、変更幅、頻度、発動条件、禁止変更を事前に定義する。

### 記入欄

- 性能改善、データ追加、閾値変更、対象集団拡張などの変更類型を列挙する。
- 各変更の上限、変更しない仕様、臨床ワークフローへの影響を定める。
- 変更計画が透明性、データ品質、国際整合の観点で説明可能か確認する。
- 未解決論点:
- 次回レビュー日:

### 根拠セル要約

#### ④ PCCP計画 (corpus cell G)

**セル定義**: Predetermined Change Control Plan、市販後監視、再評価、変更管理を整理する。


| ガイドライン | 要求強度 | セル要約 | 該当条項リンク |
|---|---|---|---|
| FDA | `should` | PCCPは予定変更、実装方法、影響評価を提出に含める。 | [PCCP Guidance, Section V Policy for Predetermined Change Control Plans / high](https://www.fda.gov/media/166704/download#page=14) |
| PMDA | `mention` | 再評価・再審査の臨床研究相談への言及あり。 | [PMDA Consultation on SaMD / high](https://www.pmda.go.jp/english/review-services/reviews/0009.html#consultation) |
| EU | `must` | 市販後監視を置き、重大インシデントを報告する義務。 | [Article 72(1)-(4); Article 73(1) / medium](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R1689#art-72) |

#### データ品質・バイアス (corpus cell F)

**セル定義**: 学習・評価・入力データの品質、代表性、偏り、根拠、検証可能性を整理する。


| ガイドライン | 要求強度 | セル要約 | 該当条項リンク |
|---|---|---|---|
| FDA | `should` | バイアス識別・低減と頑健性評価の方法開発を重視。 | [Action 4 Regulatory Science Methods Related to Algorithm Bias &amp; Robustness / high](https://www.fda.gov/files/medical%20devices/published/AIML-SaMD-Action-Plan.pdf#page=6) |
| PMDA | `not_assessed` | Lane Aではデータ品質・バイアス要求の評価未了。 | [未評価（Lane A） / low](https://www.pmda.go.jp/english/review-services/reviews/0009.html#contents) |
| EU | `must` | 訓練・検証・試験データの品質とバイアス対策を要求。 | [Article 10(1)-(5) / medium](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R1689#art-10) |

#### 国際整合・通知導線 (corpus cell L)

**セル定義**: GHTF、IMDRF、ISO、海外規制、国際展開、国際調和への言及を整理する。


| ガイドライン | 要求強度 | セル要約 | 該当条項リンク |
|---|---|---|---|
| FDA | `mention` | GMLP標準化やIMDRF等との国際調和を推進。 | [Action 2 Good Machine Learning Practice (GMLP) / high](https://www.fda.gov/files/medical%20devices/published/AIML-SaMD-Action-Plan.pdf#page=4) |
| PMDA | `mention` | 国際調和、DASH 2の国際展開、Science Board資料に言及。 | [Software as a Medical Device / DASH for SaMD 2 / high](https://www.pmda.go.jp/english/review-services/reviews/0009.html#dash) |
| EU | `mention` | 整合規格・共通仕様と既存EU整合法令との接続を規定。 | [Article 8(2); Article 40; Article 41 / medium](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R1689#art-40) |

### レビュー質問

- このセクションの記載は、PCCP対象変更とPCCP対象外変更を区別できるか。
- 変更後の安全性・有効性・透明性・データ品質を説明できるか。
- 変更時の利用者通知、規制当局報告、内部承認が追跡可能か。

## ③ 変更プロトコル (modification protocol)

**確認観点**: 変更を実装、検証、承認、リリースする手順と責任者を固定する。

### 記入欄

- 変更前レビュー、データ受入基準、モデル更新手順、ロールバック手順を書く。
- 変更実施時の記録、トレーサビリティ、品質システム上の承認経路を定める。
- 透明性文書、利用者通知、規制当局向け資料の更新タイミングを設定する。
- 未解決論点:
- 次回レビュー日:

### 根拠セル要約

#### ④ PCCP計画 (corpus cell G)

**セル定義**: Predetermined Change Control Plan、市販後監視、再評価、変更管理を整理する。


| ガイドライン | 要求強度 | セル要約 | 該当条項リンク |
|---|---|---|---|
| FDA | `should` | PCCPは予定変更、実装方法、影響評価を提出に含める。 | [PCCP Guidance, Section V Policy for Predetermined Change Control Plans / high](https://www.fda.gov/media/166704/download#page=14) |
| PMDA | `mention` | 再評価・再審査の臨床研究相談への言及あり。 | [PMDA Consultation on SaMD / high](https://www.pmda.go.jp/english/review-services/reviews/0009.html#consultation) |
| EU | `must` | 市販後監視を置き、重大インシデントを報告する義務。 | [Article 72(1)-(4); Article 73(1) / medium](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R1689#art-72) |

#### データ品質・バイアス (corpus cell F)

**セル定義**: 学習・評価・入力データの品質、代表性、偏り、根拠、検証可能性を整理する。


| ガイドライン | 要求強度 | セル要約 | 該当条項リンク |
|---|---|---|---|
| FDA | `should` | バイアス識別・低減と頑健性評価の方法開発を重視。 | [Action 4 Regulatory Science Methods Related to Algorithm Bias &amp; Robustness / high](https://www.fda.gov/files/medical%20devices/published/AIML-SaMD-Action-Plan.pdf#page=6) |
| PMDA | `not_assessed` | Lane Aではデータ品質・バイアス要求の評価未了。 | [未評価（Lane A） / low](https://www.pmda.go.jp/english/review-services/reviews/0009.html#contents) |
| EU | `must` | 訓練・検証・試験データの品質とバイアス対策を要求。 | [Article 10(1)-(5) / medium](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R1689#art-10) |

#### 国際整合・通知導線 (corpus cell L)

**セル定義**: GHTF、IMDRF、ISO、海外規制、国際展開、国際調和への言及を整理する。


| ガイドライン | 要求強度 | セル要約 | 該当条項リンク |
|---|---|---|---|
| FDA | `mention` | GMLP標準化やIMDRF等との国際調和を推進。 | [Action 2 Good Machine Learning Practice (GMLP) / high](https://www.fda.gov/files/medical%20devices/published/AIML-SaMD-Action-Plan.pdf#page=4) |
| PMDA | `mention` | 国際調和、DASH 2の国際展開、Science Board資料に言及。 | [Software as a Medical Device / DASH for SaMD 2 / high](https://www.pmda.go.jp/english/review-services/reviews/0009.html#dash) |
| EU | `mention` | 整合規格・共通仕様と既存EU整合法令との接続を規定。 | [Article 8(2); Article 40; Article 41 / medium](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R1689#art-40) |

### レビュー質問

- このセクションの記載は、PCCP対象変更とPCCP対象外変更を区別できるか。
- 変更後の安全性・有効性・透明性・データ品質を説明できるか。
- 変更時の利用者通知、規制当局報告、内部承認が追跡可能か。

## ④ 影響評価 (impact assessment)

**確認観点**: 予定変更が安全性、有効性、データ代表性、バイアス、利用者行動に与える影響を評価する。

### 記入欄

- 変更ごとにリスク、便益、想定外使用、患者安全への影響を評価する。
- サブグループ性能、データセットシフト、バイアス、透明性への影響を確認する。
- 国際展開、既存認証、報告義務、インシデント管理への波及を確認する。
- 未解決論点:
- 次回レビュー日:

### 根拠セル要約

#### ④ PCCP計画 (corpus cell G)

**セル定義**: Predetermined Change Control Plan、市販後監視、再評価、変更管理を整理する。


| ガイドライン | 要求強度 | セル要約 | 該当条項リンク |
|---|---|---|---|
| FDA | `should` | PCCPは予定変更、実装方法、影響評価を提出に含める。 | [PCCP Guidance, Section V Policy for Predetermined Change Control Plans / high](https://www.fda.gov/media/166704/download#page=14) |
| PMDA | `mention` | 再評価・再審査の臨床研究相談への言及あり。 | [PMDA Consultation on SaMD / high](https://www.pmda.go.jp/english/review-services/reviews/0009.html#consultation) |
| EU | `must` | 市販後監視を置き、重大インシデントを報告する義務。 | [Article 72(1)-(4); Article 73(1) / medium](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R1689#art-72) |

#### データ品質・バイアス (corpus cell F)

**セル定義**: 学習・評価・入力データの品質、代表性、偏り、根拠、検証可能性を整理する。


| ガイドライン | 要求強度 | セル要約 | 該当条項リンク |
|---|---|---|---|
| FDA | `should` | バイアス識別・低減と頑健性評価の方法開発を重視。 | [Action 4 Regulatory Science Methods Related to Algorithm Bias &amp; Robustness / high](https://www.fda.gov/files/medical%20devices/published/AIML-SaMD-Action-Plan.pdf#page=6) |
| PMDA | `not_assessed` | Lane Aではデータ品質・バイアス要求の評価未了。 | [未評価（Lane A） / low](https://www.pmda.go.jp/english/review-services/reviews/0009.html#contents) |
| EU | `must` | 訓練・検証・試験データの品質とバイアス対策を要求。 | [Article 10(1)-(5) / medium](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R1689#art-10) |

#### 国際整合・通知導線 (corpus cell L)

**セル定義**: GHTF、IMDRF、ISO、海外規制、国際展開、国際調和への言及を整理する。


| ガイドライン | 要求強度 | セル要約 | 該当条項リンク |
|---|---|---|---|
| FDA | `mention` | GMLP標準化やIMDRF等との国際調和を推進。 | [Action 2 Good Machine Learning Practice (GMLP) / high](https://www.fda.gov/files/medical%20devices/published/AIML-SaMD-Action-Plan.pdf#page=4) |
| PMDA | `mention` | 国際調和、DASH 2の国際展開、Science Board資料に言及。 | [Software as a Medical Device / DASH for SaMD 2 / high](https://www.pmda.go.jp/english/review-services/reviews/0009.html#dash) |
| EU | `mention` | 整合規格・共通仕様と既存EU整合法令との接続を規定。 | [Article 8(2); Article 40; Article 41 / medium](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R1689#art-40) |

### レビュー質問

- このセクションの記載は、PCCP対象変更とPCCP対象外変更を区別できるか。
- 変更後の安全性・有効性・透明性・データ品質を説明できるか。
- 変更時の利用者通知、規制当局報告、内部承認が追跡可能か。

## ⑤ 検証戦略 (validation strategy)

**確認観点**: 変更後モデルが意図する使用に対して十分な性能、安全性、頑健性を保つことを示す。

### 記入欄

- 評価データ、主要評価指標、受入基準、サブグループ解析を定義する。
- 変更前後比較、実世界性能監視、失敗時の停止基準を定める。
- 検証結果を利用者、規制当局、監査者が追跡できる形にする。
- 未解決論点:
- 次回レビュー日:

### 根拠セル要約

#### ④ PCCP計画 (corpus cell G)

**セル定義**: Predetermined Change Control Plan、市販後監視、再評価、変更管理を整理する。


| ガイドライン | 要求強度 | セル要約 | 該当条項リンク |
|---|---|---|---|
| FDA | `should` | PCCPは予定変更、実装方法、影響評価を提出に含める。 | [PCCP Guidance, Section V Policy for Predetermined Change Control Plans / high](https://www.fda.gov/media/166704/download#page=14) |
| PMDA | `mention` | 再評価・再審査の臨床研究相談への言及あり。 | [PMDA Consultation on SaMD / high](https://www.pmda.go.jp/english/review-services/reviews/0009.html#consultation) |
| EU | `must` | 市販後監視を置き、重大インシデントを報告する義務。 | [Article 72(1)-(4); Article 73(1) / medium](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R1689#art-72) |

#### データ品質・バイアス (corpus cell F)

**セル定義**: 学習・評価・入力データの品質、代表性、偏り、根拠、検証可能性を整理する。


| ガイドライン | 要求強度 | セル要約 | 該当条項リンク |
|---|---|---|---|
| FDA | `should` | バイアス識別・低減と頑健性評価の方法開発を重視。 | [Action 4 Regulatory Science Methods Related to Algorithm Bias &amp; Robustness / high](https://www.fda.gov/files/medical%20devices/published/AIML-SaMD-Action-Plan.pdf#page=6) |
| PMDA | `not_assessed` | Lane Aではデータ品質・バイアス要求の評価未了。 | [未評価（Lane A） / low](https://www.pmda.go.jp/english/review-services/reviews/0009.html#contents) |
| EU | `must` | 訓練・検証・試験データの品質とバイアス対策を要求。 | [Article 10(1)-(5) / medium](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R1689#art-10) |

#### 国際整合・通知導線 (corpus cell L)

**セル定義**: GHTF、IMDRF、ISO、海外規制、国際展開、国際調和への言及を整理する。


| ガイドライン | 要求強度 | セル要約 | 該当条項リンク |
|---|---|---|---|
| FDA | `mention` | GMLP標準化やIMDRF等との国際調和を推進。 | [Action 2 Good Machine Learning Practice (GMLP) / high](https://www.fda.gov/files/medical%20devices/published/AIML-SaMD-Action-Plan.pdf#page=4) |
| PMDA | `mention` | 国際調和、DASH 2の国際展開、Science Board資料に言及。 | [Software as a Medical Device / DASH for SaMD 2 / high](https://www.pmda.go.jp/english/review-services/reviews/0009.html#dash) |
| EU | `mention` | 整合規格・共通仕様と既存EU整合法令との接続を規定。 | [Article 8(2); Article 40; Article 41 / medium](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R1689#art-40) |

### レビュー質問

- このセクションの記載は、PCCP対象変更とPCCP対象外変更を区別できるか。
- 変更後の安全性・有効性・透明性・データ品質を説明できるか。
- 変更時の利用者通知、規制当局報告、内部承認が追跡可能か。

## ⑥ 報告/通知計画

**確認観点**: 変更、性能低下、重大インシデント、利用者向け更新情報の報告経路を決める。

### 記入欄

- 利用者、医療機関、規制当局、社内責任者への通知条件を定義する。
- 重大インシデント、性能逸脱、回収・停止判断のエスカレーションを定める。
- 海外制度や整合規格への影響を確認し、必要な文書更新を記録する。
- 未解決論点:
- 次回レビュー日:

### 根拠セル要約

#### ④ PCCP計画 (corpus cell G)

**セル定義**: Predetermined Change Control Plan、市販後監視、再評価、変更管理を整理する。


| ガイドライン | 要求強度 | セル要約 | 該当条項リンク |
|---|---|---|---|
| FDA | `should` | PCCPは予定変更、実装方法、影響評価を提出に含める。 | [PCCP Guidance, Section V Policy for Predetermined Change Control Plans / high](https://www.fda.gov/media/166704/download#page=14) |
| PMDA | `mention` | 再評価・再審査の臨床研究相談への言及あり。 | [PMDA Consultation on SaMD / high](https://www.pmda.go.jp/english/review-services/reviews/0009.html#consultation) |
| EU | `must` | 市販後監視を置き、重大インシデントを報告する義務。 | [Article 72(1)-(4); Article 73(1) / medium](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R1689#art-72) |

#### データ品質・バイアス (corpus cell F)

**セル定義**: 学習・評価・入力データの品質、代表性、偏り、根拠、検証可能性を整理する。


| ガイドライン | 要求強度 | セル要約 | 該当条項リンク |
|---|---|---|---|
| FDA | `should` | バイアス識別・低減と頑健性評価の方法開発を重視。 | [Action 4 Regulatory Science Methods Related to Algorithm Bias &amp; Robustness / high](https://www.fda.gov/files/medical%20devices/published/AIML-SaMD-Action-Plan.pdf#page=6) |
| PMDA | `not_assessed` | Lane Aではデータ品質・バイアス要求の評価未了。 | [未評価（Lane A） / low](https://www.pmda.go.jp/english/review-services/reviews/0009.html#contents) |
| EU | `must` | 訓練・検証・試験データの品質とバイアス対策を要求。 | [Article 10(1)-(5) / medium](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R1689#art-10) |

#### 国際整合・通知導線 (corpus cell L)

**セル定義**: GHTF、IMDRF、ISO、海外規制、国際展開、国際調和への言及を整理する。


| ガイドライン | 要求強度 | セル要約 | 該当条項リンク |
|---|---|---|---|
| FDA | `mention` | GMLP標準化やIMDRF等との国際調和を推進。 | [Action 2 Good Machine Learning Practice (GMLP) / high](https://www.fda.gov/files/medical%20devices/published/AIML-SaMD-Action-Plan.pdf#page=4) |
| PMDA | `mention` | 国際調和、DASH 2の国際展開、Science Board資料に言及。 | [Software as a Medical Device / DASH for SaMD 2 / high](https://www.pmda.go.jp/english/review-services/reviews/0009.html#dash) |
| EU | `mention` | 整合規格・共通仕様と既存EU整合法令との接続を規定。 | [Article 8(2); Article 40; Article 41 / medium](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R1689#art-40) |

### レビュー質問

- このセクションの記載は、PCCP対象変更とPCCP対象外変更を区別できるか。
- 変更後の安全性・有効性・透明性・データ品質を説明できるか。
- 変更時の利用者通知、規制当局報告、内部承認が追跡可能か。

---

## Footnotes

[^cc-by]: 本資料のオリジナル編集物 (構成、要約、表) は CC-BY 4.0。第三者ガイドライン原文の権利は各権利者に帰属し、CC-BY の対象外。

**Disclaimer**: 本資料は公開ガイドラインの参照用コンパイルであり、法的助言、規制適合性の保証、診療判断ではありません。最終判断は必ず PMDA/FDA/EU 等の原文および適用される法令・通知を参照してください。
