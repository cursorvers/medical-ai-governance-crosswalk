# Medical AI Governance Crosswalk

> **DISCLAIMER**: 本資料は公開ガイドラインの参照用コンパイルです。法的助言、規制適合性の保証、診療判断ではありません。利用前に必ず原文を参照してください。

<div class="gl-hero">
  <p class="gl-hero-tag">医療AIの公開ガイドライン10本×論点13列を、外来30秒で引けるクロスウォーク</p>
  <p class="gl-hero-sub">臨床医・研究者・医療機関 "使う側" の意思決定支援 / LLM非依存・静的検索（ハルシネーション回避）</p>
</div>

## 3つの使い方シナリオ

!!! tip "シナリオ1: 外来中30秒"
    患者から「このAI診断の安全性は？」と聞かれた → 検索ボックスに `透明性` `説明可能性` と入れる → 該当列の10ガイドラインの要求レベル(must/should/mention)即提示

!!! example "シナリオ2: IRB申請前チェック"
    自施設の臨床研究で AI 使う前 → `IRB` `同意` `プライバシー` で検索 → 申請書の論点漏れ防止 → <a href="evidence/irb-question-checklist.md">IRB質問チェックリスト</a> DL

!!! example "シナリオ3: 病院AI導入ポリシー作成"
    委員会で AI 導入規程を起草 → `責任主体` `監査ログ` `セキュリティ` で検索 → <a href="evidence/hospital-ai-adoption-policy.md">病院AI導入ポリシー骨子</a> を骨子に展開

## 論点を引く

<div class="gl-suggest">
  <button class="gl-suggest-btn" data-query="IRB">IRB</button>
  <button class="gl-suggest-btn" data-query="透明性">透明性</button>
  <button class="gl-suggest-btn" data-query="バイアス">バイアス</button>
  <button class="gl-suggest-btn" data-query="責任主体">責任主体</button>
</div>

<div id="gl-lookup">
  <input type="text" id="gl-query" placeholder="例: IRBで何を聞かれる?" aria-label="ガイドライン論点検索">
  <div id="gl-results"></div>
</div>
<script src="assets/lookup.js"></script>

## 📄 すぐ使えるテンプレ (Evidence Pack)

- <a href="evidence/clinician-ai-product-evaluation.md">臨床AI製品導入評価チェックリスト</a>
- <a href="evidence/patient-ai-intervention-explanation.md">患者AI介入説明文テンプレ</a>
- <a href="evidence/hospital-ai-adoption-policy.md">病院AI導入ポリシー骨子</a>
- <a href="evidence/irb-question-checklist.md">IRB質問チェックリスト</a>
- <a href="evidence/pccp-skeleton.md">PCCP骨子</a>

## 3レイヤー地図

| レイヤー | 論点 |
|---|---|
| 規制・責任 | A 適用対象<br>B リスク分類<br>H 責任<br>I 同意プライバシー<br>L 国際整合 |
| 研究・評価 | F データ品質バイアス<br>K 臨床評価 |
| 運用・ライフサイクル | C 透明性<br>D 監査ログ<br>E Human oversight<br>G PCCP市販後<br>J セキュリティ<br>M ライフサイクル |

## 概要

臨床医・臨床研究者・医療機関 (医療安全/IT/IRB事務局) が、主要ガイドラインを13論点で横断確認するための引用付き資料です。SaMD製造者の承認申請支援は対象外です。

## 収録ガイドライン

- [EU AI法](guidelines/eu-ai-act.md) (European Parliament and Council of the European Union)
- [FDA AI/ML SaMDアクションプラン・PCCPガイダンス](guidelines/fda-aiml-saamd-ap.md) (U.S. Food and Drug Administration)
- [IMDRF SaMD作業部会文書](guidelines/imdrf-samd.md) (International Medical Device Regulators Forum)
- [ISO/IEC 42001 AIマネジメントシステム](guidelines/iso-iec-42001.md) (ISO/IEC JTC 1/SC 42)
- [日本医師会 AIの臨床利用答申](guidelines/jmsf-ai-medical.md) (日本医師会)
- [経済産業省 AI事業者ガイドライン](guidelines/meti-ai-guidelines.md) (経済産業省)
- [厚労省 医療機器プログラムに関する取扱い](guidelines/mhlw-samd.md) (Ministry of Health, Labour and Welfare)
- [NIST AIリスクマネジメントフレームワーク](guidelines/nist-ai-rmf.md) (National Institute of Standards and Technology)
- [PMDA SaMD情報ページ](guidelines/pmda-samd.md) (Pharmaceuticals and Medical Devices Agency)
- [WHO AI for Health倫理・ガバナンス](guidelines/who-aih.md) (World Health Organization)

## 読み方

- `must`: 明示的な要求または強い義務
- `should`: 推奨、原則、実施すべき事項
- `mention`: 言及あり
- `none`: 扱いなし
- `not_assessed`: 未評価
- `source_unavailable`: 出典確認不可

---

**License / 引用スコープ**: 本サイトのオリジナル編集物 (マトリクス構造・要求強度判定・列定義・要約) は CC-BY 4.0。第三者ガイドライン原文の引用は各権利者帰属 (fair use / 著作権法第32条「引用」の範囲) で、CC-BY 対象外。詳細は [LICENSE](https://github.com/cursorvers/medical-ai-governance-crosswalk/blob/main/LICENSE) 参照。
