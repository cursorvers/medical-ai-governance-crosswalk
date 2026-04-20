#!/usr/bin/env python3
from __future__ import annotations

import argparse
import socket
import sys
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urldefrag
from urllib.request import Request, urlopen

import yaml

ROOT = Path(__file__).resolve().parents[1]
URL_TIMEOUT_SECONDS = 10


def load_yaml(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle) or {}


def collect_urls() -> list[str]:
    urls: set[str] = set()
    for path in sorted((ROOT / "corpus" / "guidelines").glob("*.yml")):
        doc = load_yaml(path)
        if doc.get("url"):
            urls.add(str(doc["url"]))
        for cell in doc.get("cells", []):
            citation = cell.get("citation", {}) if isinstance(cell, dict) else {}
            if citation.get("url"):
                urls.add(str(citation["url"]))
    return sorted(urls)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Check corpus source and citation URLs.")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit 1 when any URL does not return a successful response.",
    )
    return parser.parse_args()


def check_url(url: str) -> tuple[bool, str]:
    network_url = urldefrag(url).url
    request = Request(network_url, headers={"User-Agent": "medai-crosswalk-url-check/1.0"})
    try:
        with urlopen(request, timeout=URL_TIMEOUT_SECONDS) as response:
            return 200 <= response.status < 400, str(response.status)
    except HTTPError as exc:
        return False, f"HTTP {exc.code}"
    except URLError as exc:
        return False, f"URL error: {exc.reason}"
    except (TimeoutError, socket.timeout):
        return False, "timeout"


def main() -> int:
    args = parse_args()
    failures: list[str] = []
    for url in collect_urls():
        ok, status = check_url(url)
        print(f"{status} {url}")
        if not ok:
            failures.append(f"{status} {url}")
    if failures:
        print("URL check warnings:", file=sys.stderr)
        for failure in failures:
            print(f"WARNING: {failure}", file=sys.stderr)
        return 1 if args.strict else 0
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
