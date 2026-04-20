from __future__ import annotations

import shutil
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
BUILD_EVIDENCE_DIR = ROOT / "build" / "evidence"


def on_post_build(config: dict[str, Any], **_kwargs: Any) -> None:
    if not BUILD_EVIDENCE_DIR.exists():
        return
    target_dir = Path(config["site_dir"]) / "evidence"
    target_dir.mkdir(parents=True, exist_ok=True)
    for source in sorted(BUILD_EVIDENCE_DIR.glob("*.md")):
        shutil.copy2(source, target_dir / source.name)
