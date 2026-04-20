from __future__ import annotations

from pathlib import Path
from textwrap import wrap

from PIL import Image, ImageDraw, ImageFont

WIDTH = 1200
HEIGHT = 630
BLUE = "#1a5490"
BLUE_DARK = "#103b66"
INK = "#162233"
MUTED = "#526173"
SOFT_BLUE = "#edf6fb"
SOFT_GREEN = "#eef8f2"

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_OUTPUT = ROOT / "site" / "public" / "assets" / "og.png"

FONT_CANDIDATES = {
    "serif": [
        "/System/Library/Fonts/ヒラギノ明朝 ProN.ttc",
        "/System/Library/Fonts/ヒラギノ明朝 ProN.ttc",
        "/System/Library/Fonts/Supplemental/Times New Roman.ttf",
    ],
    "sans": [
        "/System/Library/Fonts/ヒラギノ角ゴシック W6.ttc",
        "/System/Library/Fonts/ヒラギノ角ゴシック W6.ttc",
        "/System/Library/Fonts/AppleSDGothicNeo.ttc",
        "/System/Library/Fonts/Supplemental/Arial Unicode.ttf",
    ],
}


def _font(kind: str, size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    for candidate in FONT_CANDIDATES[kind]:
        path = Path(candidate)
        if path.exists():
            return ImageFont.truetype(str(path), size=size)
    return ImageFont.load_default(size=size)


def _draw_wrapped(draw: ImageDraw.ImageDraw, xy: tuple[int, int], text: str, font: ImageFont.ImageFont, fill: str, max_chars: int, line_gap: int) -> int:
    x, y = xy
    lines: list[str] = []
    for raw_line in text.splitlines():
        lines.extend(wrap(raw_line, max_chars) or [raw_line])
    for line in lines:
        draw.text((x, y), line, font=font, fill=fill)
        bbox = draw.textbbox((x, y), line, font=font)
        y += bbox[3] - bbox[1] + line_gap
    return y


def generate_og(output_path: str | Path = DEFAULT_OUTPUT) -> Path:
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)

    image = Image.new("RGB", (WIDTH, HEIGHT), "#ffffff")
    draw = ImageDraw.Draw(image)

    for y in range(HEIGHT):
        ratio = y / HEIGHT
        r = int(247 * (1 - ratio) + 238 * ratio)
        g = int(251 * (1 - ratio) + 248 * ratio)
        b = int(255 * (1 - ratio) + 242 * ratio)
        draw.line((0, y, WIDTH, y), fill=(r, g, b))

    draw.ellipse((820, -120, 1320, 380), fill="#dceff8")
    draw.ellipse((900, 210, 1210, 520), fill="#dcefe5")
    draw.rounded_rectangle((64, 60, 1136, 570), radius=28, fill="#fffffff2", outline="#c9ddec", width=2)

    serif = _font("serif", 58)
    sans_bold = _font("sans", 31)
    sans = _font("sans", 25)
    small = _font("sans", 21)

    draw.rounded_rectangle((104, 100, 318, 142), radius=8, fill=BLUE)
    draw.text((124, 108), "10本×13論点", font=small, fill="#ffffff")

    title = "「このAI、安全なんですか？」と患者に聞かれて、\n外来30秒で根拠を示せるように。"
    y = _draw_wrapped(draw, (104, 178), title, serif, INK, max_chars=17, line_gap=12)

    draw.text((104, y + 18), "医療AI 公開ガイドラインを、臨床の言葉で横断検索。", font=sans, fill=MUTED)
    draw.text((104, y + 58), "LLM非依存・静的検索 / 引用URL直リンク / ハルシネーションなし", font=sans, fill=MUTED)

    draw.rounded_rectangle((104, 474, 700, 520), radius=8, outline=BLUE, width=2, fill="#ffffff")
    draw.text((128, 484), "安全性  説明責任  バイアス  責任主体", font=sans_bold, fill=BLUE_DARK)

    draw.line((828, 142, 1038, 142), fill=BLUE, width=8)
    draw.line((828, 142, 828, 352), fill=BLUE, width=8)
    draw.arc((828, 232, 1038, 442), start=0, end=180, fill=BLUE, width=8)
    draw.ellipse((1010, 348, 1076, 414), outline=BLUE, width=8)
    draw.line((933, 352, 1010, 380), fill=BLUE, width=8)

    image.save(output, "PNG")
    return output


if __name__ == "__main__":
    generate_og()
