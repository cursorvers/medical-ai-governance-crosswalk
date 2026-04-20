# 医療AI研究 IRB質問票テンプレート

> **目的**: 医療AI研究の倫理審査で、該当性、リスク、透明性、バイアス、プライバシー、同意、モニタリングを質問票として整理する。
> **対象**: 医療AIを用いる臨床研究、観察研究、二次利用研究、生成AI利用研究、研究支援AIの導入審査。

## ① 研究概要

| 項目 | 記入欄 |
|---|---|
| 研究課題名 |  |
| 研究責任者 / 所属 |  |
| AIシステム / モデル名 |  |
| AIの役割 |  |
| 対象データ |  |
| 対象者 / 患者集団 |  |
| 研究デザイン |  |
| 主要評価項目 |  |
| 外部提供 / 委託 / クラウド利用 |  |
| IRBで判断してほしい論点 |  |

### 参照ガイドライン

| ガイドライン | 要約 | 原文 |
|---|---|---|
| WHO AIH | WHOの医療AI倫理・ガバナンス指針。2021年版の6原則に加え、LMM向け勧告を参照する。 | [official source](https://www.who.int/publications/i/item/9789240029200) |
| NIST AI RMF | NISTの任意AIリスク管理枠組み。Govern/Map/Measure/Manageと生成AIプロファイルを示す。 | [official source](https://www.nist.gov/itl/ai-risk-management-framework) |
| JMSF | 日本医師会のAI臨床利用に関する答申。医師主導、人間中心、情報管理、責任、生命倫理上の課題を整理する。 | [official source](https://www.med.or.jp/dl-med/teireikaiken/20260415_3.pdf) |

## ② 該当性 (cell A)

**確認観点**: 研究が医療AI、医療機器、生成AI、臨床利用、二次利用のどれに該当するかを確認する。

### IRB質問

- 研究対象AIの用途は診療、研究支援、患者向け説明、事務支援のどれか。
- AI出力は医師または研究者の判断を代替、補助、生成するか。
- 既存研究、品質改善、医療機器評価、臨床研究の境界は明確か。
- 研究計画書の該当箇所:
- 追加で求める資料:
- 判定メモ:

### 根拠セル要約

#### ② 該当性判定 (corpus cell A)

**セル定義**: 対象となる製品、ソフトウェア、利用場面、開発段階、除外範囲を整理する。


| ガイドライン | 要求強度 | セル要約 | 原文リンク |
|---|---|---|---|
| WHO AIH | `mention` | 医療AI全般とLMMの医療・公衆衛生利用を対象にする。 | [Overview; 2021 guidance / high](https://iris.who.int/server/api/core/bitstreams/f780d926-4ae3-42ce-a6d6-e898a5562621/content#page=13) |
| NIST AI RMF | `should` | AIの設計・開発・利用・評価で信頼性リスク管理を促す。 | [Overview of the AI RMF / high](https://www.nist.gov/itl/ai-risk-management-framework#main-content) |
| JMSF | `mention` | 医療AIの臨床利用全般と医師・患者・AIの関係を対象にする。 | [第1章 総論：医療AIの現状と課題 / medium](https://www.med.or.jp/dl-med/teireikaiken/20260415_3.pdf#page=1) |

## ③ リスク評価 (cell B)

**確認観点**: 患者、研究参加者、医療者、研究組織に生じるリスクと便益を文脈別に確認する。

### IRB質問

- 誤出力、過信、自動化バイアス、診療遅延、心理的影響を評価したか。
- 高リスク集団や脆弱な参加者に固有のリスクを分けているか。
- 残余リスクを誰が受容し、どの条件で研究を停止するか。
- 研究計画書の該当箇所:
- 追加で求める資料:
- 判定メモ:

### 根拠セル要約

#### ③ リスク分類 (corpus cell B)

**セル定義**: 医療機器クラス、AIリスク分類、患者安全への影響度などの分類方法を整理する。


| ガイドライン | 要求強度 | セル要約 | 原文リンク |
|---|---|---|---|
| WHO AIH | `mention` | LMMではリスクベース枠組みと規制負荷差に言及。 | [Section 5, Assessment of general-purpose foundation models and/or applications used in health care / high](https://iris.who.int/server/api/core/bitstreams/e9e62c65-6045-481e-bd04-20e206bc5039/content#page=65) |
| NIST AI RMF | `should` | 文脈に応じてリスク許容度、優先度、影響を評価する。 | [Section 3; MAP 4-5; MANAGE 1 / high](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf#page=32) |
| JMSF | `mention` | 臨床利用を3類型に分け、悪用や制度的リスクも整理する。 | [第3章 3.3.1 AIの臨床利用の3類型 / medium](https://www.med.or.jp/dl-med/teireikaiken/20260415_3.pdf#page=68) |

## ④ 透明性/説明責任 (cell C, F)

**確認観点**: AI使用の説明、出力根拠、限界、データ品質、説明責任の所在を確認する。

### IRB質問

- 参加者、患者、医療者にAI利用の事実と限界をどう説明するか。
- モデルの入力、出力、性能、既知の限界、データ代表性を文書化したか。
- 説明不能な出力や不一致が出た場合の責任者と対応手順は明確か。
- 研究計画書の該当箇所:
- 追加で求める資料:
- 判定メモ:

### 根拠セル要約

#### 透明性・説明責任 (corpus cell C)

**セル定義**: 利用者、医療者、患者、規制当局への説明、表示、根拠提示、情報開示を整理する。


| ガイドライン | 要求強度 | セル要約 | 原文リンク |
|---|---|---|---|
| WHO AIH | `should` | 透明性・説明可能性・理解可能性を中核原則に置く。 | [Executive summary; Section 5 / high](https://iris.who.int/server/api/core/bitstreams/f780d926-4ae3-42ce-a6d6-e898a5562621/content#page=42) |
| NIST AI RMF | `should` | 透明性、説明可能性、解釈可能性を信頼性特性に含める。 | [Section 4; MEASURE 2.8 / high](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf#page=35) |
| JMSF | `should` | AI使用の患者通知、透明性措置、医師確認を重視する。 | [第3章 3.3.2 記録・文書作成の補助 / medium](https://www.med.or.jp/dl-med/teireikaiken/20260415_3.pdf#page=69) |

#### データ品質・バイアス (corpus cell F)

**セル定義**: 学習・評価・入力データの品質、代表性、偏り、根拠、検証可能性を整理する。


| ガイドライン | 要求強度 | セル要約 | 原文リンク |
|---|---|---|---|
| WHO AIH | `should` | 低品質・非代表データとバイアスの最小化を重視する。 | [Executive summary; inclusiveness and equity / high](https://iris.who.int/server/api/core/bitstreams/f780d926-4ae3-42ce-a6d6-e898a5562621/content#page=44) |
| NIST AI RMF | `should` | 公平性、有害バイアス、データ代表性を測定・管理する。 | [Section 4; MEASURE 2.11 / high](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf#page=23) |
| JMSF | `should` | バイアス、データセットシフト、精度劣化への注意を求める。 | [第3章 3.3.3 診断・治療の補助 / medium](https://www.med.or.jp/dl-med/teireikaiken/20260415_3.pdf#page=71) |

## ⑤ バイアス/公平性 (cell D, 補助参照 cell F)

**確認観点**: 記録・監査可能性とデータ品質の両面から、偏りの発見、説明、是正可能性を確認する。

### IRB質問

- 年齢、性別、疾患、施設、言語、社会経済属性ごとの性能差を確認したか。
- バイアスを発見した場合の記録、原因分析、是正、再審査手順はあるか。
- 研究対象集団が学習・評価データと異なる場合の説明は十分か。
- 研究計画書の該当箇所:
- 追加で求める資料:
- 判定メモ:

### 根拠セル要約

#### 監査ログ・記録 (corpus cell D)

**セル定義**: 判断過程、利用履歴、変更履歴、アクセス履歴などの記録と監査可能性を整理する。


| ガイドライン | 要求強度 | セル要約 | 原文リンク |
|---|---|---|---|
| WHO AIH | `should` | LMMでは第三者監査、影響評価、公開を求める。 | [Sections 4.2, 5.2, 6.4 / high](https://iris.who.int/server/api/core/bitstreams/e9e62c65-6045-481e-bd04-20e206bc5039/content#page=18) |
| NIST AI RMF | `should` | 文書化、インベントリ、来歴、監視結果の記録を求める。 | [GOVERN 1.5-1.6; MEASURE 2.8 / high](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf#page=20) |
| JMSF | `mention` | エラー報告、データ保存、AIモニタリングの必要性に触れる。 | [第3章 3.3.2; 第2章 2.8.7 / low](https://www.med.or.jp/dl-med/teireikaiken/20260415_3.pdf#page=69) |

#### データ品質・バイアス (corpus cell F)

**セル定義**: 学習・評価・入力データの品質、代表性、偏り、根拠、検証可能性を整理する。


| ガイドライン | 要求強度 | セル要約 | 原文リンク |
|---|---|---|---|
| WHO AIH | `should` | 低品質・非代表データとバイアスの最小化を重視する。 | [Executive summary; inclusiveness and equity / high](https://iris.who.int/server/api/core/bitstreams/f780d926-4ae3-42ce-a6d6-e898a5562621/content#page=44) |
| NIST AI RMF | `should` | 公平性、有害バイアス、データ代表性を測定・管理する。 | [Section 4; MEASURE 2.11 / high](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf#page=23) |
| JMSF | `should` | バイアス、データセットシフト、精度劣化への注意を求める。 | [第3章 3.3.3 診断・治療の補助 / medium](https://www.med.or.jp/dl-med/teireikaiken/20260415_3.pdf#page=71) |

## ⑥ プライバシー/データ保護 (cell H, 補助参照 cell I)

**確認観点**: 責任主体、データ管理責任、同意・機密性・個人情報保護の実装を確認する。

### IRB質問

- データ管理者、解析者、モデル提供者、研究責任者の責任分担は明確か。
- 個人情報、要配慮情報、診療情報、二次利用データの取扱いは法令・倫理指針に沿うか。
- 外部モデル、クラウド、委託先にデータが渡る場合の契約と保護措置はあるか。
- 研究計画書の該当箇所:
- 追加で求める資料:
- 判定メモ:

### 根拠セル要約

#### 責任主体・説明責任 (corpus cell H)

**セル定義**: 開発者、製造販売業者、医療者、使用者、規制当局などの責任範囲を整理する。


| ガイドライン | 要求強度 | セル要約 | 原文リンク |
|---|---|---|---|
| WHO AIH | `should` | 責任と説明責任、被害救済、価値連鎖上の責任を求める。 | [Executive summary; responsibility and accountability / high](https://iris.who.int/server/api/core/bitstreams/f780d926-4ae3-42ce-a6d6-e898a5562621/content#page=44) |
| NIST AI RMF | `should` | 役割、責任、説明責任メカニズムを組織に求める。 | [GOVERN 2.1-2.3; Section 3.4 / high](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf#page=28) |
| JMSF | `should` | 医師、開発者、行政を含む責任分担の必要性を示す。 | [第3章 3.3.3 診断・治療の補助 / medium](https://www.med.or.jp/dl-med/teireikaiken/20260415_3.pdf#page=72) |

#### 同意・プライバシー (corpus cell I)

**セル定義**: 患者・利用者データの同意、プライバシー、個人情報、共有、二次利用を整理する。


| ガイドライン | 要求強度 | セル要約 | 原文リンク |
|---|---|---|---|
| WHO AIH | `should` | プライバシー、機密性、有効な同意、データ保護を要求する。 | [Executive summary; Protecting human autonomy / high](https://iris.who.int/server/api/core/bitstreams/f780d926-4ae3-42ce-a6d6-e898a5562621/content#page=41) |
| NIST AI RMF | `should` | プライバシー強化と同意等の生成AIプライバシーリスクを扱う。 | [GAI Risks: Data Privacy; MEASURE 2.10 / high](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf#page=24) |
| JMSF | `should` | 機微な診療情報の機密性、不正アクセス防止、同意を重視する。 | [第3章 3.1.2 WMAが示す医師参加型原則 / medium](https://www.med.or.jp/dl-med/teireikaiken/20260415_3.pdf#page=54) |

## ⑦ インフォームドコンセント (cell I)

**確認観点**: 参加者に対してAI利用、データ利用、リスク、撤回、二次利用を理解可能に説明する。

### IRB質問

- 説明文書はAIの役割、限界、データ利用範囲、第三者提供を明示しているか。
- 同意免除またはオプトアウトの場合、理由と代替保護措置は妥当か。
- 同意撤回後のデータ、学習済みモデル、派生データの扱いを説明しているか。
- 研究計画書の該当箇所:
- 追加で求める資料:
- 判定メモ:

### 根拠セル要約

#### 同意・プライバシー (corpus cell I)

**セル定義**: 患者・利用者データの同意、プライバシー、個人情報、共有、二次利用を整理する。


| ガイドライン | 要求強度 | セル要約 | 原文リンク |
|---|---|---|---|
| WHO AIH | `should` | プライバシー、機密性、有効な同意、データ保護を要求する。 | [Executive summary; Protecting human autonomy / high](https://iris.who.int/server/api/core/bitstreams/f780d926-4ae3-42ce-a6d6-e898a5562621/content#page=41) |
| NIST AI RMF | `should` | プライバシー強化と同意等の生成AIプライバシーリスクを扱う。 | [GAI Risks: Data Privacy; MEASURE 2.10 / high](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf#page=24) |
| JMSF | `should` | 機微な診療情報の機密性、不正アクセス防止、同意を重視する。 | [第3章 3.1.2 WMAが示す医師参加型原則 / medium](https://www.med.or.jp/dl-med/teireikaiken/20260415_3.pdf#page=54) |

## ⑧ モニタリング/有害事象 (cell L)

**確認観点**: 研究中および研究後の監視、逸脱、インシデント、有害事象、外部報告の導線を確認する。

### IRB質問

- AI出力による有害事象、ニアミス、予期せぬ性能低下をどう検知するか。
- IRB、研究機関、規制当局、共同研究先への報告基準と期限は明確か。
- 海外ガイダンスや国際倫理との整合を継続的に見直す仕組みはあるか。
- 研究計画書の該当箇所:
- 追加で求める資料:
- 判定メモ:

### 根拠セル要約

#### 国際整合・通知導線 (corpus cell L)

**セル定義**: GHTF、IMDRF、ISO、海外規制、国際展開、国際調和への言及を整理する。


| ガイドライン | 要求強度 | セル要約 | 原文リンク |
|---|---|---|---|
| WHO AIH | `should` | LMMと医療AIの国際的な協調ガバナンスを求める。 | [Section 8; International governance of LMMs / high](https://iris.who.int/server/api/core/bitstreams/e9e62c65-6045-481e-bd04-20e206bc5039/content#page=78) |
| NIST AI RMF | `mention` | 他のリスク管理努力との整合と国際的利用を意図する。 | [Overview of the AI RMF; AIRC / high](https://www.nist.gov/itl/ai-risk-management-framework#main-content) |
| JMSF | `mention` | WMA声明、日本AI法、国際倫理と国内戦略の整合を整理する。 | [第3章 3.1 医療AIを巡る国際倫理と日本の戦略 / medium](https://www.med.or.jp/dl-med/teireikaiken/20260415_3.pdf#page=53) |

---

## IRB判定メモ

| 判定項目 | メモ |
|---|---|
| 承認 / 条件付き承認 / 継続審査 / 不承認 |  |
| 主な条件 |  |
| 同意説明文書の修正 |  |
| モニタリング条件 |  |
| 報告義務 |  |
| 次回確認日 |  |

## Footnotes

[^cc-by]: 本資料のオリジナル編集物 (構成、要約、表) は CC-BY 4.0。第三者ガイドライン原文の権利は各権利者に帰属し、CC-BY の対象外。

**Disclaimer**: 本資料は公開ガイドラインの参照用コンパイルであり、法的助言、規制適合性の保証、診療判断、倫理審査結果の保証ではありません。最終判断は必ず所属機関の倫理指針、IRB手順書、WHO/NIST/JMSF等の原文および適用法令を参照してください。
