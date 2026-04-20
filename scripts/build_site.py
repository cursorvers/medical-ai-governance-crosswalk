#!/usr/bin/env python3
from __future__ import annotations

import html
import shutil
import sys
from pathlib import Path
from typing import Any

import yaml
from jinja2 import Environment, StrictUndefined

from build_lookup_index import build_lookup_index
from generate_evidence_pack import (
    DEFAULT_TEMPLATES,
    SUPPORTED_TEMPLATES,
    copy_evidence_to_site_public,
    generate_all_evidence_packs,
)

ROOT = Path(__file__).resolve().parents[1]
SITE_DIR = ROOT / "site"
DOCS_DIR = SITE_DIR / "docs"
ASSET_SOURCE_DIR = ROOT / "assets"
DOCS_ASSETS_DIR = DOCS_DIR / "assets"
PUBLIC_ASSETS_DIR = SITE_DIR / "public" / "assets"
DISCLAIMER = (
    "本資料は公開ガイドラインの参照用コンパイルです。法的助言、規制適合性の保証、"
    "診療判断ではありません。利用前に必ず原文を参照してください。"
)
LICENSE_FOOTER = """---

**License / 引用スコープ**: 本サイトのオリジナル編集物 (マトリクス構造・要求強度判定・列定義・要約) は CC-BY 4.0。第三者ガイドライン原文の引用は各権利者帰属 (fair use / 著作権法第32条「引用」の範囲) で、CC-BY 対象外。詳細は [LICENSE](https://github.com/cursorvers/medical-ai-governance-crosswalk/blob/main/LICENSE) 参照。"""
REQ_ICON = {
    "must": "🔴",
    "should": "🟠",
    "mention": "🔵",
    "none": "⚪",
    "not_assessed": "❔",
    "source_unavailable": "⚫",
}
REQ_LABEL = {
    "must": "must",
    "should": "should",
    "mention": "mention",
    "none": "none",
    "not_assessed": "not_assessed",
    "source_unavailable": "source_unavailable",
}


