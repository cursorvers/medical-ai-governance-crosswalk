#!/usr/bin/env python3
"""Validate Medical AI Governance Crosswalk corpus YAML files."""

from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any
from urllib.parse import urldefrag, urlparse

import yaml


ROOT = Path(__file__).resolve().parents[1]
GUIDELINES_DIR = ROOT / "corpus" / "guidelines"
EXPECTED_COLUMNS = tuple("ABCDEFGHIJKLM")
REQUIREMENTS = {
    "must",
    "should",
    "mention",
    "none",
    "not_assessed",
    "source_unavailable",
}
CONFIDENCE = {"high", "medium", "low"}
TOP_REQUIRED = {
    "id",
    "name_ja",
    "issuer",
    "jurisdiction",
    "url",
    "version",
    "last_reviewed",
    "source_hash",
    "summary_ja",
    "cells",
}
CELL_REQUIRED = {"column", "requirement", "summary_ja", "citation"}
CITATION_REQUIRED = {"url", "section", "retrieved", "confidence"}
KNOWN_BLOCKED_HOSTS = {
    "iso.org",
    "www.iso.org",
}
SOURCE_HASH_RE = re.compile(r"^sha256:[0-9a-f]{64}$")
PENDING_SOURCE_HASH_RE = re.compile(r"^sha256:pending-(\d{4}-\d{2}-\d{2})$")
URL_TIMEOUT_SECONDS = 10
URL_RETRIES = 2
PENDING_SOURCE_HASH_MAX_AGE_DAYS = 30
URL_CACHE: dict[str, str | None] = {}


class UrlCheckStats:
    def __init__(self) -> None:
        self.checked = 0
        self.skipped = 0
        self.failed = 0


URL_STATS = UrlCheckStats()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check-urls",
        action="store_true",
        help="Check that top-level and citation URLs return a successful HTTP response.",
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=ROOT,
        help="Repository root. Defaults to the parent of this script.",
    )
    return parser.parse_args()


def as_date(value: Any, label: str, errors: list[str]) -> dt.date | None:
    if isinstance(value, dt.datetime):
        return value.date()
    if isinstance(value, dt.date):
        return value
    if isinstance(value, str):
        try:
            return dt.date.fromisoformat(value)
        except ValueError:
            errors.append(f"{label}: expected ISO date, got {value!r}")
            return None
    errors.append(f"{label}: expected ISO date, got {type(value).__name__}")
    return None


def is_recent(date_value: dt.date, today: dt.date) -> bool:
    months = (today.year - date_value.year) * 12 + today.month - date_value.month
    if today.day < date_value.day:
        months -= 1
    return months <= 18


def is_known_blocked(url: str) -> bool:
    return urlparse(url).hostname in KNOWN_BLOCKED_HOSTS


def fetch_url_once(url: str, method: str) -> str | None:
    headers = {"User-Agent": "curl/8.7.1"}
    request = urllib.request.Request(url, method=method, headers=headers)
    try:
        with urllib.request.urlopen(request, timeout=URL_TIMEOUT_SECONDS) as response:
            if 200 <= response.status < 400:
                return None
            return f"HTTP {response.status}"
    except urllib.error.HTTPError as exc:
        return f"HTTP {exc.code}"
    except Exception as exc:  # noqa: BLE001
        return str(exc)


def check_url(url: str) -> str | None:
    network_url = urldefrag(url).url
    if network_url in URL_CACHE:
        return URL_CACHE[network_url]

    if is_known_blocked(network_url):
        URL_STATS.skipped += 1
        URL_CACHE[network_url] = None
        return None

    URL_STATS.checked += 1
    last_problem: str | None = None
    for _attempt in range(URL_RETRIES + 1):
        problem = fetch_url_once(network_url, "HEAD")
        if problem is None:
            URL_CACHE[network_url] = None
            return None

        problem = fetch_url_once(network_url, "GET")
        if problem is None:
            URL_CACHE[network_url] = None
            return None
        last_problem = problem

    URL_STATS.failed += 1
    URL_CACHE[network_url] = last_problem
    return last_problem


def valid_source_hash(source_hash: str, today: dt.date) -> bool:
    if SOURCE_HASH_RE.fullmatch(source_hash):
        return True
    pending = PENDING_SOURCE_HASH_RE.fullmatch(source_hash)
    if not pending:
        return False
    try:
        pending_date = dt.date.fromisoformat(pending.group(1))
    except ValueError:
        return False
    age_days = (today - pending_date).days
    return 0 <= age_days <= PENDING_SOURCE_HASH_MAX_AGE_DAYS


def require_mapping(value: Any, label: str, errors: list[str]) -> dict[str, Any] | None:
    if not isinstance(value, dict):
        errors.append(f"{label}: expected mapping")
        return None
    return value


