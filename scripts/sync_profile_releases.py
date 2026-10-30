#!/usr/bin/env python3
"""Synchronize the six profile project status cells from GitHub Releases."""
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
    "Camper Weather": "ha-camper-weather",
    "Camper Route Planner": "ha-camper-route-planner",
}

VERSION_TAG = re.compile(r"^v\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?$")

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


def latest_release(items, *, prerelease):
    candidates = [
        item
        for item in items
        if not item["draft"]
        and item["prerelease"] is prerelease
        and VERSION_TAG.fullmatch(item["tag_name"])
    ]
    return max(candidates, key=lambda item: item.get("published_at") or "", default=None)


def status_from_items(repo, items):
    stable = latest_release(items, prerelease=False)
    betas = [
        item
        for item in items
        if not item["draft"]
        and item["prerelease"]
        and VERSION_TAG.fullmatch(item["tag_name"])
    ]
    if not stable and not betas:
        return "**In Entwicklung – noch kein veröffentlichtes Release**", "**In development – no published release yet**"
    # Keep the current prerelease line visible alongside Stable. Stable does
    # not imply that a newer active beta is obsolete.
    beta = max(betas, key=lambda item: item.get("published_at") or "", default=None)
    stable_de = f"Stable [`{stable['tag_name']}`](https://github.com/balronu/{repo}/releases/tag/{stable['tag_name']})" if stable else ""
    stable_en = f"Stable [`{stable['tag_name']}`](https://github.com/balronu/{repo}/releases/tag/{stable['tag_name']})" if stable else ""
    if beta:
        link_de = f"[`{beta['tag_name']}`](https://github.com/balronu/{repo}/releases/tag/{beta['tag_name']})"
        link_en = f"[`{beta['tag_name']}`](https://github.com/balronu/{repo}/releases/tag/{beta['tag_name']})"
        stable_de = f"{stable_de + '; ' if stable_de else ''}Beta {link_de}"
        stable_en = f"{stable_en + '; ' if stable_en else ''}beta {link_en}"
    if repo == "ha-camper-route-planner" and not stable:
        stable_de = f"**In Entwicklung – {stable_de}; noch kein Stable-Release**"
        stable_en = f"**In development – {stable_en}; no stable release yet**"
    return stable_de, stable_en


def status(repo):
    return status_from_items(repo, releases(repo))


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
    fuel = latest_release(releases(PROJECTS["Mobile Fuel Stations"]), prerelease=False)
    if fuel is None:
        raise RuntimeError("Mobile Fuel Stations has no published semver stable release")
    de = re.sub(r"v\d+\.\d+\.\d+ ergänzt", f"{fuel['tag_name']} ergänzt", de, count=1)
    en = re.sub(r"v\d+\.\d+\.\d+ adds", f"{fuel['tag_name']} adds", en, count=1)
    (ROOT / "README.md").write_text(de)
    (ROOT / "README.en.md").write_text(en)


if __name__ == "__main__":
    main()
