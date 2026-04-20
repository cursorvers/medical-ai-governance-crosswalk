#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from urllib.parse import urldefrag

import requests
import yaml

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BASELINE = ROOT / "state" / "source-freshness.json"
DEFAULT_OUTPUT = ROOT / "state" / "source-freshness-report.json"
GUIDELINES_DIR = ROOT / "corpus" / "guidelines"
TIMEOUT_SECONDS = 15
USER_AGENT = (
    "medgov-source-freshness/1.0 "
    "(+https://github.com/cursorvers/medical-ai-governance-crosswalk)"
)


@dataclass(frozen=True)
class CitationRef:
    guideline_id: str
    guideline_file: str
    column: str
    url: str
    fetch_url: str
    section: str | None


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check corpus citation sources for content freshness drift."
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help=f"Report output path. Default: {DEFAULT_OUTPUT}",
    )
    parser.add_argument(
        "--baseline",
        type=Path,
        default=DEFAULT_BASELINE,
        help=f"Baseline JSON path. Default: {DEFAULT_BASELINE}",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Limit unique URLs fetched, for smoke tests.",
    )
    return parser.parse_args()


def utc_now_iso() -> str:
    return dt.datetime.now(dt.UTC).replace(microsecond=0).isoformat()


def load_yaml(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    return data if isinstance(data, dict) else {}


def load_baseline(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {"sources": {}}
    try:
        with path.open("r", encoding="utf-8") as handle:
            data = json.load(handle)
    except (OSError, json.JSONDecodeError) as exc:
        return {"sources": {}, "_load_error": str(exc)}
    if not isinstance(data, dict):
        return {"sources": {}, "_load_error": "baseline root must be an object"}
    if not isinstance(data.get("sources"), dict):
        data["sources"] = {}
    return data


def collect_citation_refs(limit: int | None = None) -> tuple[dict[str, list[CitationRef]], int]:
    refs_by_fetch_url: dict[str, list[CitationRef]] = {}
    total_cells_with_url = 0

    for path in sorted(GUIDELINES_DIR.glob("*.yml")):
        doc = load_yaml(path)
        guideline_id = str(doc.get("id") or path.stem)
        cells = doc.get("cells", [])
        if not isinstance(cells, list):
            continue

        for cell in cells:
            if not isinstance(cell, dict):
                continue
            citation = cell.get("citation")
            if not isinstance(citation, dict):
                continue
            raw_url = citation.get("url")
            if not raw_url:
                continue
            total_cells_with_url += 1

            url = str(raw_url).strip()
            if not url:
                continue
            fetch_url = urldefrag(url).url
            if not fetch_url:
                continue
            if limit is not None and fetch_url not in refs_by_fetch_url:
                if len(refs_by_fetch_url) >= limit:
                    continue

            refs_by_fetch_url.setdefault(fetch_url, []).append(
                CitationRef(
                    guideline_id=guideline_id,
                    guideline_file=str(path.relative_to(ROOT)),
                    column=str(cell.get("column") or ""),
                    url=url,
                    fetch_url=fetch_url,
                    section=str(citation.get("section"))
                    if citation.get("section") is not None
                    else None,
                )
            )

    return refs_by_fetch_url, total_cells_with_url


def source_snapshot(url: str) -> dict[str, Any]:
    response = requests.get(
        url,
        headers={"User-Agent": USER_AGENT},
        timeout=TIMEOUT_SECONDS,
    )
    body = response.content.strip()
    return {
        "url": url,
        "status": response.status_code,
        "sha256": hashlib.sha256(body).hexdigest(),
        "etag": response.headers.get("ETag"),
        "last_modified": response.headers.get("Last-Modified"),
        "content_length": len(body),
        "final_url": response.url,
    }


def pick_reference_fields(ref: CitationRef) -> dict[str, Any]:
    return {
        "guideline_id": ref.guideline_id,
        "guideline_file": ref.guideline_file,
        "column": ref.column,
        "url": ref.url,
        "fetch_url": ref.fetch_url,
        "section": ref.section,
    }


def compare_snapshot(
    current: dict[str, Any],
    baseline_entry: dict[str, Any] | None,
) -> dict[str, Any]:
    if not baseline_entry:
        return {
            "reason": "missing_baseline",
            "old": {},
            "new": {
                "status": current.get("status"),
                "sha256": current.get("sha256"),
                "etag": current.get("etag"),
                "last_modified": current.get("last_modified"),
            },
        }

    fields = ("status", "sha256", "etag", "last_modified")
    changed_fields = [
        field for field in fields if baseline_entry.get(field) != current.get(field)
    ]
    return {
        "reason": "changed_fields",
        "changed_fields": changed_fields,
        "old": {field: baseline_entry.get(field) for field in fields},
        "new": {field: current.get(field) for field in fields},
    }


def build_report(args: argparse.Namespace) -> dict[str, Any]:
    baseline = load_baseline(args.baseline)
    baseline_sources = baseline.get("sources", {})
    if not isinstance(baseline_sources, dict):
        baseline_sources = {}

    refs_by_fetch_url, total_cells_with_url = collect_citation_refs(args.limit)
    report: dict[str, Any] = {
        "checked_at": utc_now_iso(),
        "total": len(refs_by_fetch_url),
        "ok": 0,
        "changed": 0,
        "errors": 0,
        "drift": [],
        "errors_detail": [],
        "meta": {
            "baseline": str(args.baseline),
            "total_cells_with_url": total_cells_with_url,
            "unique_urls": len(refs_by_fetch_url),
            "limit": args.limit,
            "user_agent": USER_AGENT,
            "timeout_seconds": TIMEOUT_SECONDS,
        },
    }
    if baseline.get("_load_error"):
        report["errors"] += 1
        report["errors_detail"].append(
            {
                "url": None,
                "phase": "baseline_load",
                "error": baseline["_load_error"],
            }
        )

    for fetch_url, refs in refs_by_fetch_url.items():
        try:
            current = source_snapshot(fetch_url)
        except requests.RequestException as exc:
            report["errors"] += 1
            for ref in refs:
                report["errors_detail"].append(
                    {
                        **pick_reference_fields(ref),
                        "error": exc.__class__.__name__,
                        "message": str(exc),
                    }
                )
            continue

        if 200 <= int(current["status"]) < 400:
            report["ok"] += 1
        else:
            report["errors"] += 1
            for ref in refs:
                report["errors_detail"].append(
                    {
                        **pick_reference_fields(ref),
                        "status": current["status"],
                        "message": "non-success HTTP status",
                    }
                )

        baseline_entry = baseline_sources.get(fetch_url)
        comparison = compare_snapshot(
            current,
            baseline_entry if isinstance(baseline_entry, dict) else None,
        )
        changed_fields = comparison.get("changed_fields")
        is_changed = comparison["reason"] == "missing_baseline" or bool(changed_fields)

        if is_changed:
            report["changed"] += 1
            for ref in refs:
                report["drift"].append(
                    {
                        **pick_reference_fields(ref),
                        "reason": comparison["reason"],
                        "changed_fields": changed_fields or [],
                        "old": comparison["old"],
                        "new": {
                            **comparison["new"],
                            "content_length": current.get("content_length"),
                            "final_url": current.get("final_url"),
                        },
                        "sample_diff_fetch_curl": (
                            "curl -L -A "
                            f"{json.dumps(USER_AGENT)} "
                            f"{json.dumps(fetch_url)}"
                        ),
                    }
                )

    return report


def write_report(report: dict[str, Any], output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8") as handle:
        json.dump(report, handle, ensure_ascii=False, indent=2, sort_keys=True)
        handle.write("\n")


def main() -> int:
    args = parse_args()
    try:
        report = build_report(args)
    except Exception as exc:  # Keep scheduled workflows non-failing by contract.
        report = {
            "checked_at": utc_now_iso(),
            "total": 0,
            "ok": 0,
            "changed": 0,
            "errors": 1,
            "drift": [],
            "errors_detail": [
                {
                    "phase": "fatal",
                    "error": exc.__class__.__name__,
                    "message": str(exc),
                }
            ],
        }
    write_report(report, args.output)
    print(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
