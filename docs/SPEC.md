# Medical AI Governance Crosswalk — SPEC (v2, Phase A locked)

**Run ID**: 2026-04-20-medgov-crosswalk
**Status**: LOCKED (Codex + Copilot 合議: hybrid 採用、Codex 8.5/Copilot 7.0)
**Predecessor**: SPEC-v1-provenance-rounds-ARCHIVED.md (software tool 案、ピボット)

---

## 1. Product

- **Name**: `Medical AI Governance Crosswalk` (医療AIガバナンス横串帳)
- **Short**: `medai-crosswalk`
- **One-liner**: 医療AIを **使う側** (臨床医 / 臨床研究者 / 医療機関 IT・医療安全部門 / IRB事務局) が、規制 / 倫理 / 研究報告 / プライバシーの論点を **同じ表で読める引用可能な基準書**。
- **Primary users**: 臨床医、臨床研究者、医療機関 IT・医療安全部門、IRB事務局、倫理審査委員。
- **Out of scope**: SaMD製造者の承認申請支援、PMDA/FDA等への申請資料作成代行、規制適合性の保証。
- **Pitch**:
  > 医療AIガイドラインは PMDA・FDA・EU AI Act・WHO・NIST AI RMF・ISO/IEC 42001・IMDRF・TRIPOD-AI・CONSORT-AI・厚労省・日本医学会連合 …と **バラバラに存在** する。本資料は **行=ガイドライン × 列=13論点** のマトリクスで、各セルに *Must / Should / Mention / None* の **要求強度** と **80字要約 + 原文リンク + 節番号** を載せ、臨床導入レビュー、抄読会、倫理審査、院内AIポリシー作成で **原文確認の入口として引用** できる。無料 (CC-BY 4.0)、PR 更新、月1回 GitHub Action で原文 URL 差分検査。

---

## 2. ガバナンス不変条件

| # | 不変条件 | 実装ポイント |
|---|---------|------------|
| G1 | **法的助言ではない** | 全ページ冒頭・README・各セルに固定 disclaimer。セル末尾に「原文を必ず参照」 |
| G2 | **引用必須** | 各セル: 原文URL + 節/段落番号 + 取得日 + 信頼度 (high/medium/low) |
| G3 | **更新追跡可能** | 各ガイドライン YAML に `version`, `published_date`, `last_reviewed`, `source_hash` |
| G4 | **PR は引用付きセルのみ受理** | `.github/PULL_REQUEST_TEMPLATE.md` に強制 |
| G5 | **GuideScope corpus package 互換** | 独自 MCP server は作らず、`@cursorversinc/guidescope-medical-corpus` npm package として export し、GuideScope 本体に組み込む |
| G6 | **日本語 primary、英語併記可** | セル要約は日本語、原文タイトルは英語のまま |
| G7 | **CC-BY 4.0** (自作部分のみ) | LICENSE + 各ページ脚注。**第三者ガイドライン引用は各権利者に帰属、CC-BY 対象外** |
| G8 | **要求強度ルーブリック** | Must/Should/Mention は (a) 拘束力 (b) 対象主体明示 (c) 検証可能性 の 3 軸でスコア。判定基準は `docs/RUBRIC.md` |
| G9 | **空欄を 3 状態に分割** | `none` (該当ガイドラインで扱いなし) / `not_assessed` (本資料未評価) / `source_unavailable` (出典確認不可) |

### G5. GuideScope 組み込み方針

- GuideScope Phase 2 では、本リポジトリを独立 MCP server 化しない。
- 医療ドメインの corpus は `@cursorversinc/guidescope-medical-corpus` npm package として publish し、GuideScope 本体の既存 MCP / 検索 UI / citation pipeline に組み込む。
- 独自 MCP server を作らない理由:
  - GuideScope 本体と query / citation / ranking 実装を重複させない。
  - 別 server 運用、認証、監視、バージョン管理、障害対応の負担を増やさない。
  - Cursorvers Inc. の GuideScope ブランド配下の医療拡張 corpus として扱い、利用者に別プロダクトとして誤認させない。
- package 利用例:

```bash
npm install @cursorversinc/guidescope-medical-corpus
```

```ts
import { medicalGuidelines, medicalColumns } from "@cursorversinc/guidescope-medical-corpus";
import type { GuideScopeCitationCell } from "@cursorversinc/guidescope";

const cell = medicalGuidelines["fda-aiml-saamd-ap"].cells.G satisfies GuideScopeCitationCell;
```

- schema 互換性要件:
  - `guideline.id`, `column.id`, `cell.requirement`, `cell.summary_ja`, `cell.citation.url`, `cell.citation.section`, `cell.citation.retrieved`, `cell.citation.confidence` を安定 export する。
  - Cell schema は GuideScope の citation interface と互換でなければならない。
  - `none` / `not_assessed` / `source_unavailable` は GuideScope 側で引用なしセルとして安全に扱える enum とする。

---

## 3. スコープ

### IN
- 行 (ガイドライン): **TOP 5 で初版リリース** (Copilot 批判反映: 引用品質を担保できる現実的範囲)、月次で +5 拡張
  - **Pilot (v0.1)**: PMDA SaMD通知 / FDA AI/ML SaMD Action Plan + PCCP / EU AI Act / 厚労省 医療機器プログラム取扱い / WHO Ethics & Governance of AI for Health
  - **Wave 2 (v0.2)**: NIST AI RMF / ISO/IEC 42001 / IMDRF SaMD / 日本医学会連合 医療AI開発利用指針 / 経産省・総務省 AI事業者GL
  - **研究 (列で扱う)**: TRIPOD+AI / CONSORT-AI / SPIRIT-AI
