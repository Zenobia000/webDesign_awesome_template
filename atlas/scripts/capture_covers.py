"""Capture cover images for the atlas.

- Resource sites: download the page's og:image (the site's own cover);
  fall back to a headless Chrome screenshot when there is none.
- Style templates (../styles/*.html): headless Chrome screenshot.

Usage: python atlas/scripts/capture_covers.py [--only res|styles] [--force]
Requires: Pillow, Google Chrome.
"""

from __future__ import annotations

import argparse
import html
import io
import re
import subprocess
import sys
import tempfile
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.parse import urljoin

from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
OUT_RES = ROOT / "atlas" / "img" / "res"
OUT_STYLES = ROOT / "atlas" / "img" / "styles"
CHROME_CANDIDATES = [
    Path(r"C:\Program Files\Google\Chrome\Application\chrome.exe"),
    Path(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"),
    Path("/usr/bin/google-chrome"),
    Path("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"),
]
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0 Safari/537.36"
SIZE = (800, 500)  # style screenshots, 16:10
OG_SIZE = (800, 420)  # og:image ratio 1200x630

RESOURCES = {
    "awwwards": "https://www.awwwards.com/",
    "godly": "https://godly.website/",
    "landbook": "https://land-book.com/",
    "lapa": "https://www.lapa.ninja/",
    "mobbin": "https://mobbin.com/",
    "saasframe": "https://www.saasframe.io/",
    "pageflows": "https://pageflows.com/",
    "shadcn": "https://ui.shadcn.com/",
    "figma": "https://www.figma.com/community",
    "21st": "https://21st.dev/",
    "aceternity": "https://ui.aceternity.com/",
    "magicui": "https://magicui.design/",
    "motion": "https://motion.dev/",
    "gsap": "https://gsap.com/",
    "lottie": "https://lottiefiles.com/",
    "rive": "https://rive.app/",
    "spline": "https://spline.design/",
    "threejs": "https://threejs.org/",
    "unsplash": "https://unsplash.com/",
    "pexels": "https://www.pexels.com/",
    "typewolf": "https://www.typewolf.com/",
    "gfonts": "https://fonts.google.com/",
    "adobefonts": "https://fonts.adobe.com/",
    "colorhunt": "https://colorhunt.co/",
    "canva": "https://www.canva.com/colors/",
    "adobecolor": "https://color.adobe.com/",
    "realtime": "https://www.realtimecolors.com/",
    "colorzilla": "https://www.colorzilla.com/chrome/",
    "sitepalette": "https://palette.site/",
    "csspeeper": "https://csspeeper.com/",
    "oklch": "https://oklch.com/",
    "webaim": "https://webaim.org/resources/contrastchecker/",
}

OG_RE = re.compile(
    r"<meta[^>]+(?:property|name)=[\"'](?:og:image|twitter:image)(?::src)?[\"'][^>]*>", re.I
)
CONTENT_RE = re.compile(r"content=[\"']([^\"']+)[\"']", re.I)


def find_chrome() -> Path:
    for c in CHROME_CANDIDATES:
        if c.exists():
            return c
    sys.exit("Chrome / Edge not found")


def fetch(url: str, timeout: int = 20) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "en"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def cover_fit(img: Image.Image, size: tuple[int, int] = SIZE, top: bool = False) -> Image.Image:
    img = img.convert("RGB")
    tw, th = size
    scale = max(tw / img.width, th / img.height)
    img = img.resize((round(img.width * scale), round(img.height * scale)), Image.Resampling.LANCZOS)
    left = (img.width - tw) // 2
    upper = 0 if top else (img.height - th) // 2
    return img.crop((left, upper, left + tw, upper + th))


def save_webp(img: Image.Image, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    img.save(path, "WEBP", quality=78, method=6)


def screenshot(chrome: Path, target: str, out: Path, wait_ms: int = 6000, size: tuple[int, int] = SIZE) -> bool:
    with tempfile.TemporaryDirectory() as tmp:
        png = Path(tmp) / "shot.png"
        cmd = [
            str(chrome), "--headless=new", "--disable-gpu", "--hide-scrollbars", "--mute-audio",
            f"--user-data-dir={tmp}", "--window-size=1440,900", f"--virtual-time-budget={wait_ms}",
            f"--user-agent={UA}", f"--screenshot={png}", target,
        ]
        try:
            subprocess.run(cmd, capture_output=True, timeout=90)
        except subprocess.TimeoutExpired:
            return False
        if not png.exists():
            return False
        save_webp(cover_fit(Image.open(png), size, top=True), out)
        return True


def capture_resource(chrome: Path, key: str, url: str, force: bool) -> str:
    out = OUT_RES / f"{key}.webp"
    if out.exists() and not force:
        return f"skip  {key}"
    try:
        page = fetch(url).decode("utf-8", "ignore")
        for tag in OG_RE.findall(page):
            m = CONTENT_RE.search(tag)
            if not m:
                continue
            img_url = urljoin(url, html.unescape(m.group(1)))
            img = Image.open(io.BytesIO(fetch(img_url)))
            if img.width < 300:
                continue
            save_webp(cover_fit(img, OG_SIZE), out)
            return f"og    {key}"
    except Exception as e:  # noqa: BLE001 - fall through to screenshot
        print(f"  og failed {key}: {e}", file=sys.stderr)
    return f"shot  {key}" if screenshot(chrome, url, out, size=OG_SIZE) else f"FAIL  {key}"


def capture_style(chrome: Path, page: Path, force: bool) -> str:
    out = OUT_STYLES / f"{page.stem}.webp"
    if out.exists() and not force:
        return f"skip  {page.stem}"
    return f"shot  {page.stem}" if screenshot(chrome, page.as_uri(), out, 4000) else f"FAIL  {page.stem}"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", choices=["res", "styles"])
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()
    chrome = find_chrome()
    with ThreadPoolExecutor(max_workers=6) as pool:
        jobs = []
        if args.only in (None, "res"):
            jobs += [pool.submit(capture_resource, chrome, k, u, args.force) for k, u in RESOURCES.items()]
        if args.only in (None, "styles"):
            jobs += [pool.submit(capture_style, chrome, p, args.force) for p in sorted((ROOT / "styles").glob("*.html"))]
        for j in jobs:
            print(j.result())


if __name__ == "__main__":
    main()
