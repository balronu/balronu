#!/usr/bin/env python3
"""Synchronize the five profile project status cells from GitHub Releases."""
import json
import os
import re
import urllib.request
from pathlib import Path

PROJECTS = {
    "Mobile Fuel Stations": "ha-mobile-fuel-stations",
    "Air Traffic": "ha-air-traffic",
    "Camper Travel Journal": "ha-camper-travel-journal",
    "Bike Weather": "ha-bike-weather",
    "Camper Route Planner": "ha-camper-route-planner",
}

ROOT = Path(__file__).resolve().parents[1]


def releases(repo):
    url = f"https://api.github.com/repos/balronu/{repo}/releases?per_page=100"
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "balronu-profile-sync"}
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    request = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(request, timeout=20) as response:
        return json.load(response)


def status(repo):
    items = releases(repo)
    stable = next((r for r in items if not r["draft"] and not r["prerelease"] and re.fullmatch(r"v\d+\.\d+\.\d+", r["tag_name"])), None)
    betas = [r for r in items if not r["draft"] and r["prerelease"]]
    if not stable and not betas:
        return "**In Entwicklung – noch kein veröffentlichtes Release**", "**In development – no published release yet**"
    stable_de = f"Stable [`{stable['tag_name']}`](https://github.com/balronu/{repo}/releases/tag/{stable['tag_name']})" if stable else ""
    stable_en = f"Stable [`{stable['tag_name']}`](https://github.com/balronu/{repo}/releases/tag/{stable['tag_name']})" if stable else ""
    beta = betas[0] if betas else None
    if beta:
        link_de = f"[`{beta['tag_name']}`](https://github.com/balronu/{repo}/releases/tag/{beta['tag_name']})"
        link_en = f"[`{beta['tag_name']}`](https://github.com/balronu/{repo}/releases/tag/{beta['tag_name']})"
        stable_de = f"{stable_de + '; ' if stable_de else ''}Beta {link_de}"
        stable_en = f"{stable_en + '; ' if stable_en else ''}beta {link_en}"
    if repo == "ha-camper-route-planner" and not stable:
        stable_de = f"**In Entwicklung – {stable_de}; noch kein Stable-Release**"
        stable_en = f"**In development – {stable_en}; no stable release yet**"
    return stable_de, stable_en


def replace_row(text, label, replacement):
    pattern = re.compile(rf"^(\| \[{re.escape(label)}\].*\| ).*?( \|)$", re.MULTILINE)
    updated, count = pattern.subn(rf"\1{replacement}\2", text, count=1)
    if count != 1:
        raise RuntimeError(f"profile row not found exactly once: {label}")
    return updated


def main():
    statuses = {label: status(repo) for label, repo in PROJECTS.items()}
    de = (ROOT / "README.md").read_text()
    en = (ROOT / "README.en.md").read_text()
    for label, (de_status, en_status) in statuses.items():
        de = replace_row(de, label, de_status)
        en = replace_row(en, label, en_status)
    fuel = next(r for r in releases(PROJECTS["Mobile Fuel Stations"]) if not r["draft"] and not r["prerelease"] and re.fullmatch(r"v\d+\.\d+\.\d+", r["tag_name"]))
    de = re.sub(r"v\d+\.\d+\.\d+ ergänzt", f"{fuel['tag_name']} ergänzt", de, count=1)
    en = re.sub(r"v\d+\.\d+\.\d+ adds", f"{fuel['tag_name']} adds", en, count=1)
    (ROOT / "README.md").write_text(de)
    (ROOT / "README.en.md").write_text(en)


if __name__ == "__main__":
    main()
