# Provenance Rounds — Spec (Phase A locked)

**Run ID**: 2026-04-20-medgov-provenance-rounds
**Status**: DRAFT (awaiting user approval before Phase B)
**Origin**: FUGUE multi-agent brainstorm (Codex 9/10, Copilot 8.5/10, Cursor broken)

---

## 1. Product

- **Name**: `Provenance Rounds` (命名: Codex lane 採用、院内抄読会 × 証跡 Ledger の二重意味)
- **短縮形**: `prov-rounds`
- **一言定義**: 院内抄読会の下読み資料を、**文単位の出典付き + 監査可能ログ付き** で毎朝届ける無料 OSS。
- **ピッチ** (医師向け):
  > 毎朝 7:00、PubMed から過去 7 日の注目論文 5 本を Word/Markdown で届けます。違うのは「各要約文が Abstract のどこに由来するか」が明記されること、ハルシネーションが自動隔離されること、使ったモデル・プロンプトの改ざん不可能な監査ログが添付されることです。Forkして API Key 2 個を登録するだけ。運営費ゼロ、診断・治療推奨は一切しません。

---

## 2. ガバナンス不変条件 (絶対守る)

| # | 不変条件 | 実装ポイント |
|---|---------|------------|
| G1 | **医師法・薬機法スコープ外** を維持。診断・治療推奨を行わない | 出力テンプレ先頭に固定 Disclaimer、プロンプトで "treatment recommendation 禁止" を制約 |
| G2 | **PHI 混入防止** | 入力は PubMed 由来に固定。ユーザー自由入力フィールド禁止 (設計上存在しない) |
| G3 | **文単位 provenance** | 要約の各文に `PMID:Abstract-Methods-S2` 形式アンカー必須。根拠なし文は出力しない (隔離) |
| G4 | **Reproducibility** | model/prompt-hash/temperature/input-PMIDs/output-hash を JSONL ログに記録、Word 末尾にも短縮表示 |
| G5 | **Tamper-evident** | SHA-256 hash chain。前レコード hash を次レコードに含む append-only ledger |
| G6 | **撤回論文フィルタ** | PubMed RetractionIn / RetractedPublication を fetch 時に除外 |
| G7 | **COI / Ethics ラベル** | funding / COI / IRB 語句を機械可読フィールドとして抽出、Word に明示表示 |
| G8 | **Claude/ChatGPT 非依存** | LLM プロバイダは Gemini 無料枠 primary、Groq fallback、Ollama (opt-in) |

---

## 3. スコープ (IN / OUT)

### IN
- PubMed E-utilities での論文取得
- 事前定義された MeSH / ジャーナル / キーワードの検索クエリテンプレ
- LLM による要約 (Abstract を入力とし、Abstract に含まれる文のみを根拠に要約)
- GitHub Actions cron (毎朝 UTC 22:00 = JST 07:00)
- 配信: Gmail (primary, 既存ユーザー資産活用) / ローカルファイル保存
- 出力: Markdown (primary) + Word (docx) (院内共有用)

### OUT
- 全文 PDF 取得・解析 (copyright + scope の両面で OUT)
- ユーザー自由プロンプト入力 (PHI 混入リスク、OUT)
- 診断・治療・投与量の推奨 (医師法スコープ、OUT)
- 患者固有情報の扱い (OUT)
- Web UI Hosted 版 (運営費リスクのため本 SPEC では OUT。将来拡張候補)

---

## 4. 配布

- **GitHub Template Repo** (MIT License)
- セットアップ: Fork → Secrets 2 個 (`GEMINI_API_KEY`, `GMAIL_APP_PASSWORD`) → Actions 有効化のみ
- 目標: セットアップ完了まで 10 分以内 (README で step-by-step)

---

## 5. 技術スタック

| 層 | 選定 | 代替 |
|---|------|-----|
| 言語 | Python 3.11+ | — |
| LLM primary | Google Gemini 2.5 Flash-Lite (free tier) | — |
| LLM fallback | Groq `llama-3.1-8b-instant` (free) | Ollama (local, opt-in flag) |
| LLM governance-check | Gemini low-temp 2nd pass + OSS NLI (optional) | — |
| PubMed | E-utilities (efetch + esearch, XML) | — |
| Word 生成 | `python-docx` | — |
| Hash chain | `hashlib.sha256`, JSONL | — |
| Secrets | GitHub Actions Secrets | — |
| CI | GitHub Actions | — |
| Test | `pytest` + `pytest-recording` (VCR) for PubMed | — |

