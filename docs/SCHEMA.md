# Guideline YAML Schema

各ガイドラインは `corpus/guidelines/<id>.yml` に 1 ファイルで保存。

## トップレベル

```yaml
id: pmda-samd                          # ファイル名と一致、英小文字+ハイフン
name_ja: PMDA SaMD通知
name_en: PMDA SaMD Notification
issuer: PMDA / 厚生労働省
jurisdiction: jp                       # jp / us / eu / international
type: regulatory                       # regulatory / ethical / reporting / standard
url: https://www.pmda.go.jp/...        # 原文URL (公式)
version: "2024.4"                      # ガイドライン側のバージョン
published_date: 2024-04-01
last_reviewed: 2026-04-20              # 本資料側のレビュー日
source_hash: sha256:...                # 原文取得時のhash (可能なら)
maintainer: cursorvers/medai
tags: [samd, jp, regulatory]

summary_ja: |
  120字程度のガイドライン要約。誰向け・何を規定するか・最新版年。

cells:                                  # 13論点ごとの記述
  - column: A                           # columns.yml の id
    requirement: must                   # must / should / mention / none
    summary_ja: 80字以内の要約
    citation:
      url: https://...                  # 該当節の URL (深リンク推奨)
      section: "第3章 2-1"               # 節/段落番号
      retrieved: 2026-04-20             # 取得日
      confidence: high                  # high / medium / low
    notes_ja: |
      補足 (任意、複数行可)。原文引用は短文のみ、CC-BY 範囲。

  - column: B
    requirement: should
    ...
```

## 必須フィールド

- `id`, `name_ja`, `issuer`, `jurisdiction`, `url`, `version`, `last_reviewed`, `summary_ja`
- `cells`: 13論点全てを列挙 (`none` でも記載)
- 各 cell の `column`, `requirement`, `summary_ja`, `citation.url`, `citation.section`, `citation.retrieved`, `citation.confidence`

## 信頼度 (confidence) の判定

- `high`: 原文の該当節を直接確認、直近6ヶ月以内に取得
- `medium`: 原文の概要や周辺記述から導出、6-18ヶ月前
- `low`: 二次資料経由、または原文URL が無効/節番号未確定

## バリデーション

`scripts/validate_corpus.py` で以下をチェック:
- schema 一致 (pydantic 等)
- 全 13 列が cells に存在
- citation.url が HTTP 200
- requirement が enum 4種のうち
- last_reviewed が 18ヶ月以内
