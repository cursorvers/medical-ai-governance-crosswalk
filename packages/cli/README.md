# @cursorversinc/medgov-cli

Terminal lookup for the **medical AI governance crosswalk** — 13 columns × 10 guidelines.

## Install

```bash
npx -y @cursorversinc/medgov-cli "IRB"
# or
npm i -g @cursorversinc/medgov-cli
medgov "IRB"
```

## Commands

```
medgov "<query>"             # color-coded text, grouped by column
medgov --json "<query>"      # JSON payload (pipe to jq)
medgov --list-columns
medgov --list-guidelines
medgov --help
```

## Color legend

| Strength  | Color      |
| --------- | ---------- |
| `must`    | red        |
| `should`  | yellow     |
| `mention` | gray       |
| `none`    | dim        |

## Example

```
$ medgov "IRB"

K — 倫理審査・同意 (IRB / consent)
  [must]    PMDA SaMD情報ページ
            倫理審査委員会の承認と患者同意を...
            https://www.pmda.go.jp/...
  [should]  NIST AIリスクマネジメントフレームワーク
            人間尊重原則の下でIRBレビューを推奨...
```

## JSON mode

```
$ medgov --json "透明性" | jq '.matches[0]'
{
  "column_id": "F",
  "column_name": "透明性",
  "cells": [ ... ]
}
```

## License

CC-BY-4.0