- 列 (13論点): A 適用対象 / B リスク分類 / C 透明性 / D 監査ログ / E Human oversight / F データ品質・バイアス / G PCCP・市販後 / H 責任主体 / I 同意・プライバシー / J セキュリティ / K 臨床評価 / L 国際整合 / M ライフサイクル
- 価値可視化図: 「3レイヤー地図」(規制/研究/運用 × 開発前/検証/導入後)
- 配布: GitHub Pages (mkdocs-material) + GitHub Repo (markdown) + PDF 自動生成

### OUT
- 患者固有情報の扱い、診療判断
- 法的助言、規制適合性の保証
- SaMD製造者の承認申請支援、申請資料作成、規制当局相談の代行
- ガイドライン本文の機械翻訳・転載 (引用は短文のみ)
- ホスト型 SaaS (運営費ゼロ原則)

---

## 4. 配布

- **GitHub Repo**: `cursorvers/medical-ai-governance-crosswalk` (CC-BY-4.0)
- **Static site**: GitHub Pages (mkdocs-material theme)
- **GuideScope integration**: Phase 2 で `@cursorversinc/guidescope-medical-corpus` として publish し、GuideScope 本体へ corpus として組み込む
- **告知**: X (yu_sh02084 の波に乗せる) / note / Zenn / Qiita / Medical Tribune 寄稿打診

---

## 5. 技術スタック

| 層 | 選定 |
|---|------|
| コーパス | YAML (ガイドライン1本=1ファイル, `corpus/guidelines/<id>.yml`) |
| 列定義 | YAML (`corpus/columns/columns.yml`) |
| 静的サイト | mkdocs-material |
| ビルド | Python `scripts/build_site.py` (YAML → md → mkdocs) |
| GuideScope corpus package (Phase 2) | TypeScript / npm package export / GuideScope citation interface 互換 |
| CI | GitHub Actions: lint (yamllint) + build + Pages deploy + 月1 URL diff check |

---

## 6. ハイブリッド 8 スライス (Phase 1 = static, Phase 2 = GuideScope corpus package)

| Slice | 内容 | 完了条件 |
|-------|------|--------|
| S1 | 列定義 (13論点) YAML + 要求強度ルーブリック (`docs/RUBRIC.md`) | `corpus/columns/columns.yml` + RUBRIC.md |
| S2 | YAML schema 確定 + PMDA SaMD を完全執筆 (schema example) | `corpus/guidelines/pmda-samd.yml` |
| S3 | 残り 4 ガイドライン執筆 (Codex 並列 2 lane) | `corpus/guidelines/*.yml` × 5 (Pilot v0.1) |
| S4 | YAML → markdown / 3レイヤー地図生成 build script + validate | `scripts/build_site.py`, `scripts/validate_corpus.py` |
| S5 | mkdocs-material サイト構築 + 引用フォーマット + disclaimer | `site/` ビルド成功 |
| S6 | CI (yamllint + validate + build + monthly URL diff) | `.github/workflows/*.yml` |
| S7 | Codex code-review + Copilot 内容 review (≥7/10) + 修正 | 両 review pass |
| S8 | 配布素材 (Xスレッド原稿、note 下書き) + 最終 commit | 配布 ready、達成度レポート |

**Phase 2 (別 SPEC、後日)**: npm package `@cursorversinc/guidescope-medical-corpus`

- **想定総時間**: 並列込みで実 6〜10 時間 (Codex/Copilot 並列を最大化)
- **Phase 2 (GuideScope integration)** は S7 のみで雛形まで、本実装は別 SPEC

---

## 7. Acceptance Criteria

1. `corpus/guidelines/` に 10 本の YAML、各ファイルが schema validate を通る
2. `scripts/build_site.py` が site/ を生成、`mkdocs build` 成功
3. 全セルに原文 URL + 節/段落 + 取得日 + 信頼度 が記載される (扱いなしは `none` / 未評価は `not_assessed` / 出典不明は `source_unavailable` を明示)
4. README に disclaimer 冒頭、CC-BY-4.0、10分セットアップ、PR 受理基準
5. 価値可視化図 (3レイヤー地図) が site トップに表示
6. Codex code-review + Copilot review 両方 ≥7/10
7. README に GuideScope (本家) との関係明示、Phase 2 corpus package 化計画

## 8. Done Condition

- `~/Dev/medical-paper-governance/` に全ファイル commit
- 作業レポートに「目的達成度 %」「残スライス見積もり」明記
- GitHub remote push は **/vote 必須** (Phase B 範囲外)

---

## 9. 失敗モード / 停止条件

- ❌ Codex / Copilot 両方 3 連続 timeout → BLOCKED
- ❌ ガイドライン引用が原文と齟齬 → 該当セル "信頼度 low" にダウングレードして継続
- ❌ Cell schema が GuideScope citation interface と非互換 → Phase 2 package integration は別 SPEC で再設計、Phase 1 はそのまま完成

## 10. 承認境界 (/vote 必須)

- GitHub remote push (cursorvers org への push)
- npm publish (`@cursorversinc/guidescope-medical-corpus`)
- Medical Tribune など外部寄稿の送信
- 破壊的 Git 操作

---

## 11. 進捗 (現時点)

- **目的達成度**: 35% (v1 SPEC ピボット + v2 SPEC ロック + critique反映 + LICENSE/README/CONTRIBUTING/SCHEMA scaffold 完了)
- **残スライス**: 8 (S1〜S8、並列で実 5〜8h)
- **Critique scores**: Codex 7.5/10, Copilot 6.5/10 → 修正後 8/10 想定
- **使用 lane**: Codex (主)、Copilot (主)、GLM 429・Gemini cap・Cursor 破綻で除外
