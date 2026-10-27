"""Offline integrity checks for the distributed skill and artwork."""

import hashlib
import json
from pathlib import Path
import re
import unittest
from urllib.parse import unquote

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]


class AssetTests(unittest.TestCase):
    def test_asset_checksums_and_inventory(self):
        hashes = json.loads((ROOT / "references/asset-checksums.json").read_text())
        actual = {p.relative_to(ROOT / "assets").as_posix()
                  for p in (ROOT / "assets").rglob("*") if p.is_file()}
        self.assertEqual(set(hashes), actual)
        for name, expected in hashes.items():
            with self.subTest(asset=name):
                self.assertEqual(hashlib.sha256((ROOT / "assets" / name).read_bytes())
                                 .hexdigest(), expected)

    def test_export_measurements(self):
        manifest = json.loads((ROOT / "references/example-exports.json").read_text())
        exports = [item for icon in manifest["icons"] for item in icon["outputs"]]
        exports.append(manifest["contact_sheet"])
        for entry in exports:
            with self.subTest(asset=entry["path"]):
                path = ROOT / entry["path"]
                self.assertEqual(path.stat().st_size, entry["bytes"])
                with Image.open(path) as image:
                    image.load()
                    self.assertEqual(list(image.size), entry["dimensions"])
                    self.assertEqual(image.mode, "RGBA")
                    self.assertEqual(image.getchannel("A").getextrema(), (0, 255))
                    self.assertEqual(image.format, "WEBP" if path.suffix == ".webp"
                                     else "PNG")

    def test_images_have_no_source_metadata(self):
        for path in (ROOT / "assets").rglob("*"):
            if path.suffix not in {".png", ".webp"}:
                continue
            with self.subTest(asset=path.relative_to(ROOT).as_posix()):
                with Image.open(path) as image:
                    image.load()
                    self.assertFalse(image.getexif())
                    self.assertFalse(set(image.info) - {"icc_profile", "gamma", "srgb",
                                                       "dpi", "loop", "background",
                                                       "chromaticity", "duration",
                                                       "timestamp"})

    def test_local_document_links(self):
        for path in [ROOT / "README.md", ROOT / "SKILL.md",
                     *(ROOT / "references").glob("*.md")]:
            content = path.read_text(encoding="utf-8")
            links = re.findall(r'\]\(([^)]+)\)|(?:src|href)="([^"]+)"', content)
            for markdown, html in links:
                target = markdown or html
                if target.startswith(("https://", "http://", "#")):
                    continue
                with self.subTest(document=path.name, target=target):
                    self.assertTrue((path.parent / unquote(target.split("#")[0])).exists())


if __name__ == "__main__":
    unittest.main()
