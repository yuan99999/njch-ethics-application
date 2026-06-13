#!/usr/bin/env python3
"""Download Nanjing Children's Hospital ethics form attachments."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
import urllib.parse
import urllib.request
from html.parser import HTMLParser
from pathlib import Path


PAGES = {
    "medical-ethics": "https://www.njch.com.cn/kyjx/detail.asp?ID=5101",
    "drug-device-trials": "https://www.njch.com.cn/kyjx/detail.asp?ID=5401",
}


class AttachmentParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[dict[str, str]] = []
        self._current: dict[str, str] | None = None
        self._text: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() != "a":
            return
        data = {key.lower(): value or "" for key, value in attrs}
        href = data.get("href", "")
        if "/upload/file/" in href:
            self._current = {"href": href, "title": data.get("title", "")}
            self._text = []

    def handle_data(self, data: str) -> None:
        if self._current is not None:
            self._text.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "a" and self._current is not None:
            text = "".join(self._text).strip()
            if text and not self._current.get("title"):
                self._current["title"] = text
            self.links.append(self._current)
            self._current = None
            self._text = []


def fetch_text(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "Codex skill form fetcher"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = resp.read()
        content_type = resp.headers.get("Content-Type", "")
    match = re.search(r"charset=([\w-]+)", content_type, re.I)
    encoding = match.group(1) if match else "utf-8"
    return data.decode(encoding, errors="replace")


def safe_name(name: str) -> str:
    name = urllib.parse.unquote(name).strip()
    name = re.sub(r"[\\/:*?\"<>|]+", "_", name)
    return name or "attachment"


def quote_url(url: str) -> str:
    parts = urllib.parse.urlsplit(url)
    return urllib.parse.urlunsplit(
        (
            parts.scheme,
            parts.netloc,
            urllib.parse.quote(urllib.parse.unquote(parts.path), safe="/"),
            urllib.parse.quote_plus(urllib.parse.unquote_plus(parts.query), safe="=&"),
            parts.fragment,
        )
    )


def download(url: str, output: Path) -> int:
    req = urllib.request.Request(quote_url(url), headers={"User-Agent": "Codex skill form fetcher"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        data = resp.read()
    output.write_bytes(data)
    return len(data)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--out",
        default=str(Path(__file__).resolve().parents[1] / "assets" / "official-forms"),
        help="Output directory for downloaded forms.",
    )
    args = parser.parse_args()

    out_dir = Path(args.out).expanduser().resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    manifest: dict[str, object] = {
        "fetched_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "pages": [],
    }

    for category, page_url in PAGES.items():
        html = fetch_text(page_url)
        parser_obj = AttachmentParser()
        parser_obj.feed(html)
        page_entry = {"category": category, "page_url": page_url, "files": []}
        category_dir = out_dir / category
        category_dir.mkdir(parents=True, exist_ok=True)

        for link in parser_obj.links:
            file_url = urllib.parse.urljoin(page_url, link["href"])
            fallback = Path(urllib.parse.urlparse(file_url).path).name
            filename = safe_name(link.get("title") or fallback)
            target = category_dir / filename
            size = download(file_url, target)
            page_entry["files"].append(
                {
                    "filename": filename,
                    "path": str(target.relative_to(out_dir)),
                    "source_url": file_url,
                    "bytes": size,
                }
            )

        manifest["pages"].append(page_entry)

    (out_dir / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    total = sum(len(page["files"]) for page in manifest["pages"])  # type: ignore[index]
    print(f"Downloaded {total} files to {out_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
