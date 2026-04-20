import { mkdir, readdir, readFile, writeFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import yaml from "js-yaml";

const __filename = fileURLToPath(import.meta.url);
const packageRoot = path.resolve(path.dirname(__filename), "..");
const repoRoot = path.resolve(packageRoot, "../..");
const guidelinesDir = path.join(repoRoot, "corpus", "guidelines");
const srcDir = path.join(packageRoot, "src");
const distDir = path.join(packageRoot, "dist");

const EXPECTED_GUIDELINES = 10;
const EXPECTED_CELLS = 13;

function assertGuideline(value, fileName) {
  if (!value || typeof value !== "object") {
    throw new Error(`${fileName}: guideline YAML must be an object`);
  }

  for (const key of ["id", "name_ja", "name_en", "issuer", "jurisdiction", "type", "url", "cells"]) {
    if (!(key in value)) {
      throw new Error(`${fileName}: missing required key "${key}"`);
    }
  }

  if (!Array.isArray(value.cells)) {
    throw new Error(`${fileName}: cells must be an array`);
  }

  if (value.cells.length !== EXPECTED_CELLS) {
    throw new Error(`${fileName}: expected ${EXPECTED_CELLS} cells, found ${value.cells.length}`);
  }

  for (const cell of value.cells) {
    if (!cell.column || !cell.requirement || !cell.summary_ja || !cell.citation) {
      throw new Error(`${fileName}: each cell must include column, requirement, summary_ja, and citation`);
    }
  }
}

async function main() {
  const files = (await readdir(guidelinesDir))
    .filter((file) => file.endsWith(".yml") || file.endsWith(".yaml"))
    .sort();

  if (files.length !== EXPECTED_GUIDELINES) {
    throw new Error(`expected ${EXPECTED_GUIDELINES} guideline files, found ${files.length}`);
  }

  const guidelines = [];

  for (const file of files) {
    const filePath = path.join(guidelinesDir, file);
    const raw = await readFile(filePath, "utf8");
    const guideline = yaml.load(raw, { schema: yaml.JSON_SCHEMA });
    assertGuideline(guideline, file);
    guidelines.push(guideline);
  }

  const corpus = {
    schema_version: "0.1.0",
    generated_at: new Date().toISOString(),
    source: "medical-paper-governance/corpus/guidelines/*.yml",
    guideline_count: guidelines.length,
    guidelines
  };

  const json = `${JSON.stringify(corpus, null, 2)}
`;

  await mkdir(srcDir, { recursive: true });
  await mkdir(distDir, { recursive: true });
  await writeFile(path.join(srcDir, "corpus.json"), json, "utf8");
  await writeFile(path.join(distDir, "corpus.json"), json, "utf8");
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
