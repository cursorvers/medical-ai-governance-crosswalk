# IMDRF SaMD作業部会文書

> **DISCLAIMER**: 本資料は公開ガイドラインの参照用コンパイルです。法的助言、規制適合性の保証、診療判断ではありません。利用前に必ず原文を参照してください。

| 項目 | 値 |
|---|---|
| ID | `imdrf-samd` |
| English | IMDRF Software as a Medical Device Working Group documents |
| 発行主体 | International Medical Device Regulators Forum |
| 管轄 | international |
| 種別 | regulatory_guidance |
| Version | N10/N12/N23/N41 + UDI N48 reference |
| Published | 2017-09-21 |
| Last reviewed | 2026-04-20 |
| Source | [official source](https://www.imdrf.org/working-groups/software-medical-device-samd) |

## Summary

IMDRFのSaMD定義、リスク分類、QMS、臨床評価、UDI参照をまとめた国際規制調和文書群。


## Cells

| 列 | 要求 | 要約 | Citation |
|---|---|---|---|
| A 適用対象 | 🟠 `should` | ハードウェアに属さず医療目的を果たすソフトをSaMDと定義。 | [N10 Section 5.1 Software as a Medical Device / high](https://www.imdrf.org/sites/default/files/docs/imdrf/final/technical/imdrf-tech-131209-samd-key-definitions-140901.pdf) |
| B リスク分類 | 🟠 `should` | 医療判断への寄与と状態重大性でIからIVに分類する。 | [N12 Sections 7.1-7.3 / high](https://www.imdrf.org/sites/default/files/docs/imdrf/final/technical/imdrf-tech-140918-samd-framework-risk-categorization-141013.pdf) |
| C 透明性 | 🔵 `mention` | 定義文、使用目的、表示・利用情報の明確化に言及する。 | [N10 Sections 5.4-5.5 / high](https://www.imdrf.org/sites/default/files/docs/imdrf/final/technical/imdrf-tech-131209-samd-key-definitions-140901.pdf) |
| D 監査ログ | 🟠 `should` | 文書管理、記録管理、構成追跡でトレーサビリティを保つ。 | [N23 Sections 7.4-7.5 / high](https://www.imdrf.org/sites/default/files/docs/imdrf/final/technical/imdrf-tech-151002-samd-qms.pdf) |
| E Human oversight | 🔵 `mention` | ユーザーリスク、使用環境、使用者支援への考慮に言及。 | [N23 Sections 7.3; 8.5 / medium](https://www.imdrf.org/sites/default/files/docs/imdrf/final/technical/imdrf-tech-151002-samd-qms.pdf) |
| F データ品質バイアス | 🟠 `should` | データ完全性、臨床データ品質、妥当性の確保を求める。 | [N41 Sections 6.0-7.0 / high](https://www.imdrf.org/sites/default/files/docs/imdrf/final/technical/imdrf-tech-170921-samd-n41-clinical-evaluation_1.pdf) |
| G PCCP市販後 | 🟠 `should` | 変更影響評価と市販後実性能データの継続監視を求める。 | [N41 Sections 8.3-8.4 / high](https://www.imdrf.org/sites/default/files/docs/imdrf/final/technical/imdrf-tech-170921-samd-n41-clinical-evaluation_1.pdf) |
| H 責任 | 🟠 `should` | SaMD製造者が品質、リスク、ライフサイクル管理を担う。 | [N23 Sections 6.0-7.0 / high](https://www.imdrf.org/sites/default/files/docs/imdrf/final/technical/imdrf-tech-151002-samd-qms.pdf) |
| I 同意プライバシー | 🟠 `should` | 患者データ等の機密性と安全な保管・廃棄を考慮する。 | [N23 Sections 8.2; 8.6 / high](https://www.imdrf.org/sites/default/files/docs/imdrf/final/technical/imdrf-tech-151002-samd-qms.pdf) |
| J セキュリティ | 🟠 `should` | 情報セキュリティ、脅威分析、脆弱性対策を安全と統合する。 | [N23 Sections 7.3; 8.3; 8.6 / high](https://www.imdrf.org/sites/default/files/docs/imdrf/final/technical/imdrf-tech-151002-samd-qms.pdf) |
| K 臨床評価 | 🟠 `should` | 臨床関連性、分析妥当性、臨床妥当性の三要素で評価する。 | [N41 Sections 5.0-7.0 / high](https://www.imdrf.org/sites/default/files/docs/imdrf/final/technical/imdrf-tech-170921-samd-n41-clinical-evaluation_1.pdf) |
| L 国際整合 | 🟠 `should` | 各国規制当局のSaMD用語・管理原則の収束を目的とする。 | [Working Group charter / high](https://www.imdrf.org/working-groups/software-medical-device-samd) |
| M ライフサイクル | 🟠 `should` | 計画、開発、検証、展開、保守、廃止までQMSで管理する。 | [N23 Sections 7.0-8.6 / high](https://www.imdrf.org/sites/default/files/docs/imdrf/final/technical/imdrf-tech-151002-samd-qms.pdf) |

## Notes

### A 適用対象

汎用プラットフォーム上で動く医療目的ソフト、IVD、モバイルアプリも定義に含まれる。

### B リスク分類

Category IVが最高影響、Category Iが最低影響。規制分類そのものではない。

### C 透明性

透明性一般ではなく、SaMD定義文、意図用途、ラベル・使用説明の情報に関する言及。

### D 監査ログ

監査ログという語ではないが、文書・記録・構成・苦情等の追跡可能性を扱う。

### E Human oversight

人間監督義務としては明示されず、ユーザーリスクと意図使用の考慮にとどまる。

### F データ品質バイアス

N23はデータ完全性、N41は臨床評価エビデンスの品質・関連性を扱う。

### G PCCP市販後

PCCPという用語ではないが、変更、市販後情報、継続学習、実世界性能監視を扱う。

### H 責任

組織リーダーシップ、説明責任、ガバナンス、資源提供をQMSの基盤に置く。

### I 同意プライバシー

同意手続ではなく、機微データ、患者情報、機密データの保護に関するQMS考慮。

### J セキュリティ

侵入検知、ペネトレーションテスト、脆弱性スキャン、データ完全性試験に言及。

### K 臨床評価

SaMDの安全性、有効性、性能を示す臨床評価の収束的アプローチを定義。

### L 国際整合

国際的な共通語彙、リスク分類、QMS、臨床評価原則の整合を狙う。

### M ライフサイクル

ライフサイクル支援プロセスと実現・使用プロセスをSaMD全体に適用する。

---

**License / 引用スコープ**: 本サイトのオリジナル編集物 (マトリクス構造・要求強度判定・列定義・要約) は CC-BY 4.0。第三者ガイドライン原文の引用は各権利者帰属 (fair use / 著作権法第32条「引用」の範囲) で、CC-BY 対象外。詳細は [LICENSE](https://github.com/cursorvers/medical-ai-governance-crosswalk/blob/main/LICENSE) 参照。
