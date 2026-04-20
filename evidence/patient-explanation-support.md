# 患者説明・インフォームドコンセント補助テンプレート

> **目的**: 医師が外来・病棟でAI介入を患者に説明する際に、AI使用、想定利益、既知の限界、代替手段、拒否・撤回の権利を整理する。
> **対象**: 外来・病棟で患者にAI介入を説明する医師、研究者、説明文書を作る臨床研究チーム。

## 説明対象

| 項目 | 記入欄 |
|---|---|
| 診療 / 研究 / 説明場面 |  |
| 使用するAIシステム |  |
| AIが扱う情報 |  |
| AIの出力 |  |
| 最終判断者 |  |
| 患者への説明者 |  |
| 拒否・撤回時の代替対応 |  |

## 参照ガイドライン

| ガイドライン | 要約 | 原文 |
|---|---|---|
| WHO AIH | WHOの医療AI倫理・ガバナンス指針。2021年版の6原則に加え、LMM向け勧告を参照する。 | [official source](https://www.who.int/publications/i/item/9789240029200) |
| JMSF/JMA | 日本医師会のAI臨床利用に関する答申。医師主導、人間中心、情報管理、責任、生命倫理上の課題を整理する。 | [official source](https://www.med.or.jp/dl-med/teireikaiken/20260415_3.pdf) |
| EU AI Act | EUのAI包括規則。医療機器AI等の高リスク分類、提供者義務、監視・透明性を定める。 | [official source](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R1689) |

## ① AIを使用する旨の説明

**確認観点**: 診療または研究でAIがどの役割を担うか、患者に理解できる言葉で説明する。

### 説明文ドラフト欄

- この診療・検査・説明でAIを使うことを明示する。
- AIは医師の判断を補助するもので、最終判断者を明確にする。
- 患者が質問できる窓口と、AIを使う範囲を伝える。

> 患者向け表現:
>
> 

### 確認メモ

- 説明済み / 未説明:
- 患者からの質問:
- 追加説明が必要な点:

### 根拠セル要約

#### 透明性・説明責任 (corpus cell C)

**セル定義**: 利用者、医療者、患者、規制当局への説明、表示、根拠提示、情報開示を整理する。


| ガイドライン | 要求強度 | セル要約 | 原文リンク |
|---|---|---|---|
| WHO AIH | `should` | 透明性・説明可能性・理解可能性を中核原則に置く。 | [Executive summary; Section 5 / high](https://iris.who.int/server/api/core/bitstreams/f780d926-4ae3-42ce-a6d6-e898a5562621/content#page=42) |
| JMSF/JMA | `should` | AI使用の患者通知、透明性措置、医師確認を重視する。 | [第3章 3.3.2 記録・文書作成の補助 / medium](https://www.med.or.jp/dl-med/teireikaiken/20260415_3.pdf#page=69) |
| EU AI Act | `must` | 提供者は導入者へ性能、限界、使用説明を提供する義務。 | [Article 13(1)-(3) / medium](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R1689#art-13) |

## ② 想定利益

**確認観点**: AI利用により期待される診療上・説明上の利益を、過大に約束せず整理する。

### 説明文ドラフト欄

- 診断補助、見落とし低減、待ち時間短縮、説明の標準化など期待される利益を書く。
- 利益は保証ではなく、個々の患者で結果が異なることを説明する。
- 医師がAI出力を確認し、必要に応じて追加検査や通常診療を行うことを明記する。

> 患者向け表現:
>
> 

### 確認メモ

- 説明済み / 未説明:
- 患者からの質問:
- 追加説明が必要な点:

### 根拠セル要約

#### ⑤ 臨床評価計画 (corpus cell K)

**セル定義**: 臨床試験、臨床研究、性能評価、有効性・安全性評価、申請資料を整理する。


| ガイドライン | 要求強度 | セル要約 | 原文リンク |
|---|---|---|---|
| WHO AIH | `should` | 安全性、正確性、有効性、性能証明を重視する。 | [Executive summary; human well-being and safety / high](https://iris.who.int/server/api/core/bitstreams/f780d926-4ae3-42ce-a6d6-e898a5562621/content#page=42) |
| JMSF/JMA | `mention` | 診断・治療補助では性能、透明性、医師判断への影響を検討する。 | [第3章 3.3.3 診断・治療の補助 / medium](https://www.med.or.jp/dl-med/teireikaiken/20260415_3.pdf#page=70) |
| EU AI Act | `must` | 意図目的に照らした試験・妥当性確認と性能指標を要求。 | [Article 9(6)-(8); Article 15(1)-(4) / medium](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R1689#art-9) |

#### 透明性・説明責任 (corpus cell C)

**セル定義**: 利用者、医療者、患者、規制当局への説明、表示、根拠提示、情報開示を整理する。


| ガイドライン | 要求強度 | セル要約 | 原文リンク |
|---|---|---|---|
| WHO AIH | `should` | 透明性・説明可能性・理解可能性を中核原則に置く。 | [Executive summary; Section 5 / high](https://iris.who.int/server/api/core/bitstreams/f780d926-4ae3-42ce-a6d6-e898a5562621/content#page=42) |
| JMSF/JMA | `should` | AI使用の患者通知、透明性措置、医師確認を重視する。 | [第3章 3.3.2 記録・文書作成の補助 / medium](https://www.med.or.jp/dl-med/teireikaiken/20260415_3.pdf#page=69) |
| EU AI Act | `must` | 提供者は導入者へ性能、限界、使用説明を提供する義務。 | [Article 13(1)-(3) / medium](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R1689#art-13) |

## ③ 既知の限界・リスク (cell B, D)

**確認観点**: 誤出力、偏り、説明不能性、過信、記録・監査上の限界を患者説明に落とす。

### 説明文ドラフト欄

- AIが誤った提案、過不足のある説明、患者背景に合わない出力を出す可能性を伝える。
- 年齢、疾患、検査条件、データの偏りにより性能が変わる可能性を説明する。
- AI利用の記録、問題発生時の確認手順、医師による再確認を伝える。

> 患者向け表現:
>
> 

### 確認メモ

- 説明済み / 未説明:
- 患者からの質問:
- 追加説明が必要な点:

### 根拠セル要約

#### ③ リスク分類 (corpus cell B)

**セル定義**: 医療機器クラス、AIリスク分類、患者安全への影響度などの分類方法を整理する。


| ガイドライン | 要求強度 | セル要約 | 原文リンク |
|---|---|---|---|
| WHO AIH | `mention` | LMMではリスクベース枠組みと規制負荷差に言及。 | [Section 5, Assessment of general-purpose foundation models and/or applications used in health care / high](https://iris.who.int/server/api/core/bitstreams/e9e62c65-6045-481e-bd04-20e206bc5039/content#page=65) |
| JMSF/JMA | `mention` | 臨床利用を3類型に分け、悪用や制度的リスクも整理する。 | [第3章 3.3.1 AIの臨床利用の3類型 / medium](https://www.med.or.jp/dl-med/teireikaiken/20260415_3.pdf#page=68) |
| EU AI Act | `must` | Annex I対象かAnnex III該当なら高リスクAIに分類。 | [Article 6(1)-(4); Annex III point 5(a), 5(d) / medium](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R1689#art-6) |

#### 監査ログ・記録 (corpus cell D)

**セル定義**: 判断過程、利用履歴、変更履歴、アクセス履歴などの記録と監査可能性を整理する。


| ガイドライン | 要求強度 | セル要約 | 原文リンク |
|---|---|---|---|
| WHO AIH | `should` | LMMでは第三者監査、影響評価、公開を求める。 | [Sections 4.2, 5.2, 6.4 / high](https://iris.who.int/server/api/core/bitstreams/e9e62c65-6045-481e-bd04-20e206bc5039/content#page=18) |
| JMSF/JMA | `mention` | エラー報告、データ保存、AIモニタリングの必要性に触れる。 | [第3章 3.3.2; 第2章 2.8.7 / low](https://www.med.or.jp/dl-med/teireikaiken/20260415_3.pdf#page=69) |
| EU AI Act | `must` | 高リスクAIはライフタイム中の自動ログ記録を技術的に可能にする。 | [Article 12(1)-(2); Article 21(2) / medium](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R1689#art-12) |

#### データ品質・バイアス (corpus cell F)

**セル定義**: 学習・評価・入力データの品質、代表性、偏り、根拠、検証可能性を整理する。


| ガイドライン | 要求強度 | セル要約 | 原文リンク |
|---|---|---|---|
| WHO AIH | `should` | 低品質・非代表データとバイアスの最小化を重視する。 | [Executive summary; inclusiveness and equity / high](https://iris.who.int/server/api/core/bitstreams/f780d926-4ae3-42ce-a6d6-e898a5562621/content#page=44) |
| JMSF/JMA | `should` | バイアス、データセットシフト、精度劣化への注意を求める。 | [第3章 3.3.3 診断・治療の補助 / medium](https://www.med.or.jp/dl-med/teireikaiken/20260415_3.pdf#page=71) |
| EU AI Act | `must` | 訓練・検証・試験データの品質とバイアス対策を要求。 | [Article 10(1)-(5) / medium](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R1689#art-10) |

## ④ 代替手段

**確認観点**: AIを使わない通常診療、医師判断、追加検査、セカンドオピニオンを選べることを説明する。

### 説明文ドラフト欄

- AIを使わない場合の診療手順や説明方法を伝える。
- AIの提案と医師判断が異なる場合の扱いを説明する。
- 必要に応じて追加検査、専門医相談、セカンドオピニオンが可能であることを伝える。

> 患者向け表現:
>
> 

### 確認メモ

- 説明済み / 未説明:
- 患者からの質問:
- 追加説明が必要な点:

### 根拠セル要約

#### Human oversight (corpus cell E)

**セル定義**: 医師、使用者、事業者、管理者による監督、介入、最終判断、適正使用を整理する。


| ガイドライン | 要求強度 | セル要約 | 原文リンク |
|---|---|---|---|
| WHO AIH | `should` | 医療判断は人間が管理し、人間監督点を設ける。 | [Executive summary; Protecting human autonomy / high](https://iris.who.int/server/api/core/bitstreams/f780d926-4ae3-42ce-a6d6-e898a5562621/content#page=41) |
| JMSF/JMA | `should` | 医師参加型原則により医師が確認し最終判断を行う。 | [第3章 3.1.2 WMAが示す医師参加型原則 / medium](https://www.med.or.jp/dl-med/teireikaiken/20260415_3.pdf#page=53) |
| EU AI Act | `must` | 高リスクAIは自然人による有効な監督を可能に設計する。 | [Article 14(1)-(5) / medium](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R1689#art-14) |

#### 透明性・説明責任 (corpus cell C)

**セル定義**: 利用者、医療者、患者、規制当局への説明、表示、根拠提示、情報開示を整理する。


| ガイドライン | 要求強度 | セル要約 | 原文リンク |
|---|---|---|---|
| WHO AIH | `should` | 透明性・説明可能性・理解可能性を中核原則に置く。 | [Executive summary; Section 5 / high](https://iris.who.int/server/api/core/bitstreams/f780d926-4ae3-42ce-a6d6-e898a5562621/content#page=42) |
| JMSF/JMA | `should` | AI使用の患者通知、透明性措置、医師確認を重視する。 | [第3章 3.3.2 記録・文書作成の補助 / medium](https://www.med.or.jp/dl-med/teireikaiken/20260415_3.pdf#page=69) |
| EU AI Act | `must` | 提供者は導入者へ性能、限界、使用説明を提供する義務。 | [Article 13(1)-(3) / medium](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R1689#art-13) |

## ⑤ 拒否/撤回の権利 (cell I)

**確認観点**: AI利用、データ利用、二次利用への同意・拒否・撤回を説明する。

### 説明文ドラフト欄

- AI利用やデータ利用を拒否できる範囲、拒否時の診療への影響を説明する。
- 撤回後のデータ、記録、既に実施された解析結果の扱いを明示する。
- 外部サービス、クラウド、ベンダー改善利用がある場合は別に説明する。

> 患者向け表現:
>
> 

### 確認メモ

- 説明済み / 未説明:
- 患者からの質問:
- 追加説明が必要な点:

### 根拠セル要約

#### 同意・プライバシー (corpus cell I)

**セル定義**: 患者・利用者データの同意、プライバシー、個人情報、共有、二次利用を整理する。


| ガイドライン | 要求強度 | セル要約 | 原文リンク |
|---|---|---|---|
| WHO AIH | `should` | プライバシー、機密性、有効な同意、データ保護を要求する。 | [Executive summary; Protecting human autonomy / high](https://iris.who.int/server/api/core/bitstreams/f780d926-4ae3-42ce-a6d6-e898a5562621/content#page=41) |
| JMSF/JMA | `should` | 機微な診療情報の機密性、不正アクセス防止、同意を重視する。 | [第3章 3.1.2 WMAが示す医師参加型原則 / medium](https://www.med.or.jp/dl-med/teireikaiken/20260415_3.pdf#page=54) |
| EU AI Act | `must` | 個人データ保護法を維持し、特殊データ処理に保護条件を課す。 | [Article 2(7); Article 10(5) / medium](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R1689#art-10) |

#### 責任主体・説明責任 (corpus cell H)

**セル定義**: 開発者、製造販売業者、医療者、使用者、規制当局などの責任範囲を整理する。


| ガイドライン | 要求強度 | セル要約 | 原文リンク |
|---|---|---|---|
| WHO AIH | `should` | 責任と説明責任、被害救済、価値連鎖上の責任を求める。 | [Executive summary; responsibility and accountability / high](https://iris.who.int/server/api/core/bitstreams/f780d926-4ae3-42ce-a6d6-e898a5562621/content#page=44) |
| JMSF/JMA | `should` | 医師、開発者、行政を含む責任分担の必要性を示す。 | [第3章 3.3.3 診断・治療の補助 / medium](https://www.med.or.jp/dl-med/teireikaiken/20260415_3.pdf#page=72) |
| EU AI Act | `must` | 提供者等の義務とQMS内の責任枠組みを定める。 | [Article 16; Article 17(1)(m) / medium](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R1689#art-17) |

---

## 説明・同意記録

| 項目 | メモ |
|---|---|
| AI利用の説明 |  |
| 利益と限界の説明 |  |
| 代替手段の説明 |  |
| 拒否・撤回の説明 |  |
| データ利用・外部提供の説明 |  |
| 患者の希望 / 質問 |  |
| 同意 / 不同意 / 保留 |  |

## Footnotes

[^cc-by]: 本資料のオリジナル編集物 (構成、要約、表) は CC-BY 4.0。第三者ガイドライン原文の権利は各権利者に帰属し、CC-BY の対象外。

**Disclaimer**: 本資料は公開ガイドラインの参照用コンパイルであり、法的助言、規制適合性の保証、診療判断、同意取得の法的有効性を保証するものではありません。最終説明文は所属機関の同意手順、倫理審査、個人情報保護規程、WHO/JMSF/EU等の原文および適用法令を参照してください。
