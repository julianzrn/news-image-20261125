#!/usr/bin/env python3
"""Sum up 25 November 2026's world news in one image (make.fun entry).

Renders a one-page wire-service news summary -- a dated header, a lead
story with a large photograph, three secondary stories in a uniform
three-column grid, and a text brief -- from real news photographs
stored beside this file in ``assets/``.

Layout is the 24 November v4 sheet, reused unchanged (the user
approved that density): margins 30 px, column gaps 20 px, lead
photograph 496x296 with the standfirst running its full height,
secondary photographs 308x190 in a uniform three-column grid, one
block order in every cell (photo -> caption -> kicker -> headline ->
summary), and a text-only brief band under the grid that fills the
bottom of the page. Only the date, the stories and the photographs
are new. The folio reads WEDNESDAY, 25 NOVEMBER 2026.

Every story was reported on 25 Nov 2026 by at least two major
outlets (see candidates.md for the per-story source log). Claims
from one side only are attributed in the copy: the Houthis' Ras
Tanura strike is reported as their claim, with the coalition's
account beside it. Photographs are file images and are captioned
as such. Nothing from the 24 November entry is reused: no 24 Nov
story, no 24 Nov photograph.

The program uses no network, no clock and no randomness; it runs
twice and writes byte-identical output to /output/entry.png.
"""

import os

from PIL import Image, ImageDraw, ImageFont, ImageOps

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, "assets")
OUTPUT = "/output/entry.png"

W, H = 1024, 1024
MARGIN = 30
RIGHT = W - MARGIN
CONTENT_W = RIGHT - MARGIN

PAPER = (247, 244, 236)
INK = (18, 18, 18)
RED = (146, 24, 20)
GRAY = (96, 90, 80)
HAIRLINE = (60, 58, 52)

FONT_DIR = "/usr/share/fonts/truetype"
SERIF_DISPLAY_BOLD = [
    f"{FONT_DIR}/noto/NotoSerifDisplay-Bold.ttf",
    f"{FONT_DIR}/noto/NotoSerif-Bold.ttf",
    f"{FONT_DIR}/dejavu/DejaVuSerif-Bold.ttf",
    f"{FONT_DIR}/liberation/LiberationSerif-Bold.ttf",
]
SERIF_BOLD = [
    f"{FONT_DIR}/noto/NotoSerif-Bold.ttf",
    f"{FONT_DIR}/dejavu/DejaVuSerif-Bold.ttf",
    f"{FONT_DIR}/liberation/LiberationSerif-Bold.ttf",
]
SERIF = [
    f"{FONT_DIR}/noto/NotoSerif-Regular.ttf",
    f"{FONT_DIR}/dejavu/DejaVuSerif.ttf",
    f"{FONT_DIR}/liberation/LiberationSerif-Regular.ttf",
]
SERIF_ITALIC = [
    f"{FONT_DIR}/noto/NotoSerif-Italic.ttf",
    f"{FONT_DIR}/dejavu/DejaVuSerif-Italic.ttf",
    f"{FONT_DIR}/liberation/LiberationSerif-Italic.ttf",
]
SANS_BOLD = [
    f"{FONT_DIR}/noto/NotoSans-Bold.ttf",
    f"{FONT_DIR}/dejavu/DejaVuSans-Bold.ttf",
    f"{FONT_DIR}/liberation/LiberationSans-Bold.ttf",
]
SANS = [
    f"{FONT_DIR}/noto/NotoSans-Regular.ttf",
    f"{FONT_DIR}/dejavu/DejaVuSans.ttf",
    f"{FONT_DIR}/liberation/LiberationSans-Regular.ttf",
]

# ---------------------------------------------------------------- copy

TITLE = "The World in One Image"
FOLIO_LEFT = "WEDNESDAY, 25 NOVEMBER 2026"
FOLIO_RIGHT = "COMPILED FROM WIRE REPORTS"

LEAD_KICKER = "WASHINGTON"
LEAD_HEADLINE = "U.S. Proposes New Tariffs on 14 Trading Partners"
LEAD_STANDFIRST = (
    "The Trump administration on Wednesday proposed new tariffs on "
    "14 major trading partners, including China, the European Union "
    "and Japan, after an eight-month inquiry into what Washington "
    "calls structural excess industrial capacity. China would face "
    "the highest rates, a proposed 20 per cent duty on top of "
    "roughly 25 per cent from the president's first term. The duties "
    "face a public comment period and a hearing, and may not take "
    "effect until January. Beijing called overcapacity a 'false "
    "issue'."
)
LEAD_PHOTO = "lead_tariffs.jpg"
LEAD_CENTERING = (0.5, 0.5)
LEAD_CAPTION = "Container ships at a port. (File photograph)"

