#!/usr/bin/env python3
"""Build the static clinical lookup index for the MkDocs site."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_COLUMNS = tuple("ABCDEFGHIJKLM")
DEFAULT_OUTPUT = ROOT / "site" / "docs" / "assets" / "lookup-index.json"


def load_yaml(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def load_columns() -> dict[str, dict[str, Any]]:
    doc = load_yaml(ROOT / "corpus" / "columns" / "columns.yml") or {}
    columns = doc.get("columns", [])
    by_id = {column.get("id"): column for column in columns if isinstance(column, dict)}
    missing = [column_id for column_id in EXPECTED_COLUMNS if column_id not in by_id]
    if missing:
        raise ValueError(f"missing column definitions: {missing}")
    return {column_id: by_id[column_id] for column_id in EXPECTED_COLUMNS}


def load_guidelines() -> list[dict[str, Any]]:
    guidelines: list[dict[str, Any]] = []
    for path in sorted((ROOT / "corpus" / "guidelines").glob("*.yml")):
        doc = load_yaml(path)
        if not isinstance(doc, dict):
            raise ValueError(f"{path}: guideline YAML must be a mapping")
        cells = doc.get("cells", [])
        if not isinstance(cells, list):
            raise ValueError(f"{path}: cells must be a list")
        doc["_cells_by_column"] = {cell["column"]: cell for cell in cells}
        guidelines.append(doc)
    if len(guidelines) != 10:
        raise ValueError(f"expected 10 guideline files, found {len(guidelines)}")
    return guidelines


def build_keywords() -> dict[str, list[str]]:
    doc = load_yaml(ROOT / "corpus" / "lookup-map.yml") or {}
    keywords: dict[str, list[str]] = {}
    for index, mapping in enumerate(doc.get("mappings", [])):
        column = mapping.get("column")
        if column not in EXPECTED_COLUMNS:
            raise ValueError(f"lookup-map.yml mappings[{index}]: invalid column {column!r}")
        values = mapping.get("keywords", [])
        if not isinstance(values, list) or not values:
            raise ValueError(f"lookup-map.yml mappings[{index}]: keywords must be a non-empty list")
        for keyword in values:
            if not isinstance(keyword, str) or not keyword.strip():
                raise ValueError(f"lookup-map.yml mappings[{index}]: invalid keyword {keyword!r}")
            columns = keywords.setdefault(keyword.strip(), [])
            if column not in columns:
                columns.append(column)
    mapped_columns = {column for columns in keywords.values() for column in columns}
    missing = [column for column in EXPECTED_COLUMNS if column not in mapped_columns]
    if missing:
        raise ValueError(f"lookup-map.yml does not cover columns: {missing}")
    return keywords


def build_lookup_index(output_path: Path = DEFAULT_OUTPUT) -> dict[str, Any]:
    column_defs = load_columns()
    guidelines = load_guidelines()
    index: dict[str, Any] = {"columns": {}, "keywords": build_keywords()}

    for column_id, column in column_defs.items():
        cells: list[dict[str, str]] = []
        for guideline in guidelines:
            cell = guideline["_cells_by_column"].get(column_id)
            if cell is None:
                raise ValueError(f"{guideline['id']}: missing cell for column {column_id}")
            citation = cell.get("citation", {})
            cells.append(
                {
                    "guideline": guideline["name_ja"],
                    "guideline_id": guideline["id"],
                    "strength": cell.get("requirement", ""),
                    "summary": cell.get("summary_ja", ""),
                    "citation_url": citation.get("url", ""),
                    "confidence": citation.get("confidence", "low"),
                }
            )
        if len(cells) != 10:
            raise ValueError(f"column {column_id}: expected 10 cells, found {len(cells)}")
        index["columns"][column_id] = {
            "name": column.get("name_ja", column_id),
            "name_en": column.get("name_en", ""),
            "cells": cells,
        }

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(index, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return index


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    index = build_lookup_index(args.output)
    cell_count = sum(len(column["cells"]) for column in index["columns"].values())
    print(f"lookup index generated: {args.output} ({len(index['columns'])} columns, {cell_count} cells)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
