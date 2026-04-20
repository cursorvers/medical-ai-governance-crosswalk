# Roadmap

## Wave 1 Pilot (v0.1)
- PMDA / MHLW / FDA / EU AI Act / WHO : 13 cells 埋まっているが一部 not_assessed
- not_assessed の理由: 原文未確認、または言及なし
- Evidence Pack は臨床医・臨床研究者・医療機関向けの5本を default 生成対象にする

## v0.2 でやること
- 学会発表用: 医療AI倫理・ガバナンス根拠引用テンプレート
- 医学教育: 医師国家試験・専門医試験向けガバナンス要点スライド骨子
- 多言語患者説明: EN/ZH/KO の患者同意文テンプレート
- `@cursorversinc/guidescope-medical-corpus` npm package を publish し、GuideScope 本体へ医療 corpus として組み込む
- Wave 3: ISO/IEC 42001 本文を取得し、引用可能な節番号・取得日・信頼度付きで再評価する

## Wave 2 (進行中)
- NIST AI RMF / ISO/IEC 42001 / IMDRF SaMD / 日本医学会連合 / 経産省

## v0.3 でやること
- 「臨床質問→該当GLセル即提示」の検索UIを実装する
- GuideScope 本体の citation interface と medical corpus package の連携を検証する

## Wave 3 (未着手)
- ISO/IEC 42001 本文取得後の cell 深堀り
- not_assessed cell の深堀り (PMDA 関連通知・審査ポイント、WHO LMM guidance)
- 学会・保険・国際調和の追加

## Issue テンプレート
`.github/ISSUE_TEMPLATE/cell-update.md` を通じた cell 更新 PR を歓迎