STORIES = [
    {
        "kicker": "RAS TANURA",
        "headline": "Houthis Say They Hit the Ras Tanura Refinery",
        "summary": (
            "Yemen's Houthis said on Wednesday they had attacked the "
            "Ras Tanura refinery. The coalition said four drones "
            "were destroyed over the site and did not confirm a hit. "
            "Satellite images showed thick black smoke."
        ),
        "photo": "ras_tanura.jpg",
        "centering": (0.5, 0.5),
        "caption": "The Ras Tanura refinery. (File photograph)",
    },
    {
        "kicker": "JIUQUAN",
        "headline": "Pakistani Astronaut Boards China's Space Station",
        "summary": (
            "Muhammad Zeeshan Ali on Wednesday became the first "
            "foreign astronaut to board the Tiangong station, "
            "arriving on Shenzhou-24 with Tang Hongbo and Wu Yi. "
            "He will spend a week in orbit."
        ),
        "photo": "shenzhou.jpg",
        "centering": (0.5, 0.45),
        "caption": "A Shenzhou crew lifts off. (File photograph)",
    },
    {
        "kicker": "CANBERRA",
        "headline": "Solomon Islands Names Australia Its Security Partner",
        "summary": (
            "Solomon Islands signed a treaty in Canberra on Wednesday "
            "making Australia its primary security partner, with no "
            "foreign military bases. Australia will provide A$740 "
            "million over ten years."
        ),
        "photo": "canberra.jpg",
        "centering": (0.5, 0.5),
        "caption": "Parliament House in Canberra. (File photograph)",
    },
]

BRIEF_KICKER = "UKRAINE"
BRIEF_HEADLINE = "Strikes Cut Power Across Five Regions"
BRIEF_SUMMARY = (
    "Russian strikes killed at least five people and cut power in "
    "five regions, Ukrainian officials said, and the Zaporizhzhia "
    "nuclear plant lost external power and switched to diesel "
    "generators. A Ukrainian drone attack in Russia's Samara region "
    "killed one person and cut power there."
)

FOOTER = (
    "Reporting: Reuters · Al Jazeera · Associated Press · CNN · "
    "Nikkei Asia — Photographs are file images, as captioned."
)

# ---------------------------------------------------------------- text


def load_font(paths, size):
    for path in paths:
        if os.path.exists(path):
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def wrap(draw, text, font, width):
    """Greedy word wrap; returns the list of lines."""
    lines, current = [], ""
    for word in text.split():
        trial = word if not current else current + " " + word
        if draw.textlength(trial, font=font) <= width:
            current = trial
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def draw_lines(draw, x, y, lines, font, fill, line_height):
    for line in lines:
        draw.text((x, y), line, font=font, fill=fill)
        y += line_height
    return y


def paste_photo(page, name, box, centering=(0.5, 0.5)):
    """Cover-fit the asset into box (x, y, w, h) without distortion."""
    x, y, w, h = box
    path = os.path.join(ASSETS, name)
    photo = Image.open(path).convert("RGB")
    fitted = ImageOps.fit(photo, (w, h), method=Image.LANCZOS, centering=centering)
    page.paste(fitted, (x, y))

# ---------------------------------------------------------------- page


def draw_header(d):
    f_folio = load_font(SANS_BOLD, 13)
    f_folio_r = load_font(SANS, 13)
    d.text((MARGIN, 12), FOLIO_LEFT, font=f_folio, fill=INK)
    w = d.textlength(FOLIO_RIGHT, font=f_folio_r)
    d.text((RIGHT - w, 12), FOLIO_RIGHT, font=f_folio_r, fill=GRAY)
    d.line([(MARGIN, 31), (RIGHT, 31)], fill=INK, width=1)

    f_title = load_font(SERIF_BOLD, 36)
    w = d.textlength(TITLE, font=f_title)
    d.text(((W - w) / 2, 39), TITLE, font=f_title, fill=INK)

    d.line([(MARGIN, 88), (RIGHT, 88)], fill=INK, width=2)
    d.line([(MARGIN, 93), (RIGHT, 93)], fill=INK, width=1)
    return 108


