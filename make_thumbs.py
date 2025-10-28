#!/usr/bin/env python3
"""
make_thumbs.py
Create 400px-wide thumbnails for images in /assets/img/ → /assets/thumbs/
- Keeps the same filenames
- Maintains aspect ratio
- Skips images that already have a thumbnail (unless --force)
- Handles PNG/JPG/JPEG/WebP; skips SVG/GIF by default
"""

import argparse
import sys
from pathlib import Path
from PIL import Image, ImageOps

SUPPORTED_EXT = {".png", ".jpg", ".jpeg", ".webp"}

def safe_exif_transpose(im):
    """
    Safely apply EXIF-based orientation transpose if available.
    Works with older Pillow versions that may not have ImageOps.exif_transpose.
    Returns the original image if not applicable.
    """
    try:
        exif_transpose = getattr(ImageOps, "exif_transpose", None)
        if callable(exif_transpose):
            return exif_transpose(im)
    except Exception:
        # Older Pillow or images without valid EXIF; just return as-is
        pass
    return im

def make_thumb(src_path: Path, dst_path: Path, width: int, force: bool = False, verbose: bool = True, exif_fix: bool = True):
    if not force and dst_path.exists():
        if verbose:
            print(f"SKIP (exists): {dst_path}")
        return

    try:
        with Image.open(src_path) as im:
            # Respect EXIF orientation (for JPEGs, etc.)
            if exif_fix:
                im = safe_exif_transpose(im)

            # Only downscale if wider than target width
            if im.width > width:
                ratio = width / float(im.width)
                new_size = (width, int(round(im.height * ratio)))
                im = im.resize(new_size, Image.LANCZOS)

            # Ensure destination folder exists
            dst_path.parent.mkdir(parents=True, exist_ok=True)

            ext = src_path.suffix.lower()
            if ext in {".jpg", ".jpeg"}:
                # Convert to RGB (JPEG doesn’t support alpha)
                if im.mode not in ("RGB", "L"):
                    im = im.convert("RGB")
                im.save(dst_path, format="JPEG", quality=88, optimize=True, progressive=True)
            elif ext == ".png":
                # Preserve alpha for PNG
                if im.mode not in ("RGBA", "RGB", "L", "LA"):
                    im = im.convert("RGBA")
                im.save(dst_path, format="PNG", optimize=True)
            elif ext == ".webp":
                # Keep alpha if present
                lossless = im.mode in ("RGBA", "LA")
                im.save(dst_path, format="WEBP", quality=88, method=6, lossless=lossless)
            else:
                # Fallback (shouldn’t hit due to filter)
                im.save(dst_path)

            if verbose:
                print(f"OK  → {dst_path}")

    except Exception as e:
        print(f"ERROR processing {src_path}: {e}", file=sys.stderr)

def main():
    parser = argparse.ArgumentParser(description="Generate thumbnails in /assets/thumbs/ with same filenames.")
    parser.add_argument("--src", default="assets/img", help="Source image directory (default: assets/img)")
    parser.add_argument("--dst", default="assets/thumbs", help="Destination thumbs directory (default: assets/thumbs)")
    parser.add_argument("--width", type=int, default=400, help="Thumbnail width in pixels (default: 400)")
    parser.add_argument("--force", action="store_true", help="Overwrite existing thumbnails")
    parser.add_argument("--quiet", action="store_true", help="Reduce output")
    parser.add_argument("--no-recursive", action="store_true", help="Do not scan subfolders")
    parser.add_argument("--no-exif-fix", action="store_true", help="Disable EXIF orientation correction (useful for very old Pillow)")
    args = parser.parse_args()

    src = Path(args.src)
    dst = Path(args.dst)
    if not src.exists():
        print(f"Source folder not found: {src}", file=sys.stderr)
        sys.exit(1)

    exif_fix = not args.no_exif_fix
    if exif_fix and not getattr(ImageOps, "exif_transpose", None) and not args.quiet:
        print("Note: EXIF orientation fix not available in this Pillow version; proceeding without it.", file=sys.stderr)

    globber = src.rglob if not args.no_recursive else src.glob
    count = 0

    for p in globber("*"):
        if p.is_dir():
            continue
        ext = p.suffix.lower()
        if ext not in SUPPORTED_EXT:
            # Skip SVG/GIF/etc.
            continue
        # Don’t recurse into thumbs output itself
        try:
            p.relative_to(dst)
            # If this succeeds, it's inside the thumbs folder—skip
            continue
        except ValueError:
            pass

        rel = p.relative_to(src)
        out = dst / rel
        make_thumb(p, out, width=args.width, force=args.force, verbose=not args.quiet, exif_fix=exif_fix)
        count += 1

    if not args.quiet:
        print(f"\nProcessed up to {count} files.")

if __name__ == "__main__":
    main()