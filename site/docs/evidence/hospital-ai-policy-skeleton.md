# 病院AI導入ポリシー骨子

> **目的**: 医療機関がAI導入時の審査、継続モニタリング、有害事象報告、教育、変更管理を院内規程として整理する。
> **対象**: 病院医療安全室、情報システム部門、倫理委員会事務局、診療部門責任者、AI導入審査会議体。

## いつ使う？

**シーン 4: 病院AI導入ポリシーの策定** — 病院長 / 経営会議から「当院のAI導入ガバナンス方針」の策定を指示されたとき、サイト hero chips「責任主体」「監査ログ」「セキュリティ」で各ガイドライン要件を横断確認し、自院仕様にカスタマイズして経営層提出版に仕上げます。詳しい流れは [使い方シナリオ #4](../usage.md#4-ai) を参照。

## ポリシー基本情報

| 項目 | 記入欄 |
|---|---|
| 文書名 / 版 |  |
| 所管部署 |  |
| 承認会議体 |  |
| 適用開始日 |  |
| 対象AIシステム |  |
| 対象部署 |  |
| 関連規程 |  |
| 次回見直し日 |  |

## 参照ガイドライン

| ガイドライン | 要約 | 原文 |
|---|---|---|
| NIST AI RMF | NISTの任意AIリスク管理枠組み。Govern/Map/Measure/Manageと生成AIプロファイルを示す。 | [official source](https://www.nist.gov/itl/ai-risk-management-framework) |
| ISO/IEC 42001 | AIマネジメントシステムの国際標準。本文未取得のため詳細要求は低信頼で限定評価。 | [official source](https://www.iso.org/standard/81230.html) |
| JMSF/JMA | 日本医師会のAI臨床利用に関する答申。医師主導、人間中心、情報管理、責任、生命倫理上の課題を整理する。 | [official source](https://www.med.or.jp/dl-med/teireikaiken/20260415_3.pdf) |

## ① 適用範囲

**確認観点**: 院内で審査対象とするAI利用を、診療、研究、教育、事務、患者向け利用に分ける。

### ポリシー記載案

- 診療判断に影響するAI、文書作成AI、患者向けAI、研究AI、業務支援AIを分類する。
- 院内承認が必要な利用、部門判断で足りる利用、禁止する利用を定める。
- 外部クラウド、生成AI、医療機器、研究用ツールの扱いを分ける。

### 院内実装メモ

- 所管部署:
- 必要な会議体:
- 必要な記録:
- 未決事項:

### 根拠セル要約

#### ② 該当性判定 (corpus cell A)

**セル定義**: 対象となる製品、ソフトウェア、利用場面、開発段階、除外範囲を整理する。


| ガイドライン | 要求強度 | セル要約 | 原文リンク |
|---|---|---|---|
| NIST AI RMF | `should` | AIの設計・開発・利用・評価で信頼性リスク管理を促す。 | [Overview of the AI RMF / high](https://www.nist.gov/itl/ai-risk-management-framework#main-content) |
| ISO/IEC 42001 | `should` | AI製品・サービスの開発、提供、利用組織を対象にする。 | [ISO public page: What is ISO/IEC 42001? / low](https://www.iso.org/standard/81230.html) |
| JMSF/JMA | `mention` | 医療AIの臨床利用全般と医師・患者・AIの関係を対象にする。 | [第1章 総論：医療AIの現状と課題 / medium](https://www.med.or.jp/dl-med/teireikaiken/20260415_3.pdf#page=1) |

## ② 導入審査プロセス (cell A, B)

**確認観点**: 導入前に、適用対象、リスク、責任、データ保護、患者説明を審査する流れを定める。

### ポリシー記載案

- 申請者、審査会議体、必要資料、承認条件、再審査条件を定める。
- 患者安全、個人情報、医師の監督、ベンダー契約、研究該当性を確認する。
- 高リスク利用は医療安全、情報システム、倫理、法務、診療部門で共同審査する。

### 院内実装メモ

- 所管部署:
- 必要な会議体:
- 必要な記録:
- 未決事項:

### 根拠セル要約

#### ② 該当性判定 (corpus cell A)

**セル定義**: 対象となる製品、ソフトウェア、利用場面、開発段階、除外範囲を整理する。


| ガイドライン | 要求強度 | セル要約 | 原文リンク |
|---|---|---|---|
| NIST AI RMF | `should` | AIの設計・開発・利用・評価で信頼性リスク管理を促す。 | [Overview of the AI RMF / high](https://www.nist.gov/itl/ai-risk-management-framework#main-content) |
| ISO/IEC 42001 | `should` | AI製品・サービスの開発、提供、利用組織を対象にする。 | [ISO public page: What is ISO/IEC 42001? / low](https://www.iso.org/standard/81230.html) |
| JMSF/JMA | `mention` | 医療AIの臨床利用全般と医師・患者・AIの関係を対象にする。 | [第1章 総論：医療AIの現状と課題 / medium](https://www.med.or.jp/dl-med/teireikaiken/20260415_3.pdf#page=1) |

#### ③ リスク分類 (corpus cell B)

**セル定義**: 医療機器クラス、AIリスク分類、患者安全への影響度などの分類方法を整理する。


| ガイドライン | 要求強度 | セル要約 | 原文リンク |
|---|---|---|---|
| NIST AI RMF | `should` | 文脈に応じてリスク許容度、優先度、影響を評価する。 | [Section 3; MAP 4-5; MANAGE 1 / high](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf#page=32) |
| ISO/IEC 42001 | `mention` | AI関連リスクと機会を管理する枠組みとして説明される。 | [ISO public page: Benefits / low](https://www.iso.org/standard/81230.html) |
| JMSF/JMA | `mention` | 臨床利用を3類型に分け、悪用や制度的リスクも整理する。 | [第3章 3.3.1 AIの臨床利用の3類型 / medium](https://www.med.or.jp/dl-med/teireikaiken/20260415_3.pdf#page=68) |

#### 責任主体・説明責任 (corpus cell H)

**セル定義**: 開発者、製造販売業者、医療者、使用者、規制当局などの責任範囲を整理する。


| ガイドライン | 要求強度 | セル要約 | 原文リンク |
|---|---|---|---|
| NIST AI RMF | `should` | 役割、責任、説明責任メカニズムを組織に求める。 | [GOVERN 2.1-2.3; Section 3.4 / high](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf#page=28) |
| ISO/IEC 42001 | `mention` | 方針、目的、プロセスによる責任あるAI管理を扱う。 | [ISO public page: FAQ; AIMS definition / low](https://www.iso.org/standard/81230.html) |
| JMSF/JMA | `should` | 医師、開発者、行政を含む責任分担の必要性を示す。 | [第3章 3.3.3 診断・治療の補助 / medium](https://www.med.or.jp/dl-med/teireikaiken/20260415_3.pdf#page=72) |

#### 同意・プライバシー (corpus cell I)

**セル定義**: 患者・利用者データの同意、プライバシー、個人情報、共有、二次利用を整理する。


| ガイドライン | 要求強度 | セル要約 | 原文リンク |
|---|---|---|---|
| NIST AI RMF | `should` | プライバシー強化と同意等の生成AIプライバシーリスクを扱う。 | [GAI Risks: Data Privacy; MEASURE 2.10 / high](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf#page=24) |
| ISO/IEC 42001 | `not_assessed` | 同意・プライバシー要求は本文未取得で評価未了。 | [not assessed; standard text unavailable / low](https://www.iso.org/standard/81230.html) |
| JMSF/JMA | `should` | 機微な診療情報の機密性、不正アクセス防止、同意を重視する。 | [第3章 3.1.2 WMAが示す医師参加型原則 / medium](https://www.med.or.jp/dl-med/teireikaiken/20260415_3.pdf#page=54) |

## ③ 継続モニタリング (cell L)

**確認観点**: 導入後の性能、利用状況、苦情、インシデント、国際基準との整合を継続確認する。

### ポリシー記載案

- 監視指標、レビュー頻度、責任部署、報告先を定める。
- 性能低下、対象外利用、患者影響、ベンダー更新を検知する手順を書く。
- 国際基準や専門職答申の更新時に院内ルールを見直す。

### 院内実装メモ

- 所管部署:
- 必要な会議体:
- 必要な記録:
- 未決事項:

### 根拠セル要約

#### 国際整合・通知導線 (corpus cell L)

**セル定義**: GHTF、IMDRF、ISO、海外規制、国際展開、国際調和への言及を整理する。


| ガイドライン | 要求強度 | セル要約 | 原文リンク |
|---|---|---|---|
| NIST AI RMF | `mention` | 他のリスク管理努力との整合と国際的利用を意図する。 | [Overview of the AI RMF; AIRC / high](https://www.nist.gov/itl/ai-risk-management-framework#main-content) |
| ISO/IEC 42001 | `mention` | AI管理システムの国際標準として位置づけられる。 | [ISO public page: General information / low](https://www.iso.org/standard/81230.html) |
| JMSF/JMA | `mention` | WMA声明、日本AI法、国際倫理と国内戦略の整合を整理する。 | [第3章 3.1 医療AIを巡る国際倫理と日本の戦略 / medium](https://www.med.or.jp/dl-med/teireikaiken/20260415_3.pdf#page=53) |

#### ⑥ ライフサイクル管理 (corpus cell M)

**セル定義**: 開発、申請、導入、教育、変更、更新、廃止までの継続管理を整理する。


| ガイドライン | 要求強度 | セル要約 | 原文リンク |
|---|---|---|---|
| NIST AI RMF | `should` | Govern/Map/Measure/ManageをAIライフサイクル全体に適用する。 | [Section 5; Tables 1-4 / high](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf#page=26) |
| ISO/IEC 42001 | `should` | AIMSの確立、実施、維持、継続的改善を要求する。 | [ISO public page: What is ISO/IEC 42001? / low](https://www.iso.org/standard/81230.html) |
| JMSF/JMA | `mention` | 医師会の継続的関与と新たなガバナンス体制を求める。 | [第3章 3.1.4 まとめ; 第2章 2.8.7 / medium](https://www.med.or.jp/dl-med/teireikaiken/20260415_3.pdf#page=56) |

#### 監査ログ・記録 (corpus cell D)

**セル定義**: 判断過程、利用履歴、変更履歴、アクセス履歴などの記録と監査可能性を整理する。


| ガイドライン | 要求強度 | セル要約 | 原文リンク |
|---|---|---|---|
| NIST AI RMF | `should` | 文書化、インベントリ、来歴、監視結果の記録を求める。 | [GOVERN 1.5-1.6; MEASURE 2.8 / high](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf#page=20) |
| ISO/IEC 42001 | `not_assessed` | 監査ログ・記録要求は本文未取得で評価未了。 | [not assessed; standard text unavailable / low](https://www.iso.org/standard/81230.html) |
| JMSF/JMA | `mention` | エラー報告、データ保存、AIモニタリングの必要性に触れる。 | [第3章 3.3.2; 第2章 2.8.7 / low](https://www.med.or.jp/dl-med/teireikaiken/20260415_3.pdf#page=69) |

## ④ 有害事象報告

**確認観点**: AI利用に関連する有害事象、ニアミス、説明誤り、情報漏えいの報告経路を定める。

### ポリシー記載案

- 報告対象、期限、一次対応、患者説明、ベンダー連絡、再発防止を定義する。
- AI出力、医師判断、最終対応、ログ、証跡を保存する。
- 医療安全報告、情報セキュリティ報告、倫理審査報告の分岐を決める。

### 院内実装メモ

- 所管部署:
- 必要な会議体:
- 必要な記録:
- 未決事項:

### 根拠セル要約

#### 監査ログ・記録 (corpus cell D)

**セル定義**: 判断過程、利用履歴、変更履歴、アクセス履歴などの記録と監査可能性を整理する。


| ガイドライン | 要求強度 | セル要約 | 原文リンク |
|---|---|---|---|
| NIST AI RMF | `should` | 文書化、インベントリ、来歴、監視結果の記録を求める。 | [GOVERN 1.5-1.6; MEASURE 2.8 / high](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf#page=20) |
| ISO/IEC 42001 | `not_assessed` | 監査ログ・記録要求は本文未取得で評価未了。 | [not assessed; standard text unavailable / low](https://www.iso.org/standard/81230.html) |
| JMSF/JMA | `mention` | エラー報告、データ保存、AIモニタリングの必要性に触れる。 | [第3章 3.3.2; 第2章 2.8.7 / low](https://www.med.or.jp/dl-med/teireikaiken/20260415_3.pdf#page=69) |

#### ③ リスク分類 (corpus cell B)

**セル定義**: 医療機器クラス、AIリスク分類、患者安全への影響度などの分類方法を整理する。


| ガイドライン | 要求強度 | セル要約 | 原文リンク |
|---|---|---|---|
| NIST AI RMF | `should` | 文脈に応じてリスク許容度、優先度、影響を評価する。 | [Section 3; MAP 4-5; MANAGE 1 / high](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf#page=32) |
| ISO/IEC 42001 | `mention` | AI関連リスクと機会を管理する枠組みとして説明される。 | [ISO public page: Benefits / low](https://www.iso.org/standard/81230.html) |
| JMSF/JMA | `mention` | 臨床利用を3類型に分け、悪用や制度的リスクも整理する。 | [第3章 3.3.1 AIの臨床利用の3類型 / medium](https://www.med.or.jp/dl-med/teireikaiken/20260415_3.pdf#page=68) |

#### 責任主体・説明責任 (corpus cell H)

**セル定義**: 開発者、製造販売業者、医療者、使用者、規制当局などの責任範囲を整理する。


| ガイドライン | 要求強度 | セル要約 | 原文リンク |
|---|---|---|---|
| NIST AI RMF | `should` | 役割、責任、説明責任メカニズムを組織に求める。 | [GOVERN 2.1-2.3; Section 3.4 / high](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf#page=28) |
| ISO/IEC 42001 | `mention` | 方針、目的、プロセスによる責任あるAI管理を扱う。 | [ISO public page: FAQ; AIMS definition / low](https://www.iso.org/standard/81230.html) |
| JMSF/JMA | `should` | 医師、開発者、行政を含む責任分担の必要性を示す。 | [第3章 3.3.3 診断・治療の補助 / medium](https://www.med.or.jp/dl-med/teireikaiken/20260415_3.pdf#page=72) |

## ⑤ 教育・トレーニング (cell M)

**確認観点**: 利用者がAIの限界、過信リスク、説明責任、データ保護を理解する教育を定める。

### ポリシー記載案

- 初回利用前、定期更新時、重大変更時に必要な教育内容を定める。
- AI出力の確認方法、患者説明、拒否対応、インシデント報告を訓練する。
- 職種別に医師、看護師、事務、研究者、情報システム担当の教育範囲を分ける。

### 院内実装メモ

- 所管部署:
- 必要な会議体:
- 必要な記録:
- 未決事項:

### 根拠セル要約

#### ⑥ ライフサイクル管理 (corpus cell M)

**セル定義**: 開発、申請、導入、教育、変更、更新、廃止までの継続管理を整理する。


| ガイドライン | 要求強度 | セル要約 | 原文リンク |
|---|---|---|---|
| NIST AI RMF | `should` | Govern/Map/Measure/ManageをAIライフサイクル全体に適用する。 | [Section 5; Tables 1-4 / high](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf#page=26) |
| ISO/IEC 42001 | `should` | AIMSの確立、実施、維持、継続的改善を要求する。 | [ISO public page: What is ISO/IEC 42001? / low](https://www.iso.org/standard/81230.html) |
| JMSF/JMA | `mention` | 医師会の継続的関与と新たなガバナンス体制を求める。 | [第3章 3.1.4 まとめ; 第2章 2.8.7 / medium](https://www.med.or.jp/dl-med/teireikaiken/20260415_3.pdf#page=56) |

#### 透明性・説明責任 (corpus cell C)

**セル定義**: 利用者、医療者、患者、規制当局への説明、表示、根拠提示、情報開示を整理する。


| ガイドライン | 要求強度 | セル要約 | 原文リンク |
|---|---|---|---|
| NIST AI RMF | `should` | 透明性、説明可能性、解釈可能性を信頼性特性に含める。 | [Section 4; MEASURE 2.8 / high](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf#page=35) |
| ISO/IEC 42001 | `mention` | 透明性、トレーサビリティ、信頼性を利点として掲げる。 | [ISO public page: Benefits / low](https://www.iso.org/standard/81230.html) |
| JMSF/JMA | `should` | AI使用の患者通知、透明性措置、医師確認を重視する。 | [第3章 3.3.2 記録・文書作成の補助 / medium](https://www.med.or.jp/dl-med/teireikaiken/20260415_3.pdf#page=69) |

#### データ品質・バイアス (corpus cell F)

**セル定義**: 学習・評価・入力データの品質、代表性、偏り、根拠、検証可能性を整理する。


| ガイドライン | 要求強度 | セル要約 | 原文リンク |
|---|---|---|---|
| NIST AI RMF | `should` | 公平性、有害バイアス、データ代表性を測定・管理する。 | [Section 4; MEASURE 2.11 / high](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf#page=23) |
| ISO/IEC 42001 | `not_assessed` | データ品質・バイアス要求は本文未取得で評価未了。 | [not assessed; standard text unavailable / low](https://www.iso.org/standard/81230.html) |
| JMSF/JMA | `should` | バイアス、データセットシフト、精度劣化への注意を求める。 | [第3章 3.3.3 診断・治療の補助 / medium](https://www.med.or.jp/dl-med/teireikaiken/20260415_3.pdf#page=71) |

#### 同意・プライバシー (corpus cell I)

**セル定義**: 患者・利用者データの同意、プライバシー、個人情報、共有、二次利用を整理する。


| ガイドライン | 要求強度 | セル要約 | 原文リンク |
|---|---|---|---|
| NIST AI RMF | `should` | プライバシー強化と同意等の生成AIプライバシーリスクを扱う。 | [GAI Risks: Data Privacy; MEASURE 2.10 / high](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf#page=24) |
| ISO/IEC 42001 | `not_assessed` | 同意・プライバシー要求は本文未取得で評価未了。 | [not assessed; standard text unavailable / low](https://www.iso.org/standard/81230.html) |
| JMSF/JMA | `should` | 機微な診療情報の機密性、不正アクセス防止、同意を重視する。 | [第3章 3.1.2 WMAが示す医師参加型原則 / medium](https://www.med.or.jp/dl-med/teireikaiken/20260415_3.pdf#page=54) |

## ⑥ 変更管理 (cell G)

**確認観点**: モデル更新、閾値変更、対象拡大、ベンダー仕様変更を院内で再評価する。

### ポリシー記載案

- 変更通知を受ける窓口、影響評価、再承認、利用者通知、患者説明更新を定める。
- 性能、対象患者、利用環境、データ処理が変わる場合の停止・再開基準を書く。
- 変更履歴、承認履歴、検証結果、教育実施を監査可能に保存する。

### 院内実装メモ

- 所管部署:
- 必要な会議体:
- 必要な記録:
- 未決事項:

### 根拠セル要約

#### ④ PCCP計画 (corpus cell G)

**セル定義**: Predetermined Change Control Plan、市販後監視、再評価、変更管理を整理する。


| ガイドライン | 要求強度 | セル要約 | 原文リンク |
|---|---|---|---|
| NIST AI RMF | `should` | 展開後監視、改善、事故・エラー連絡を管理機能に含める。 | [MANAGE 4.1-4.3 / high](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf#page=38) |
| ISO/IEC 42001 | `not_assessed` | PCCP・市販後管理相当の条項は評価未了。 | [not assessed; standard text unavailable / low](https://www.iso.org/standard/81230.html) |
| JMSF/JMA | `mention` | 展開後の能力維持やAIによるAI監視を課題に挙げる。 | [第2章 2.8.7 さいごに / low](https://www.med.or.jp/dl-med/teireikaiken/20260415_3.pdf#page=51) |

#### ⑥ ライフサイクル管理 (corpus cell M)

**セル定義**: 開発、申請、導入、教育、変更、更新、廃止までの継続管理を整理する。


| ガイドライン | 要求強度 | セル要約 | 原文リンク |
|---|---|---|---|
| NIST AI RMF | `should` | Govern/Map/Measure/ManageをAIライフサイクル全体に適用する。 | [Section 5; Tables 1-4 / high](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf#page=26) |
| ISO/IEC 42001 | `should` | AIMSの確立、実施、維持、継続的改善を要求する。 | [ISO public page: What is ISO/IEC 42001? / low](https://www.iso.org/standard/81230.html) |
| JMSF/JMA | `mention` | 医師会の継続的関与と新たなガバナンス体制を求める。 | [第3章 3.1.4 まとめ; 第2章 2.8.7 / medium](https://www.med.or.jp/dl-med/teireikaiken/20260415_3.pdf#page=56) |

#### 監査ログ・記録 (corpus cell D)

**セル定義**: 判断過程、利用履歴、変更履歴、アクセス履歴などの記録と監査可能性を整理する。


| ガイドライン | 要求強度 | セル要約 | 原文リンク |
|---|---|---|---|
| NIST AI RMF | `should` | 文書化、インベントリ、来歴、監視結果の記録を求める。 | [GOVERN 1.5-1.6; MEASURE 2.8 / high](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf#page=20) |
| ISO/IEC 42001 | `not_assessed` | 監査ログ・記録要求は本文未取得で評価未了。 | [not assessed; standard text unavailable / low](https://www.iso.org/standard/81230.html) |
| JMSF/JMA | `mention` | エラー報告、データ保存、AIモニタリングの必要性に触れる。 | [第3章 3.3.2; 第2章 2.8.7 / low](https://www.med.or.jp/dl-med/teireikaiken/20260415_3.pdf#page=69) |

---

## 付録: 運用台帳項目

| 項目 | 記入欄 |
|---|---|
| AIシステム名 |  |
| 利用部署 |  |
| リスク区分 |  |
| 導入承認日 |  |
| データ処理責任者 |  |
| ベンダー連絡先 |  |
| 監視指標 |  |
| 有害事象報告先 |  |
| 教育実施日 |  |
| 変更履歴 |  |
| 廃止 / 停止条件 |  |

## Footnotes

[^cc-by]: 本資料のオリジナル編集物 (構成、要約、表) は CC-BY 4.0。第三者ガイドライン原文の権利は各権利者に帰属し、CC-BY の対象外。

**Disclaimer**: 本資料は公開ガイドラインの参照用コンパイルであり、法的助言、規制適合性の保証、診療判断、院内規程としての完全性を保証するものではありません。最終ポリシーは所属機関の規程、医療安全・情報セキュリティ・倫理審査手順、NIST/ISO/JMSF等の原文および適用法令を参照してください。