def draw_lead(page, d, top):
    f_kicker = load_font(SANS_BOLD, 15)
    d.text((MARGIN, top), LEAD_KICKER, font=f_kicker, fill=RED)
    y = top + 24

    f_head = load_font(SERIF_DISPLAY_BOLD, 36)
    lines = wrap(d, LEAD_HEADLINE, f_head, CONTENT_W)
    y = draw_lines(d, MARGIN, y, lines, f_head, INK, 41)
    y += 10

    photo_w, photo_h = 496, 296
    photo_x = RIGHT - photo_w
    paste_photo(page, LEAD_PHOTO, (photo_x, y, photo_w, photo_h),
                centering=LEAD_CENTERING)
    f_cap = load_font(SERIF_ITALIC, 13)
    cap_lines = wrap(d, LEAD_CAPTION, f_cap, photo_w)
    cap_end = draw_lines(d, photo_x, y + photo_h + 6, cap_lines,
                         f_cap, GRAY, 16)

    text_w = photo_x - MARGIN - 20
    f_stand = load_font(SERIF, 18)
    stand_lines = wrap(d, LEAD_STANDFIRST, f_stand, text_w)
    text_end = draw_lines(d, MARGIN, y, stand_lines, f_stand, INK, 26)

    bottom = max(cap_end, text_end) + 8
    d.line([(MARGIN, bottom), (RIGHT, bottom)], fill=INK, width=2)
    return bottom + 14


def draw_cell(page, d, story, x, y, w):
    photo_h = 190
    paste_photo(page, story["photo"], (x, y, w, photo_h),
                centering=story["centering"])
    cy = y + photo_h + 5

    f_cap = load_font(SERIF_ITALIC, 13)
    cap_lines = wrap(d, story["caption"], f_cap, w)
    cy = draw_lines(d, x, cy, cap_lines, f_cap, GRAY, 15)
    cy += 5

    f_kicker = load_font(SANS_BOLD, 13)
    d.text((x, cy), story["kicker"], font=f_kicker, fill=RED)
    cy += 17

    f_head = load_font(SERIF_BOLD, 20)
    head_lines = wrap(d, story["headline"], f_head, w)
    cy = draw_lines(d, x, cy, head_lines, f_head, INK, 23)
    cy += 3

    f_sum = load_font(SERIF, 15)
    sum_lines = wrap(d, story["summary"], f_sum, w)
    cy = draw_lines(d, x, cy, sum_lines, f_sum, INK, 19)
    return cy


def draw_grid(page, d, top):
    gap = 20
    col_w = (CONTENT_W - 2 * gap) // 3
    col_x = [MARGIN, MARGIN + col_w + gap, MARGIN + 2 * (col_w + gap)]

    bottom = top
    for i, story in enumerate(STORIES):
        end = draw_cell(page, d, story, col_x[i], top, col_w)
        bottom = max(bottom, end)

    for gx in (col_x[1] - gap // 2, col_x[2] - gap // 2):
        d.line([(gx, top), (gx, bottom)], fill=HAIRLINE, width=1)
    return bottom


def draw_brief(d, top):
    d.line([(MARGIN, top), (RIGHT, top)], fill=HAIRLINE, width=1)
    y = top + 8

    f_kicker = load_font(SANS_BOLD, 13)
    d.text((MARGIN, y), BRIEF_KICKER, font=f_kicker, fill=RED)

    f_head = load_font(SERIF_BOLD, 19)
    head_lines = wrap(d, BRIEF_HEADLINE, f_head, 420)
    head_end = draw_lines(d, MARGIN, y + 17, head_lines, f_head, INK, 22)

    sum_x = MARGIN + 448
    f_sum = load_font(SERIF, 14)
    sum_lines = wrap(d, BRIEF_SUMMARY, f_sum, RIGHT - sum_x)
    sum_end = draw_lines(d, sum_x, y + 2, sum_lines, f_sum, INK, 18)
    return max(head_end, sum_end)


def draw_footer(d, top):
    d.line([(MARGIN, top), (RIGHT, top)], fill=HAIRLINE, width=1)
    f = load_font(SANS, 11)
    w = d.textlength(FOOTER, font=f)
    d.text(((W - w) / 2, top + 7), FOOTER, font=f, fill=GRAY)


def render():
    page = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(page)
    y = draw_header(d)
    y = draw_lead(page, d, y)
    y = draw_grid(page, d, y)
    y = draw_brief(d, y + 10)
    draw_footer(d, y + 8)
    return page


def main():
    page = render()
    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    page.save(OUTPUT, "PNG", optimize=True)
    print(f"wrote {OUTPUT}: {page.size[0]}x{page.size[1]}")


if __name__ == "__main__":
    main()