def validate_guideline(path: Path, check_urls: bool, today: dt.date) -> list[str]:
    errors: list[str] = []
    try:
        with path.open("r", encoding="utf-8") as handle:
            data = yaml.safe_load(handle)
    except yaml.YAMLError as exc:
        return [f"{path}: YAML parse error: {exc}"]
    except OSError as exc:
        return [f"{path}: cannot read file: {exc}"]

    doc = require_mapping(data, str(path), errors)
    if doc is None:
        return errors

    missing = sorted(TOP_REQUIRED - doc.keys())
    if missing:
        errors.append(f"{path}: missing top-level fields: {', '.join(missing)}")

    guideline_id = doc.get("id")
    if guideline_id and path.stem != guideline_id:
        errors.append(f"{path}: id {guideline_id!r} does not match filename")

    top_url = doc.get("url")
    if not isinstance(top_url, str) or not top_url.startswith(("http://", "https://")):
        errors.append(f"{path}: url must start with http:// or https://")
    elif check_urls:
        problem = check_url(top_url)
        if problem:
            errors.append(f"{path}: url check failed for {top_url}: {problem}")

    last_reviewed = as_date(doc.get("last_reviewed"), f"{path}: last_reviewed", errors)
    if last_reviewed and not is_recent(last_reviewed, today):
        errors.append(f"{path}: last_reviewed is older than 18 months")

    source_hash = doc.get("source_hash")
    if not isinstance(source_hash, str) or not source_hash.strip():
        errors.append(f"{path}: source_hash must be a non-empty string")
    elif not valid_source_hash(source_hash, today):
        errors.append(
            f"{path}: source_hash must be 'sha256:' + 64 lowercase hex chars "
            "or temporary 'sha256:pending-YYYY-MM-DD' dated within 30 days"
        )

    cells = doc.get("cells")
    if not isinstance(cells, list):
        errors.append(f"{path}: cells must be a list")
        return errors

    seen_columns: list[str] = []
    for index, cell in enumerate(cells):
        label = f"{path}: cells[{index}]"
        cell_map = require_mapping(cell, label, errors)
        if cell_map is None:
            continue

        missing_cell = sorted(CELL_REQUIRED - cell_map.keys())
        if missing_cell:
            errors.append(f"{label}: missing fields: {', '.join(missing_cell)}")

        column = cell_map.get("column")
        if column not in EXPECTED_COLUMNS:
            errors.append(f"{label}: invalid column {column!r}")
        else:
            seen_columns.append(column)

        requirement = cell_map.get("requirement")
        if requirement not in REQUIREMENTS:
            errors.append(f"{label}: invalid requirement {requirement!r}")

        summary = cell_map.get("summary_ja")
        if not isinstance(summary, str) or not summary.strip():
            errors.append(f"{label}: summary_ja must be a non-empty string")
        elif len(summary.strip()) > 80:
            errors.append(f"{label}: summary_ja exceeds 80 characters")

        citation = cell_map.get("citation")
        citation_map = require_mapping(citation, f"{label}: citation", errors)
        if citation_map is None:
            continue

        missing_citation = sorted(CITATION_REQUIRED - citation_map.keys())
        if missing_citation:
            errors.append(f"{label}: citation missing fields: {', '.join(missing_citation)}")

        citation_url = citation_map.get("url")
        if not isinstance(citation_url, str) or not citation_url.startswith(("http://", "https://")):
            errors.append(f"{label}: citation.url must start with http:// or https://")
        elif check_urls:
            problem = check_url(citation_url)
            if problem:
                errors.append(f"{label}: citation.url check failed for {citation_url}: {problem}")

        if not isinstance(citation_map.get("section"), str) or not citation_map["section"].strip():
            errors.append(f"{label}: citation.section must be a non-empty string")

        as_date(citation_map.get("retrieved"), f"{label}: citation.retrieved", errors)

        confidence = citation_map.get("confidence")
        if confidence not in CONFIDENCE:
            errors.append(f"{label}: invalid citation.confidence {confidence!r}")

    duplicates = sorted({column for column in seen_columns if seen_columns.count(column) > 1})
    if duplicates:
        errors.append(f"{path}: duplicate cells for columns: {', '.join(duplicates)}")

    missing_columns = sorted(set(EXPECTED_COLUMNS) - set(seen_columns))
    if missing_columns:
        errors.append(f"{path}: missing cells for columns: {', '.join(missing_columns)}")

    extra_columns = sorted(set(seen_columns) - set(EXPECTED_COLUMNS))
    if extra_columns:
        errors.append(f"{path}: unexpected cells for columns: {', '.join(extra_columns)}")

    return errors


def main() -> int:
    args = parse_args()
    guidelines_dir = args.root / "corpus" / "guidelines"
    today = dt.date.today()

    if not guidelines_dir.exists():
        print(f"missing directory: {guidelines_dir}", file=sys.stderr)
        return 1

    files = sorted(guidelines_dir.glob("*.yml"))
    if not files:
        print(f"no guideline YAML files found in {guidelines_dir}", file=sys.stderr)
        return 1

    all_errors: list[str] = []
    for path in files:
        all_errors.extend(validate_guideline(path, args.check_urls, today))

    if args.check_urls:
        print(
            "URL check summary: "
            f"checked={URL_STATS.checked} skipped={URL_STATS.skipped} failed={URL_STATS.failed}",
            file=sys.stderr,
        )

    if all_errors:
        for error in all_errors:
            print(error, file=sys.stderr)
        return 1

    print(f"validated {len(files)} guideline file(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
