# 医療AI製品 導入評価チェックリスト

> **目的**: 臨床医が病棟・外来で医療AI製品の導入可否を判断する前に、適応、リスク、透明性、バイアス、データ保護、運用責任を確認する。
> **対象**: 病棟・外来でAI製品導入判断を迫られる医師、診療科責任者、臨床研究者、院内AI導入審査担当者。

## いつ使う？

**シーン 1: ベンダー提案の逸脱判定** — メーカー営業から新しいAI診断支援ソフトの提案書を受領したとき、ベンダー提案 vs ガイドライン要件の gap をこのチェックリストで埋めながら横断確認します。詳しい流れは [使い方シナリオ #1](../usage.md#1) を参照。

## 評価対象

| 項目 | 記入欄 |
|---|---|
| 製品名 / ベンダー |  |
| 利用予定部署 / 診療科 |  |
| 想定する診療場面 |  |
| 対象患者 / 除外患者 |  |
| 入力データ |  |
| AI出力 / 推奨内容 |  |
| 医師の最終判断プロセス |  |
| 患者説明が必要な場面 |  |
| 導入判定 | □ 導入可 / □ 条件付き / □ 保留 / □ 不採用 |

## 参照ガイドライン

| ガイドライン | 要約 | 原文 |
|---|---|---|
| WHO AIH | WHOの医療AI倫理・ガバナンス指針。2021年版の6原則に加え、LMM向け勧告を参照する。 | [official source](https://www.who.int/publications/i/item/9789240029200) |
| FDA GMLP/PCCP | FDAのAI/ML SaMD監督方針とPCCP提出推奨を整理し、TPLC・透明性・性能監視を示す。 | [official source](https://www.fda.gov/medical-devices/software-medical-device-samd/artificial-intelligence-and-machine-learning-software-medical-device) |
| EU AI Act | EUのAI包括規則。医療機器AI等の高リスク分類、提供者義務、監視・透明性を定める。 | [official source](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R1689) |

## ① 製品概要

**確認観点**: 導入候補AIの用途、臨床的位置づけ、利用環境、利用者、患者集団を整理する。

### チェック項目

- [ ] AIが支援する診療行為、対象患者、利用場面、除外条件を記載する。
- [ ] AI出力が診断、治療方針、トリアージ、文書作成、患者説明のどこに影響するかを分ける。
- [ ] 医師、看護師、患者、ベンダー、院内管理者の関与範囲を記録する。

### 判定メモ

- 現時点の根拠:
- 未確認事項:
- 導入条件 / 保留理由:
- 追加で求める資料:

### 根拠セル要約

#### ② 該当性判定 (corpus cell A)

**セル定義**: 対象となる製品、ソフトウェア、利用場面、開発段階、除外範囲を整理する。


| ガイドライン | 要求強度 | セル要約 | 原文リンク |
|---|---|---|---|
| WHO AIH | `mention` | 医療AI全般とLMMの医療・公衆衛生利用を対象にする。 | [Overview; 2021 guidance / high](https://iris.who.int/server/api/core/bitstreams/f780d926-4ae3-42ce-a6d6-e898a5562621/content#page=13) |
| FDA GMLP/PCCP | `should` | AI-DSFを含む医療機器と510(k)等の提出が主対象。 | [PCCP Guidance, Section III Scope / high](https://www.fda.gov/media/166704/download#page=9) |
| EU AI Act | `must` | EU市場・利用のAIに適用し医療機器AIも対象化。 | [Article 2(1); Article 6(1); Annex I Section A points 11-12 / medium](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R1689#art-6) |

## ② 適応 (cell A)

**確認観点**: 候補製品の適用対象と、自施設での実使用条件が一致するかを確認する。

### チェック項目

- [ ] 添付文書、利用規約、説明資料に書かれた intended use と現場の使い方は一致するか。
- [ ] 対象疾患、年齢層、検査種別、診療科、施設規模に外挿がないか。
- [ ] 研究利用、診療補助、患者向け利用、管理業務利用の境界は明確か。

### 判定メモ

- 現時点の根拠:
- 未確認事項:
- 導入条件 / 保留理由:
- 追加で求める資料:

### 根拠セル要約

#### ② 該当性判定 (corpus cell A)

**セル定義**: 対象となる製品、ソフトウェア、利用場面、開発段階、除外範囲を整理する。


| ガイドライン | 要求強度 | セル要約 | 原文リンク |
|---|---|---|---|
| WHO AIH | `mention` | 医療AI全般とLMMの医療・公衆衛生利用を対象にする。 | [Overview; 2021 guidance / high](https://iris.who.int/server/api/core/bitstreams/f780d926-4ae3-42ce-a6d6-e898a5562621/content#page=13) |
| FDA GMLP/PCCP | `should` | AI-DSFを含む医療機器と510(k)等の提出が主対象。 | [PCCP Guidance, Section III Scope / high](https://www.fda.gov/media/166704/download#page=9) |
| EU AI Act | `must` | EU市場・利用のAIに適用し医療機器AIも対象化。 | [Article 2(1); Article 6(1); Annex I Section A points 11-12 / medium](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R1689#art-6) |

## ③ リスク評価 (cell B)

**確認観点**: 誤出力、過信、診療遅延、責任分担などのリスクを臨床文脈で整理する。

### チェック項目

- [ ] AIの誤判定が患者安全に与える最大影響を具体的に書く。
- [ ] 人間の確認で検出できるリスクと、検出しにくいリスクを分ける。
- [ ] 高リスク患者、緊急時、夜間休日、経験の浅い利用者でリスクが変わるか確認する。

### 判定メモ

- 現時点の根拠:
- 未確認事項:
- 導入条件 / 保留理由:
- 追加で求める資料:

### 根拠セル要約

#### ③ リスク分類 (corpus cell B)

**セル定義**: 医療機器クラス、AIリスク分類、患者安全への影響度などの分類方法を整理する。


| ガイドライン | 要求強度 | セル要約 | 原文リンク |
|---|---|---|---|
| WHO AIH | `mention` | LMMではリスクベース枠組みと規制負荷差に言及。 | [Section 5, Assessment of general-purpose foundation models and/or applications used in health care / high](https://iris.who.int/server/api/core/bitstreams/e9e62c65-6045-481e-bd04-20e206bc5039/content#page=65) |
| FDA GMLP/PCCP | `should` | IMDRFリスク分類やFDA便益リスクを踏まえた監督を想定。 | [Introduction &amp; Background; Action 1 / high](https://www.fda.gov/files/medical%20devices/published/AIML-SaMD-Action-Plan.pdf#page=2) |
| EU AI Act | `must` | Annex I対象かAnnex III該当なら高リスクAIに分類。 | [Article 6(1)-(4); Annex III point 5(a), 5(d) / medium](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R1689#art-6) |

## ④ 透明性/説明可能性 (cell C, F)

**確認観点**: 利用者と患者が、AIの役割、性能、限界、データ根拠を理解できるかを確認する。

### チェック項目

- [ ] 医師がAI出力の意味、根拠、信頼区間、適用外条件を説明できるか。
- [ ] 学習・評価データの代表性、外部検証、性能指標、更新日が入手できるか。
- [ ] 説明できない出力を診療に使わない条件、または追加確認の条件を定める。

### 判定メモ

- 現時点の根拠:
- 未確認事項:
- 導入条件 / 保留理由:
- 追加で求める資料:

### 根拠セル要約

#### 透明性・説明責任 (corpus cell C)

**セル定義**: 利用者、医療者、患者、規制当局への説明、表示、根拠提示、情報開示を整理する。


| ガイドライン | 要求強度 | セル要約 | 原文リンク |
|---|---|---|---|
| WHO AIH | `should` | 透明性・説明可能性・理解可能性を中核原則に置く。 | [Executive summary; Section 5 / high](https://iris.who.int/server/api/core/bitstreams/f780d926-4ae3-42ce-a6d6-e898a5562621/content#page=42) |
| FDA GMLP/PCCP | `should` | 学習データ、入力、ロジック、性能根拠等の透明性を推奨。 | [Action 3 Patient-Centered Approach Incorporating Transparency to Users / high](https://www.fda.gov/files/medical%20devices/published/AIML-SaMD-Action-Plan.pdf#page=5) |
| EU AI Act | `must` | 提供者は導入者へ性能、限界、使用説明を提供する義務。 | [Article 13(1)-(3) / medium](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R1689#art-13) |

#### データ品質・バイアス (corpus cell F)

**セル定義**: 学習・評価・入力データの品質、代表性、偏り、根拠、検証可能性を整理する。


| ガイドライン | 要求強度 | セル要約 | 原文リンク |
|---|---|---|---|
| WHO AIH | `should` | 低品質・非代表データとバイアスの最小化を重視する。 | [Executive summary; inclusiveness and equity / high](https://iris.who.int/server/api/core/bitstreams/f780d926-4ae3-42ce-a6d6-e898a5562621/content#page=44) |
| FDA GMLP/PCCP | `should` | バイアス識別・低減と頑健性評価の方法開発を重視。 | [Action 4 Regulatory Science Methods Related to Algorithm Bias &amp; Robustness / high](https://www.fda.gov/files/medical%20devices/published/AIML-SaMD-Action-Plan.pdf#page=6) |
| EU AI Act | `must` | 訓練・検証・試験データの品質とバイアス対策を要求。 | [Article 10(1)-(5) / medium](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R1689#art-10) |

## ⑤ バイアス/限界 (cell D)

**確認観点**: 性能差、監査可能性、記録、想定外使用を確認し、限界を運用ルールに落とす。

### チェック項目

- [ ] 年齢、性別、疾患、施設、言語、検査機器、データ欠損による性能差を確認したか。
- [ ] AI利用履歴、出力、医師判断、最終判断の記録を後から追跡できるか。
- [ ] 限界が見つかったときに、利用停止、対象制限、患者説明更新へつなげる手順はあるか。

### 判定メモ

- 現時点の根拠:
- 未確認事項:
- 導入条件 / 保留理由:
- 追加で求める資料:

### 根拠セル要約

#### 監査ログ・記録 (corpus cell D)

**セル定義**: 判断過程、利用履歴、変更履歴、アクセス履歴などの記録と監査可能性を整理する。


| ガイドライン | 要求強度 | セル要約 | 原文リンク |
|---|---|---|---|
| WHO AIH | `should` | LMMでは第三者監査、影響評価、公開を求める。 | [Sections 4.2, 5.2, 6.4 / high](https://iris.who.int/server/api/core/bitstreams/e9e62c65-6045-481e-bd04-20e206bc5039/content#page=18) |
| FDA GMLP/PCCP | `should` | PCCPではデータ管理、更新手順、追跡表で変更根拠を残す。 | [PCCP Guidance, Section VII.C Traceability / high](https://www.fda.gov/media/166704/download#page=33) |
| EU AI Act | `must` | 高リスクAIはライフタイム中の自動ログ記録を技術的に可能にする。 | [Article 12(1)-(2); Article 21(2) / medium](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R1689#art-12) |

#### データ品質・バイアス (corpus cell F)

**セル定義**: 学習・評価・入力データの品質、代表性、偏り、根拠、検証可能性を整理する。


| ガイドライン | 要求強度 | セル要約 | 原文リンク |
|---|---|---|---|
| WHO AIH | `should` | 低品質・非代表データとバイアスの最小化を重視する。 | [Executive summary; inclusiveness and equity / high](https://iris.who.int/server/api/core/bitstreams/f780d926-4ae3-42ce-a6d6-e898a5562621/content#page=44) |
| FDA GMLP/PCCP | `should` | バイアス識別・低減と頑健性評価の方法開発を重視。 | [Action 4 Regulatory Science Methods Related to Algorithm Bias &amp; Robustness / high](https://www.fda.gov/files/medical%20devices/published/AIML-SaMD-Action-Plan.pdf#page=6) |
| EU AI Act | `must` | 訓練・検証・試験データの品質とバイアス対策を要求。 | [Article 10(1)-(5) / medium](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R1689#art-10) |

## ⑥ データ保護 (cell H)

**確認観点**: 患者データの責任主体、外部提供、保存、再利用、委託先管理を確認する。

### チェック項目

- [ ] データ管理責任者、処理者、委託先、ベンダーの責任分担は契約上明確か。
- [ ] 診療情報がクラウド、外部API、モデル改善、二次利用に使われるか確認したか。
- [ ] アクセス制御、ログ、匿名化・仮名化、患者説明、問い合わせ窓口を確認したか。

### 判定メモ

- 現時点の根拠:
- 未確認事項:
- 導入条件 / 保留理由:
- 追加で求める資料:

### 根拠セル要約

#### 責任主体・説明責任 (corpus cell H)

**セル定義**: 開発者、製造販売業者、医療者、使用者、規制当局などの責任範囲を整理する。


| ガイドライン | 要求強度 | セル要約 | 原文リンク |
|---|---|---|---|
| WHO AIH | `should` | 責任と説明責任、被害救済、価値連鎖上の責任を求める。 | [Executive summary; responsibility and accountability / high](https://iris.who.int/server/api/core/bitstreams/f780d926-4ae3-42ce-a6d6-e898a5562621/content#page=44) |
| FDA GMLP/PCCP | `should` | 製造業者がPCCPを作成し品質システムで影響評価する。 | [PCCP Guidance, Section VIII Impact Assessment / high](https://www.fda.gov/media/166704/download#page=34) |
| EU AI Act | `must` | 提供者等の義務とQMS内の責任枠組みを定める。 | [Article 16; Article 17(1)(m) / medium](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R1689#art-17) |

#### 同意・プライバシー (corpus cell I)

**セル定義**: 患者・利用者データの同意、プライバシー、個人情報、共有、二次利用を整理する。


| ガイドライン | 要求強度 | セル要約 | 原文リンク |
|---|---|---|---|
| WHO AIH | `should` | プライバシー、機密性、有効な同意、データ保護を要求する。 | [Executive summary; Protecting human autonomy / high](https://iris.who.int/server/api/core/bitstreams/f780d926-4ae3-42ce-a6d6-e898a5562621/content#page=41) |
| FDA GMLP/PCCP | `mention` | 患者中心の信頼・透明性を扱うが同意手続は主題外。 | [Action 3 Patient-Centered Approach Incorporating Transparency to Users / medium](https://www.fda.gov/files/medical%20devices/published/AIML-SaMD-Action-Plan.pdf#page=5) |
| EU AI Act | `must` | 個人データ保護法を維持し、特殊データ処理に保護条件を課す。 | [Article 2(7); Article 10(5) / medium](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R1689#art-10) |

#### セキュリティ (corpus cell J)

**セル定義**: サイバーセキュリティ、アクセス制御、脆弱性対応、情報保護を整理する。


| ガイドライン | 要求強度 | セル要約 | 原文リンク |
|---|---|---|---|
| WHO AIH | `mention` | 安全性とサイバーセキュリティ上のリスクを扱う。 | [Sections 4.2, 5.2; cybersecurity risks / high](https://iris.who.int/server/api/core/bitstreams/e9e62c65-6045-481e-bd04-20e206bc5039/content#page=18) |
| FDA GMLP/PCCP | `mention` | GMLPを医療機器サイバーセキュリティ施策と連携すると記載。 | [Action 2 Good Machine Learning Practice (GMLP) / high](https://www.fda.gov/files/medical%20devices/published/AIML-SaMD-Action-Plan.pdf#page=4) |
| EU AI Act | `must` | 正確性、堅牢性、サイバーセキュリティ水準を確保する義務。 | [Article 15(1)-(5) / medium](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R1689#art-15) |

## ⑦ 運用・監査・責任 (cell L, 責任所在)

**確認観点**: 導入後監視、監査、エスカレーション、国際基準との整合、責任所在を固定する。

### チェック項目

- [ ] AI出力の採否、患者説明、有害事象対応の最終責任者を定める。
- [ ] 性能低下、インシデント、苦情、想定外使用をどの会議体へ報告するか決める。
- [ ] 導入後レビューの頻度、監査項目、停止基準、ベンダー再評価条件を記録する。

### 判定メモ

- 現時点の根拠:
- 未確認事項:
- 導入条件 / 保留理由:
- 追加で求める資料:

### 根拠セル要約

#### 国際整合・通知導線 (corpus cell L)

**セル定義**: GHTF、IMDRF、ISO、海外規制、国際展開、国際調和への言及を整理する。


| ガイドライン | 要求強度 | セル要約 | 原文リンク |
|---|---|---|---|
| WHO AIH | `should` | LMMと医療AIの国際的な協調ガバナンスを求める。 | [Section 8; International governance of LMMs / high](https://iris.who.int/server/api/core/bitstreams/e9e62c65-6045-481e-bd04-20e206bc5039/content#page=78) |
| FDA GMLP/PCCP | `mention` | GMLP標準化やIMDRF等との国際調和を推進。 | [Action 2 Good Machine Learning Practice (GMLP) / high](https://www.fda.gov/files/medical%20devices/published/AIML-SaMD-Action-Plan.pdf#page=4) |
| EU AI Act | `mention` | 整合規格・共通仕様と既存EU整合法令との接続を規定。 | [Article 8(2); Article 40; Article 41 / medium](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R1689#art-40) |

#### 責任主体・説明責任 (corpus cell H)

**セル定義**: 開発者、製造販売業者、医療者、使用者、規制当局などの責任範囲を整理する。


| ガイドライン | 要求強度 | セル要約 | 原文リンク |
|---|---|---|---|
| WHO AIH | `should` | 責任と説明責任、被害救済、価値連鎖上の責任を求める。 | [Executive summary; responsibility and accountability / high](https://iris.who.int/server/api/core/bitstreams/f780d926-4ae3-42ce-a6d6-e898a5562621/content#page=44) |
| FDA GMLP/PCCP | `should` | 製造業者がPCCPを作成し品質システムで影響評価する。 | [PCCP Guidance, Section VIII Impact Assessment / high](https://www.fda.gov/media/166704/download#page=34) |
| EU AI Act | `must` | 提供者等の義務とQMS内の責任枠組みを定める。 | [Article 16; Article 17(1)(m) / medium](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R1689#art-17) |

#### ⑥ ライフサイクル管理 (corpus cell M)

**セル定義**: 開発、申請、導入、教育、変更、更新、廃止までの継続管理を整理する。


| ガイドライン | 要求強度 | セル要約 | 原文リンク |
|---|---|---|---|
| WHO AIH | `should` | 設計、導入、実使用中の継続評価を求める。 | [Executive summary; responsive and sustainable / high](https://iris.who.int/server/api/core/bitstreams/f780d926-4ae3-42ce-a6d6-e898a5562621/content#page=46) |
| FDA GMLP/PCCP | `should` | 開発前から市販後までTPLC監督とRWP監視を重視。 | [Introduction &amp; Background; Action 5 Real-World Performance (RWP) / high](https://www.fda.gov/files/medical%20devices/published/AIML-SaMD-Action-Plan.pdf#page=7) |
| EU AI Act | `must` | リスク管理、QMS、市販後監視を通じた継続管理を要求。 | [Article 9(2); Article 17(1); Article 72 / medium](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R1689#art-72) |

---

## 最終導入判定

| 判定項目 | メモ |
|---|---|
| 導入可否 |  |
| 必須条件 |  |
| 患者説明の要否 |  |
| 医療安全レビュー |  |
| 情報システム / セキュリティレビュー |  |
| 導入後モニタリング期限 |  |
| 再評価日 |  |

## Footnotes

[^cc-by]: 本資料のオリジナル編集物 (構成、要約、表) は CC-BY 4.0。第三者ガイドライン原文の権利は各権利者に帰属し、CC-BY の対象外。

**Disclaimer**: 本資料は公開ガイドラインの参照用コンパイルであり、法的助言、規制適合性の保証、診療判断ではありません。最終判断は必ず所属機関の規程、製品添付文書・契約、WHO/FDA/EU等の原文および適用法令を参照してください。
