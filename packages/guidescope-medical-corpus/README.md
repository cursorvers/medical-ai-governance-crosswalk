# @cursorversinc/guidescope-medical-corpus

Medical AI governance crosswalk corpus for GuideScope-compatible consumers.

The package exports the `medical-paper-governance` guideline corpus as typed JavaScript objects. The current corpus covers 10 guideline sources across 13 governance columns.

## Install

```sh
npm install @cursorversinc/guidescope-medical-corpus
```

## Usage

```ts
import { guidelines } from "@cursorversinc/guidescope-medical-corpus";

for (const guideline of guidelines) {
  console.log(guideline.id, guideline.name_en, guideline.cells.length);
}
```

You can also import the TypeScript types:

```ts
import type { Guideline, Cell, Citation } from "@cursorversinc/guidescope-medical-corpus";
```

## Build From Source

```sh
npm install
npm run build
```

The build reads `../../corpus/guidelines/*.yml`, writes `dist/corpus.json`, and compiles `dist/index.js` plus `dist/index.d.ts`.

## License And Attribution

This package is licensed under Creative Commons Attribution 4.0 International (CC BY 4.0).

Attribution: Copyright (c) 2026 Cursorvers Inc.

The CC-BY 4.0 license applies only to the original compilation, summarization, structure, and commentary authored by Cursorvers Inc. Third-party guideline texts and source documents remain the property of their respective rights holders.

## Disclaimer

This package is a reference corpus of publicly available medical AI governance materials. It is not legal advice, regulatory compliance certification, clinical guidance, or medical advice. The original source documents always take precedence. Consult qualified legal, regulatory, clinical, and business professionals before making decisions based on this corpus.