**依存最小化**: requests, python-docx, google-generativeai, groq, lxml, pydantic, pyyaml のみ。

---

## 6. 8-スライス実装ロードマップ

| Slice | 内容 | 主担当 | 完了条件 |
|-------|------|--------|--------|
| S1 | Project scaffold + MIT License + Disclaimer + README + CI lint | Codex | `pytest` / `ruff` が走る、README に Disclaimer 冒頭 |
| S2 | PubMed fetch + 撤回フィルタ + scoring + PMID 正規化 | Codex | VCR でテストが通る、撤回論文除外の unit test |
| S3 | Abstract section/sentence decomposer + provenance ID 発番 | Codex | Methods/Results/Conclusions 分割の unit test |
| S4 | Multi-LLM provider 抽象化 + Reproducibility block emitter | Copilot | Gemini/Groq/Ollama の 3 provider テスト |
| S5 | Sentence-level citation + evidence-less 隔離 + governance-check gate | Codex | 根拠なし文が "quarantined" マークで出力される |
| S6 | Tamper-evident hash-chain JSONL audit log | Copilot | 改ざん検知テスト (ハッシュ不整合で fail) |
| S7 | Output renderer (Markdown + Word) + Disclaimer header + COI/retraction表示 | Codex | サンプル入力で Word/MD が生成、Disclaimer 先頭固定 |
| S8 | GitHub Actions workflow + 配信 (Gmail/local) + setup wizard + 統合テスト + security review | Copilot+GLM | E2E dry-run 成功、code review ≥7/10 |

- **1 slice ≒ 1〜2 時間の Codex/Copilot 並列実行**
- **想定総実装時間**: 実作業 8〜16 時間 (並列化で実 4〜8 時間)

---

## 7. Acceptance Criteria (Phase B 完了条件)

1. `make test` が全 unit テスト pass
2. `make demo` でサンプル PMIDs (固定 5 本) から Word + Markdown + audit.jsonl が生成される
3. Word 先頭に Disclaimer 固定表示、本文の各要約文に provenance ID が付与
4. audit.jsonl の hash chain が `scripts/verify-chain.py` で検証成功
5. Gemini を GROQ に切替えても同じインタフェースで動作 (provider 抽象化テスト)
6. README に 10-minute-setup ガイド、Disclaimer、ライセンス、 サポート範囲 (≠ 診療判断) が明記
7. GitHub Actions workflow が cron で起動可能な状態 (push 先で有効化待ち)
8. Codex code-review + GLM general-review 両方が ≥7/10 ( Claude は判定に関与しない )

## 8. Done Condition

- `~/Dev/medical-paper-governance/` に全ファイル commit 済み (ローカル)
- 作業レポートに「目的達成度 100%」「8 slice 消化」を記載
- GitHub org への push は **/vote 承認後に別途実施** (Phase B 本体には含めない)

---

## 9. 失敗モード / 停止条件

- ❌ Codex / Copilot 両方が 3 回連続で 429/タイムアウト → BLOCKED 通知
- ❌ GLM code-review が <7/10 → 修正ループ (最大 2 回、超えたら BLOCKED)
- ❌ security-analyst の REJECT → 即 STOP、ユーザー通知
- ❌ PHI 混入設計が破綻 → G2 は hard invariant、違反検知で即 STOP

## 10. 承認境界 (/vote 必須)

- GitHub remote への push (repo 作成含む)
- Gmail 等外部送信の live test
- 破壊的 Git 操作

これらは **Phase B の範囲外**、完了後にユーザーと /vote で相談。

---

## 11. 進捗レポート (現時点)

- **目的達成度**: 15% (ブレスト + 批判的吟味 + SPEC draft 完了)
- **残スライス見積もり**: 8 slice (S1〜S8)
- **ブレスト参加 lane**: Codex (成功, 9/10), Copilot (成功, 8.5/10), Cursor (破綻: `@anysphere/file-service-darwin-x64` module 不在)
- **rate-limit state**: Claude 余裕あり、GLM 429、Gemini 月額 cap 超過 — Phase B 実装は Codex + Copilot 並列で回す
