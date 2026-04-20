# Maintenance

## Source Freshness Cron

`Source Freshness` GitHub Actions workflow は毎月 `0 6 1 * *` UTC に実行する。`corpus/guidelines/*.yml` の各 cell から `citation.url` を集め、15 秒 timeout で source を取得し、`state/source-freshness-report.json` を 90 日保持の workflow artifact として保存する。

machine-managed baseline は `state/source-freshness.json` に置く。baseline key は fetch 対象 URL で、URL fragment は除去する。同じ source を複数 cell が引用しても baseline を重複させないため。corpus YAML は editorial data として保ち、freshness state は corpus file の外へ分離する。

## Issue Triage

workflow が source drift を検出した場合、`corpus` と `auto-detected` label 付きの GitHub Issue を作る。Issue body の番号付き drift list を確認し、sample `curl` command で現在の source を取得する。hash や ETag だけで判断せず、必ず該当 section の本文が cell の判定に影響するか確認する。

各 drift item の処理手順:

1. 引用 section の本文変更が crosswalk cell に影響するか確認する。
2. cell が現在も妥当なら、PR で `state/source-freshness.json` の hash、ETag、Last-Modified、checked timestamp を更新する。
3. cell が古い場合は、同じ PR で該当 corpus cell を更新し、その後 baseline entry も更新する。
4. source が取得不可の場合は、現 citation を維持するか、公式代替 URL に差し替えるか、cell を適切な状態に変更するか判断する。

## Corpus Cell Update Flow

drift issue を起点に原文を手動確認し、PR を作成する。source freshness metadata は `state/source-freshness.json` に保持し、`corpus/guidelines/*.yml` に cell-level freshness hash を追加しない。merge 後、次回 monthly run は追加 drift がない限り静かに終了する。