def load_yaml(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def md_escape(value: Any) -> str:
    text = "" if value is None else str(value)
    return html.escape(text).replace("|", "\\|")


def citation_link(cell: dict[str, Any]) -> str:
    citation = cell.get("citation", {})
    url = citation.get("url", "")
    section = citation.get("section", "source")
    confidence = citation.get("confidence", "unknown")
    return f"[{md_escape(section)} / {md_escape(confidence)}]({url})"


def load_corpus() -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    columns_doc = load_yaml(ROOT / "corpus" / "columns" / "columns.yml") or {}
    columns = columns_doc.get("columns", [])
    if not isinstance(columns, list) or len(columns) != 13:
        raise ValueError("corpus/columns/columns.yml must define 13 columns")
    default_layers = {
        "A": "regulatory",
        "B": "regulatory",
        "C": "operations",
        "D": "operations",
        "E": "operations",
        "F": "research",
        "G": "lifecycle",
        "H": "regulatory",
        "I": "operations",
        "J": "operations",
        "K": "research",
        "L": "regulatory",
        "M": "lifecycle",
    }
    for column in columns:
        column.setdefault("layer", default_layers.get(column.get("id"), "operations"))

    guidelines: list[dict[str, Any]] = []
    for path in sorted((ROOT / "corpus" / "guidelines").glob("*.yml")):
        doc = load_yaml(path)
        if not isinstance(doc, dict):
            raise ValueError(f"{path}: guideline YAML must be a mapping")
        doc["_path"] = path
        doc["_cells_by_column"] = {cell["column"]: cell for cell in doc.get("cells", [])}
        guidelines.append(doc)
    if not guidelines:
        raise ValueError("no guidelines found in corpus/guidelines")
    return columns, guidelines


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def with_license_footer(content: str) -> str:
    return content.rstrip() + "\n\n" + LICENSE_FOOTER


def copy_lookup_assets() -> None:
    DOCS_ASSETS_DIR.mkdir(parents=True, exist_ok=True)
    PUBLIC_ASSETS_DIR.mkdir(parents=True, exist_ok=True)
    for name in ("lookup.js", "lookup.css"):
        source = ASSET_SOURCE_DIR / name
        if not source.exists():
            raise FileNotFoundError(f"missing lookup asset: {source}")
        shutil.copy2(source, DOCS_ASSETS_DIR / name)
        shutil.copy2(source, PUBLIC_ASSETS_DIR / name)


def generate_lookup_index_assets() -> None:
    index = build_lookup_index(DOCS_ASSETS_DIR / "lookup-index.json")
    shutil.copy2(DOCS_ASSETS_DIR / "lookup-index.json", PUBLIC_ASSETS_DIR / "lookup-index.json")
    cell_count = sum(len(column["cells"]) for column in index["columns"].values())
    if len(index["columns"]) != 13 or cell_count != 130:
        raise ValueError(f"lookup index must contain 13 columns and 130 cells, got {len(index['columns'])} columns and {cell_count} cells")


def render_site(columns: list[dict[str, Any]], guidelines: list[dict[str, Any]]) -> None:
    if DOCS_DIR.exists():
        shutil.rmtree(DOCS_DIR)
    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    (DOCS_DIR / "guidelines").mkdir(parents=True, exist_ok=True)

    env = Environment(undefined=StrictUndefined, autoescape=False, trim_blocks=True)
    env.filters["md"] = md_escape
    env.globals.update(
        citation_link=citation_link,
        req_icon=REQ_ICON,
        req_label=REQ_LABEL,
        disclaimer=DISCLAIMER,
    )

    index_t = env.from_string(
        """# Medical AI Governance Crosswalk

> **DISCLAIMER**: {{ disclaimer }}

<div id="gl-lookup">
  <input type="text" id="gl-query" placeholder="例: IRBで何を聞かれる?" aria-label="ガイドライン論点検索">
  <div id="gl-results"></div>
</div>
<script src="assets/lookup.js"></script>

## 3レイヤー地図

| レイヤー | 論点 |
|---|---|
| 規制・責任 | {% for c in columns if c.layer == "regulatory" %}{{ c.id }} {{ c.name_ja }}{% if not loop.last %}<br>{% endif %}{% endfor %} |
| 研究・評価 | {% for c in columns if c.layer == "research" %}{{ c.id }} {{ c.name_ja }}{% if not loop.last %}<br>{% endif %}{% endfor %} |
| 運用・ライフサイクル | {% for c in columns if c.layer in ["operations", "lifecycle"] %}{{ c.id }} {{ c.name_ja }}{% if not loop.last %}<br>{% endif %}{% endfor %} |

## 概要

臨床医・臨床研究者・医療機関 (医療安全/IT/IRB事務局) が、主要ガイドラインを13論点で横断確認するための引用付き資料です。SaMD製造者の承認申請支援は対象外です。

## 収録ガイドライン

{% for g in guidelines -%}
- [{{ g.name_ja }}](guidelines/{{ g.id }}.md) ({{ g.issuer }})
{% endfor %}

## 読み方

- `must`: 明示的な要求または強い義務
- `should`: 推奨、原則、実施すべき事項
- `mention`: 言及あり
- `none`: 扱いなし
- `not_assessed`: 未評価
- `source_unavailable`: 出典確認不可
"""
    )
    write(
        DOCS_DIR / "index.md",
        with_license_footer(index_t.render(columns=columns, guidelines=guidelines)),
    )

    matrix_lines = [
        "# 13列マトリクス",
        "",
        f"> **DISCLAIMER**: {DISCLAIMER}",
        "",
        "| ガイドライン | " + " | ".join(f"{c['id']} {c['name_ja']}" for c in columns) + " |",
        "|" + "---|" * (len(columns) + 1),
    ]
    for guideline in guidelines:
        row_cells = []
        for column in columns:
            cell = guideline["_cells_by_column"][column["id"]]
            row_cells.append(
                f"{REQ_ICON[cell['requirement']]} {md_escape(cell['summary_ja'])}"
                f"<br>{citation_link(cell)}"
            )
        matrix_lines.append(
            f"| [{md_escape(guideline['name_ja'])}](guidelines/{guideline['id']}.md) | "
            + " | ".join(row_cells)
            + " |"
        )
    write(DOCS_DIR / "matrix.md", with_license_footer("\n".join(matrix_lines)))

    columns_t = env.from_string(
        """# 13列の定義

> **DISCLAIMER**: {{ disclaimer }}

| ID | 論点 | English | レイヤー | 定義 |
|---|---|---|---|---|
{% for c in columns -%}
| {{ c.id }} | {{ c.name_ja }} | {{ c.name_en }} | {{ c.layer }} | {{ c.description_ja }} |
{% endfor %}
"""
    )
    write(DOCS_DIR / "columns.md", with_license_footer(columns_t.render(columns=columns)))

    guideline_t = env.from_string(
        """# {{ g.name_ja }}

> **DISCLAIMER**: {{ disclaimer }}

| 項目 | 値 |
|---|---|
| ID | `{{ g.id }}` |
| English | {{ g.get("name_en", "") }} |
| 発行主体 | {{ g.issuer }} |
| 管轄 | {{ g.jurisdiction }} |
| 種別 | {{ g.get("type", "") }} |
| Version | {{ g.version }} |
| Published | {{ g.published_date }} |
| Last reviewed | {{ g.last_reviewed }} |
| Source | [official source]({{ g.url }}) |

## Summary

{{ g.summary_ja }}

## Cells

| 列 | 要求 | 要約 | Citation |
|---|---|---|---|
{% for c in columns -%}
{%- set cell = g._cells_by_column[c.id] -%}
| {{ c.id }} {{ c.name_ja }} | {{ req_icon[cell.requirement] }} `{{ cell.requirement }}` | {{ cell.summary_ja | md }} | {{ citation_link(cell) }} |
{% endfor %}

## Notes

{% for c in columns -%}
{%- set cell = g._cells_by_column[c.id] -%}
{% if cell.get("notes_ja") %}
### {{ c.id }} {{ c.name_ja }}

{{ cell.get("notes_ja") }}
{% endif %}
{% endfor %}
"""
    )
    for guideline in guidelines:
        write(
            DOCS_DIR / "guidelines" / f"{guideline['id']}.md",
            with_license_footer(guideline_t.render(g=guideline, columns=columns)),
        )

    guidelines_index_t = env.from_string(
        """# ガイドライン一覧

> **DISCLAIMER**: {{ disclaimer }}

| ガイドライン | 発行主体 | 管轄 | 種別 | Last reviewed |
|---|---|---|---|---|
{% for g in guidelines -%}
| [{{ g.name_ja }}]({{ g.id }}.md) | {{ g.issuer }} | {{ g.jurisdiction }} | {{ g.get("type", "") }} | {{ g.last_reviewed }} |
{% endfor %}
"""
    )
    write(
        DOCS_DIR / "guidelines" / "index.md",
        with_license_footer(guidelines_index_t.render(guidelines=guidelines)),
    )

    evidence_packs = []
    for template_name in DEFAULT_TEMPLATES:
        spec = SUPPORTED_TEMPLATES[template_name]
        output_filename = spec["output_filename"]
        evidence_packs.append(
            {
                "template_name": template_name,
                "title_ja": spec["title_ja"],
                "audience_ja": spec["audience_ja"],
                "use_case_ja": spec["use_case_ja"],
                "url": f"https://cursorvers.github.io/medical-ai-governance-crosswalk/evidence/{output_filename}",
                "repo_path": f"build/evidence/{output_filename}",
            }
        )

    evidence_t = env.from_string(
        """# Evidence Pack

> **DISCLAIMER**: {{ disclaimer }}

臨床医・臨床研究者・医療機関 (医療安全/IT/IRB事務局) 向けに、公開ガイドライン要点を集約した作業テンプレートです。SaMD製造者の承認申請支援は対象外です。

## ダウンロード

{% for pack in evidence_packs -%}
- [{{ pack.title_ja }}]({{ pack.url }})  
  **想定利用者**: {{ pack.audience_ja }}  
  **用途**: {{ pack.use_case_ja }}
{% endfor %}
## リポジトリ内生成先

{% for pack in evidence_packs -%}
- `{{ pack.repo_path }}`
{% endfor %}
## 使い方

1. 対象テンプレートを選ぶ。
2. 製品導入、研究計画、患者説明、院内ポリシー、変更管理の該当欄に現状と不明点を書く。
3. 表中の PMDA/FDA/EU/WHO/NIST/JMSF/ISO 原文リンクで根拠を確認する。

## 注意

本ページおよび evidence pack は公開ガイドラインの参照用コンパイルであり、法的助言、規制適合性の保証、診療判断ではありません。最終判断は必ず所属機関の規程、製品文書、倫理審査手順、原文ガイドラインを参照してください。
"""
    )
    write(DOCS_DIR / "evidence.md", with_license_footer(evidence_t.render(evidence_packs=evidence_packs)))

    generate_all_evidence_packs()
    copy_evidence_to_site_public()
    copy_lookup_assets()
    generate_lookup_index_assets()

    mkdocs_yml = {
        "site_name": "Medical AI Governance Crosswalk",
        "docs_dir": "docs",
        "site_dir": "public",
        "site_url": "https://cursorvers.github.io/medical-ai-governance-crosswalk/",
        "theme": {"name": "material", "language": "ja"},
        "plugins": ["search"],
        "extra_css": ["assets/lookup.css"],
        "hooks": ["../scripts/mkdocs_hooks.py"],
        "nav": [
            {"Home": "index.md"},
            {"Matrix": "matrix.md"},
            {"Evidence": "evidence.md"},
            {"Columns": "columns.md"},
            {
                "Guidelines": [
                    {g["name_ja"]: f"guidelines/{g['id']}.md"} for g in guidelines
                ]
            },
        ],
    }
    write(SITE_DIR / "mkdocs.yml", yaml.safe_dump(mkdocs_yml, sort_keys=False, allow_unicode=True))


def main() -> int:
    try:
        columns, guidelines = load_corpus()
        for guideline in guidelines:
            missing = [c["id"] for c in columns if c["id"] not in guideline["_cells_by_column"]]
            if missing:
                raise ValueError(f"{guideline['id']}: missing cells for {missing}")
        render_site(columns, guidelines)
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print(f"site generated: {DOCS_DIR.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
