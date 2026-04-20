from __future__ import annotations

import html
import importlib.util
import re
import shutil
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
BUILD_EVIDENCE_DIR = ROOT / "build" / "evidence"
CHANGELOG_PATH = ROOT / "CHANGELOG.md"
CHANGELOG_PARTIAL_PATH = ROOT / "site" / "docs" / "_partials" / "changelog.md"
OG_GENERATOR_PATH = ROOT / "site" / "scripts" / "generate_og.py"


def _changelog_sections() -> list[str]:
    if not CHANGELOG_PATH.exists():
        return []
    text = CHANGELOG_PATH.read_text(encoding="utf-8").strip()
    if not text:
        return []
    matches = list(re.finditer(r"(?m)^##\s+", text))
    sections: list[str] = []
    for index, match in enumerate(matches):
        start = match.start()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        sections.append(text[start:end].strip())
    return sections


def _recent_changelog(limit: int = 5) -> str:
    sections = _changelog_sections()[:limit]
    if not sections:
        return "- 更新履歴はまだありません。"
    return "\n\n".join(sections)


def _recent_changelog_html(limit: int = 5) -> str:
    sections = _changelog_sections()[:limit]
    if not sections:
        return "<p>更新履歴はまだありません。</p>"
    articles: list[str] = []
    for section in sections:
        lines = [line.rstrip() for line in section.splitlines()]
        title = html.escape(lines[0].lstrip("# ").strip() if lines else "更新")
        items = [html.escape(line[2:].strip()) for line in lines[1:] if line.startswith("- ")]
        if items:
            body = "<ul>" + "".join(f"<li>{item}</li>" for item in items) + "</ul>"
        else:
            paragraphs = [html.escape(line) for line in lines[1:] if line.strip()]
            body = "".join(f"<p>{paragraph}</p>" for paragraph in paragraphs)
        articles.append(f"<article><h3>{title}</h3>{body}</article>")
    return "\n".join(articles)


def _last_updated() -> str:
    recent = _recent_changelog(1)
    match = re.search(r"\d{4}-\d{2}-\d{2}", recent)
    if match:
        return match.group(0)
    return "未設定"


def _write_changelog_partial() -> None:
    CHANGELOG_PARTIAL_PATH.parent.mkdir(parents=True, exist_ok=True)
    CHANGELOG_PARTIAL_PATH.write_text(_recent_changelog(5) + "\n", encoding="utf-8")


def _generate_og(site_dir: str | Path) -> None:
    if not OG_GENERATOR_PATH.exists():
        return
    spec = importlib.util.spec_from_file_location("generate_og", OG_GENERATOR_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load OG generator: {OG_GENERATOR_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.generate_og(Path(site_dir) / "assets" / "og.png")


def on_page_markdown(markdown: str, **_kwargs: Any) -> str:
    _write_changelog_partial()
    return (
        markdown.replace("{{last_updated}}", _last_updated())
        .replace("{{changelog_recent5}}", _recent_changelog_html(5))
    )


def on_post_build(config: dict[str, Any], **_kwargs: Any) -> None:
    if BUILD_EVIDENCE_DIR.exists():
        target_dir = Path(config["site_dir"]) / "evidence"
        target_dir.mkdir(parents=True, exist_ok=True)
        for source in sorted(BUILD_EVIDENCE_DIR.glob("*.md")):
            shutil.copy2(source, target_dir / source.name)
    _write_changelog_partial()
    _generate_og(config["site_dir"])
