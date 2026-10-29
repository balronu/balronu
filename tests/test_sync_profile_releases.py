import importlib.util
import unittest
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "scripts" / "sync_profile_releases.py"
SPEC = importlib.util.spec_from_file_location("sync_profile_releases", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


def release(tag, *, prerelease=False, draft=False, published_at="2026-01-01T00:00:00Z"):
    return {
        "tag_name": tag,
        "prerelease": prerelease,
        "draft": draft,
        "published_at": published_at,
    }


class ReleaseSelectionTests(unittest.TestCase):
    def test_ignores_drafts_and_non_version_releases(self):
        items = [
            release("v9.9.9", draft=True),
            release("public-release"),
            release("v1.2.0", published_at="2026-02-01T00:00:00Z"),
        ]
        selected = MODULE.latest_release(items, prerelease=False)
        self.assertEqual(selected["tag_name"], "v1.2.0")

    def test_selects_newest_published_stable_and_beta_independently(self):
        items = [
            release("v1.0.0"),
            release("v1.1.0", published_at="2026-03-01T00:00:00Z"),
            release("v2.0.0-beta.1", prerelease=True),
            release("v2.0.0-beta.2", prerelease=True, published_at="2026-03-02T00:00:00Z"),
        ]
        self.assertEqual(MODULE.latest_release(items, prerelease=False)["tag_name"], "v1.1.0")
        self.assertEqual(MODULE.latest_release(items, prerelease=True)["tag_name"], "v2.0.0-beta.2")

    def test_in_development_status_when_no_published_release_exists(self):
        de, en = MODULE.status_from_items("ha-camper-route-planner", [release("v0.1.0", draft=True)])
        self.assertIn("In Entwicklung", de)
        self.assertIn("In development", en)

    def test_stable_hides_all_prereleases(self):
        items = [
            release("v1.0.0"),
            release("v2.0.0-beta.1", prerelease=True, published_at="2026-03-02T00:00:00Z"),
            release("v2.0.0-rc.1", prerelease=True, published_at="2026-03-03T00:00:00Z"),
        ]
        de, en = MODULE.status_from_items("ha-camper-weather", items)
        self.assertIn("Stable [`v1.0.0`]", de)
        self.assertIn("Stable [`v1.0.0`]", en)
        self.assertNotIn("beta", de.lower())
        self.assertNotIn("beta", en.lower())
        self.assertNotIn("rc", de.lower())
        self.assertNotIn("rc", en.lower())


if __name__ == "__main__":
    unittest.main()
