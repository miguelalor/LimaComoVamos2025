"""Builds index.html at the repo root from dashboard/shell.html and dashboard/page.html.

Usage: python scripts/build_site.py
"""
from pathlib import Path

root = Path(__file__).resolve().parent.parent
shell = (root / "dashboard" / "shell.html").read_text(encoding="utf-8")
page = (root / "dashboard" / "page.html").read_text(encoding="utf-8")
(root / "index.html").write_text(shell.replace("<!-- PAGE -->", page), encoding="utf-8")
print("index.html written")
