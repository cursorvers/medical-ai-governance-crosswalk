# WHO AI for Health倫理・ガバナンス

> **DISCLAIMER**: 本資料は公開ガイドラインの参照用コンパイルです。法的助言、規制適合性の保証、診療判断ではありません。利用前に必ず原文を参照してください。

| 項目 | 値 |
|---|---|
| ID | `who-aih` |
| English | Ethics and governance of artificial intelligence for health |
| 発行主体 | World Health Organization |
| 管轄 | international |
| 種別 | ethical |
| Version | 2021 guidance + 2023 LLM update + 2024/2025 LMM guidance |
| Published | 2021-06-28 |
| Last reviewed | 2026-04-20 |
| Source | [official source](https://www.who.int/publications/i/item/9789240029200) |

## Summary

WHOの医療AI倫理・ガバナンス指針。2021年版の6原則に加え、LMM向け勧告を参照する。


## Cells

| 列 | 要求 | 要約 | Citation |
|---|---|---|---|
| A 適用対象 | 🔵 `mention` | 医療AI全般とLMMの医療・公衆衛生利用を対象にする。 | [Overview; 2021 guidance / high](https://iris.who.int/server/api/core/bitstreams/f780d926-4ae3-42ce-a6d6-e898a5562621/content#page=13) |
| B リスク分類 | 🔵 `mention` | LMMではリスクベース枠組みと規制負荷差に言及。 | [Section 5, Assessment of general-purpose foundation models and/or applications used in health care / high](https://iris.who.int/server/api/core/bitstreams/e9e62c65-6045-481e-bd04-20e206bc5039/content#page=65) |
| C 透明性 | 🟠 `should` | 透明性・説明可能性・理解可能性を中核原則に置く。 | [Executive summary; Section 5 / high](https://iris.who.int/server/api/core/bitstreams/f780d926-4ae3-42ce-a6d6-e898a5562621/content#page=42) |
| D 監査ログ | 🟠 `should` | LMMでは第三者監査、影響評価、公開を求める。 | [Sections 4.2, 5.2, 6.4 / high](https://iris.who.int/server/api/core/bitstreams/e9e62c65-6045-481e-bd04-20e206bc5039/content#page=18) |
| E Human oversight | 🟠 `should` | 医療判断は人間が管理し、人間監督点を設ける。 | [Executive summary; Protecting human autonomy / high](https://iris.who.int/server/api/core/bitstreams/f780d926-4ae3-42ce-a6d6-e898a5562621/content#page=41) |
| F データ品質バイアス | 🟠 `should` | 低品質・非代表データとバイアスの最小化を重視する。 | [Executive summary; inclusiveness and equity / high](https://iris.who.int/server/api/core/bitstreams/f780d926-4ae3-42ce-a6d6-e898a5562621/content#page=44) |
| G PCCP市販後 | 🔵 `mention` | 実使用中の継続的評価とリリース後監査に触れる。 | [Section 6.2; deployment responsibilities / medium](https://iris.who.int/server/api/core/bitstreams/e9e62c65-6045-481e-bd04-20e206bc5039/content#page=72) |
| H 責任 | 🟠 `should` | 責任と説明責任、被害救済、価値連鎖上の責任を求める。 | [Executive summary; responsibility and accountability / high](https://iris.who.int/server/api/core/bitstreams/f780d926-4ae3-42ce-a6d6-e898a5562621/content#page=44) |
| I 同意プライバシー | 🟠 `should` | プライバシー、機密性、有効な同意、データ保護を要求する。 | [Executive summary; Protecting human autonomy / high](https://iris.who.int/server/api/core/bitstreams/f780d926-4ae3-42ce-a6d6-e898a5562621/content#page=41) |
| J セキュリティ | 🔵 `mention` | 安全性とサイバーセキュリティ上のリスクを扱う。 | [Sections 4.2, 5.2; cybersecurity risks / high](https://iris.who.int/server/api/core/bitstreams/e9e62c65-6045-481e-bd04-20e206bc5039/content#page=18) |
| K 臨床評価 | 🟠 `should` | 安全性、正確性、有効性、性能証明を重視する。 | [Executive summary; human well-being and safety / high](https://iris.who.int/server/api/core/bitstreams/f780d926-4ae3-42ce-a6d6-e898a5562621/content#page=42) |
| L 国際整合 | 🟠 `should` | LMMと医療AIの国際的な協調ガバナンスを求める。 | [Section 8; International governance of LMMs / high](https://iris.who.int/server/api/core/bitstreams/e9e62c65-6045-481e-bd04-20e206bc5039/content#page=78) |
| M ライフサイクル | 🟠 `should` | 設計、導入、実使用中の継続評価を求める。 | [Executive summary; responsive and sustainable / high](https://iris.who.int/server/api/core/bitstreams/f780d926-4ae3-42ce-a6d6-e898a5562621/content#page=46) |

## Notes

### A 適用対象

2021年版はAI for health全般、LMM版は診療・患者利用・事務・教育・研究などを扱う。

### B リスク分類

"the burden of proof increasing with the level of risk" と記載。ただし分類表ではない。

### C 透明性

6原則の一つとして透明性、説明可能性、理解可能性を掲げる。

### D 監査ログ

LMM guidance は開発初期監査、影響評価、独立したリリース後監査を勧告する。

### E Human oversight

人間の自律、医療判断の人間による管理、human warranty を重視する。

### F データ品質バイアス

2021年版は公平性と包摂性、LMM版は訓練データ品質とバイアスを明示する。

### G PCCP市販後

PCCP固有用語ではないが、運用中評価、継続監視、post-release audits を扱う。

### H 責任

LMM guidance Section 7 は開発、提供、導入の価値連鎖上の責任にも言及する。

### I 同意プライバシー

2021年版は自律原則にプライバシー、機密性、有効な同意を含める。

### J セキュリティ

LMM guidance は安全性、サイバーセキュリティ、患者情報保護のリスクを列挙する。

### K 臨床評価

2021年版は安全性・正確性・有効性、LMM版は性能証明や医療機器規制適合を扱う。

### L 国際整合

LMM guidance は国際ルール形成、国連内協調、最低基準の整合を扱う。

### M ライフサイクル

2021年版は実使用中の継続的・体系的・透明な評価を求める。

---

**License / 引用スコープ**: 本サイトのオリジナル編集物 (マトリクス構造・要求強度判定・列定義・要約) は CC-BY 4.0。第三者ガイドライン原文の引用は各権利者帰属 (fair use / 著作権法第32条「引用」の範囲) で、CC-BY 対象外。詳細は [LICENSE](https://github.com/cursorvers-inc/medical-ai-governance-crosswalk/blob/main/LICENSE) 参照。
