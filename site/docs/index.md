# Medical AI Governance Crosswalk

> **DISCLAIMER**: 本資料は公開ガイドラインの参照用コンパイルです。法的助言、規制適合性の保証、診療判断ではありません。利用前に必ず原文を参照してください。

<div id="gl-lookup">
  <input type="text" id="gl-query" placeholder="例: IRBで何を聞かれる?" aria-label="ガイドライン論点検索">
  <div id="gl-results"></div>
</div>
<script src="assets/lookup.js"></script>

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

**License / 引用スコープ**: 本サイトのオリジナル編集物 (マトリクス構造・要求強度判定・列定義・要約) は CC-BY 4.0。第三者ガイドライン原文の引用は各権利者帰属 (fair use / 著作権法第32条「引用」の範囲) で、CC-BY 対象外。詳細は [LICENSE](https://github.com/cursorvers-inc/medical-ai-governance-crosswalk/blob/main/LICENSE) 参照。
