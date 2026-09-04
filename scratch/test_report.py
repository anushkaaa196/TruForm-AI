import os
import sys
import time
from typing import Dict, Any, List, Tuple
from PIL import Image, ImageDraw, ImageFont

def get_font(size: int, bold: bool = False) -> ImageFont.ImageFont:
    font_names = (
        ["segoeuib.ttf", "arialbd.ttf", "segoeui.ttf", "arial.ttf"] if bold
        else ["segoeui.ttf", "arial.ttf"]
    )
    for fn in font_names:
        try:
            return ImageFont.truetype(fn, size)
        except Exception:
            continue
    return ImageFont.load_default()

def wrap_text(text: str, font: ImageFont.ImageFont, max_width: int, draw: ImageDraw.ImageDraw) -> List[str]:
    words = text.split()
    lines = []
    current: List[str] = []
    for word in words:
        test_line = " ".join(current + [word])
        bbox = draw.textbbox((0, 0), test_line, font=font)
        w = bbox[2] - bbox[0]
        if w <= max_width:
            current.append(word)
        else:
            if current:
                lines.append(" ".join(current))
                current = [word]
            else:
                lines.append(word)
                current = []
    if current:
        lines.append(" ".join(current))
    return lines

print("Test helpers defined successfully")
