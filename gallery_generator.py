#!/usr/bin/env python3
"""
Generate a static AsciiDoc (.adoc) gallery page listing all .jpg images
in a specified folder.

Usage:
    python generate_gallery_adoc.py <image_folder> [output_file]

Example:
    python generate_gallery_adoc.py bildergalerie gallery.adoc
"""

import os
import sys

def generate_asciidoc(image_folder, output_file="gallery.adoc"):
    # Collect all .jpg files
    images = sorted(
        f for f in os.listdir(image_folder)
        if f.lower().endswith(".jpg")
    )

    if not images:
        print(f"No .jpg images found in folder: {image_folder}")
        return

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"= Bildergalerie\n")
        f.write(f":imagesdir: {image_folder}\n\n")
        f.write("== Galerie\n\n")

        for img in images:
            name = os.path.splitext(img)[0].replace("_", " ").title()
            f.write(f"image::{img}[{name}]\n+\n{name}\n\n")

    print(f"✅ Generated AsciiDoc file: {output_file}")
    print(f"📁 Images directory: {image_folder}")
    print(f"🖼️  {len(images)} images added.")

def main():
    if len(sys.argv) < 2:
        print("Usage: python generate_gallery_adoc.py <image_folder> [output_file]")
        sys.exit(1)

    image_folder = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else "gallery.adoc"

    if not os.path.isdir(image_folder):
        print(f"Error: folder not found – {image_folder}")
        sys.exit(1)

    generate_asciidoc(image_folder, output_file)

if __name__ == "__main__":
    main()
