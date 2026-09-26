import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from scripts import build_site


class BuildSiteTests(unittest.TestCase):
    def test_repository_content_is_escaped_and_path_is_rejected(self):
        template = Path(build_site.ROOT / "site/repo.html").read_text(encoding="utf-8")
        entry = {"owner": "author", "name": "repo", "desc": 'A <script>alert("x")</script> project', "stars": 2}
        page = build_site.render(template, entry)
        self.assertIn('A &lt;script&gt;alert(&quot;x&quot;)&lt;/script&gt; project', page)
        self.assertNotIn('<script>alert', page)
        entry["name"] = ".."
        with self.assertRaises(ValueError):
            build_site.render(template, entry)

    def test_build_has_bookmarkable_page_for_each_entry(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / "data").mkdir()
            (root / "site").mkdir()
            (root / "assets").mkdir()
            (root / "node_modules/dompurify/dist").mkdir(parents=True)
            (root / "index.html").write_text("INDEX", encoding="utf-8")
            (root / "site/repo.html").write_text('__ROOT__ __TITLE__', encoding="utf-8")
            (root / "assets/site.css").write_text("CSS", encoding="utf-8")
            (root / "node_modules/dompurify/dist/purify.min.js").write_text("SANITIZER", encoding="utf-8")
            (root / "data/jev.json").write_text(json.dumps([{"owner": "a", "name": "b", "desc": "hello"}]), encoding="utf-8")
            (root / "data/meta.json").write_text("{}", encoding="utf-8")
            with patch.object(build_site, "ROOT", root), patch.object(build_site, "DEST", root / "dist"):
                build_site.build()
            self.assertEqual((root / "dist/repo/a/b/index.html").read_text(encoding="utf-8"), "../../../ a / b")
            self.assertTrue((root / "dist/assets/purify.min.js").is_file())


if __name__ == "__main__":
    unittest.main()
