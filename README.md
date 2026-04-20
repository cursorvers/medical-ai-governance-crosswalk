# Medical AI Governance Crosswalk (医療AIガバナンス横串帳)

> **DISCLAIMER**: 本資料および Evidence Pack は診断・治療・承認申請の根拠として単独使用できません。公開ガイドラインへの入口となる引用付き対照表・作業テンプレートであり、法的助言・規制適合性の保証・診療判断ではありません。Evidence Pack の選択、記入、転記、提出判断、最終提出物の品質管理は利用者側の責任です。最終判断は必ず原文を参照し、必要に応じて有資格者・規制専門家・倫理審査担当者のレビューを受けてください。

本プロジェクトは **医療AIを「使う側」** (臨床医 / 臨床研究者 / 医療機関 IT・医療安全部門 / IRB事務局) を対象とします。SaMD製造者の承認申請支援は **Out of scope** です。

医療AI の導入・研究・説明・院内運用に関わる人が、規制 / 倫理 / 研究報告 / プライバシーの論点を **read-order map / 入口となる引用付き対照表** として確認するための資料です。

## できること

- AI製品の臨床導入可否を評価する
- IRB / 倫理審査の質問リストを即発行する
- 患者へのAI介入説明文テンプレートを作る
- 病院AI導入ポリシー骨子を作る

## 構成

- **行**: 主要ガイドライン (PMDA / FDA / EU AI Act / WHO / NIST / ISO 42001 / IMDRF / 厚労省 / 日本医学会連合 / 経産省 ほか)
- **列**: 13論点 (適用対象 / リスク / 透明性 / 監査 / Human oversight / データ品質 / バイアス / PCCP / 責任 / 同意 / セキュリティ / 臨床評価 / ライフサイクル)
- **セル**: 要求強度 (`Must` / `Should` / `Mention` / `None`) + 80字要約 + 原文URL + 節/段落番号 + 取得日 + 信頼度

## なぜこれが必要か

- 臨床医: 導入候補AIの透明性、監査、人間監督、患者説明、導入後モニタリングの論点を原文確認の入口として整理できます。
- 臨床研究者: AIを用いる研究計画について、同意、プライバシー、バイアス、Human oversight の確認質問を作れます。
- 医療機関 IT・医療安全部門: AI導入時の審査、記録、セキュリティ、有害事象報告、変更管理を院内ポリシーに落とし込めます。
- IRB事務局・倫理審査委員: どの指針のどこを確認すべきかを各原文への入口として確認できます。

## 使い方

1. [GitHub Pages](https://cursorvers.github.io/medical-ai-governance-crosswalk/) を開く (構築中)
2. ガイドライン名 or 論点名で検索
3. セルをクリック → 各原文への入口へ移動。最終判断は必ず原文を参照

外来の合間に確認したい場合は、トップページ冒頭の検索ボックスに日本語で質問を入れると、該当コラムの10ガイドラインセルが即表示されます。LLMや外部APIは使わず、静的に生成したキーワード対応表と引用付きセルだけを表示します。

## Evidence Pack の使い方

Evidence Pack は、crosswalk の引用付きセルを臨床導入評価、患者説明、院内ポリシー、倫理審査前チェック、変更管理レビューに使いやすい Markdown テンプレートへ束ねる補助資料です。テンプレートは入口であり、最終判断は所属機関の規程と専門家レビューを通してください。

| Template | 位置づけ | 想定ユースケース |
|----------|----------|----------------|
| `clinical-ai-product-evaluation` | 中心 | 臨床医・診療科責任者・院内AI導入審査担当者が、AI製品の適応、リスク、透明性、データ保護、運用責任を導入前に確認する |
| `patient-explanation-support` | 中心 | 医師・臨床研究者が、AI利用、利益と限界、代替手段、拒否・撤回、データ利用の患者説明文を整理する |
| `hospital-ai-policy-skeleton` | 中心 | 医療安全部門・情報システム部門・IRB事務局が、AI導入審査、継続モニタリング、有害事象報告、教育、変更管理を院内規程化する |
| `irb-question-checklist` | 中心 | 臨床研究者・IRB事務局・倫理審査委員が、透明性、同意、プライバシー、バイアス、Human oversight の質問項目を洗い出す |
| `pccp-skeleton` | 補助 | 医療機関側の変更管理レビューとして、AI製品の予定変更、影響評価、検証計画を確認する |
| `samd-consultation-prep` | archived | SaMD製造者のPMDA事前相談向け旧テンプレート。default 生成・自動配信から除外し、明示指定時のみ生成可能 |

生成コマンド例:

```bash
# default: clinical-ai-product-evaluation / patient-explanation-support /
# hospital-ai-policy-skeleton / irb-question-checklist / pccp-skeleton の5本を生成
.venv/bin/python scripts/generate_evidence_pack.py

# archived template は明示指定時のみ生成
.venv/bin/python scripts/generate_evidence_pack.py --template samd-consultation-prep
```

GitHub Pages では Evidence ページから各 Markdown をダウンロードします。ページ本体は `site/docs/evidence.md` として生成され、公開後は `https://cursorvers.github.io/medical-ai-governance-crosswalk/evidence/` 配下のファイルへリンクします。ローカルでは `build/evidence/<template>.md` を確認してください。

免責: Evidence Pack は公開ガイドライン確認の入口です。医療機関、倫理審査委員会、研究機関、製品ベンダーごとの要求を満たす保証はありません。テンプレートの採否、記入内容、添付資料、最終判断は利用者が責任を持ち、必要に応じて法務・薬事・臨床・倫理審査の専門家レビューを受けてください。

## 10分セットアップ

```bash
git clone https://github.com/cursorvers/medical-ai-governance-crosswalk.git
cd medical-ai-governance-crosswalk
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python scripts/validate_corpus.py          # YAML schema 検証
.venv/bin/python scripts/build_site.py               # site/docs + site/public 生成
.venv/bin/python -m mkdocs build --strict            # 厳密 build 確認
.venv/bin/mkdocs serve                               # http://localhost:8000
```

## ライセンス・引用

- License: [CC BY 4.0](LICENSE)
- 引用例: `Cursorvers Inc. (2026). Medical AI Governance Crosswalk. https://github.com/cursorvers/medical-ai-governance-crosswalk`

## コントリビュート

- セル更新 PR は **原文URL + 節/段落番号 + 取得日 + 信頼度** が必須 ([CONTRIBUTING.md](CONTRIBUTING.md))
- ガイドライン追加リクエストは Issue で

## ロードマップ

- Phase 1 (本リポ): 静的サイト + TOP 10 ガイドライン + 使う側向け Evidence Pack
- Phase 2: npm package `@cursorversinc/guidescope-medical-corpus` として publish し、GuideScope 本体へ医療 corpus として組み込み

## 関連プロダクト

- [GuideScope MCP](https://cursorvers.jp/tools/guidescope/) — 生成AI国内ガイドライン検索 (Cursorvers 本家プロダクト)
- 本資料は GuideScope の **医療ドメイン拡張コーパス** として将来統合予定。独自 MCP server は作らず、GuideScope 本体の検索・citation interface と互換な corpus package として連携します。
