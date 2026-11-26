# Build transcript — news-image-20261125

Competition: "Sum up 25 November's world news in one image" (make.fun,
$100 pool, entries close 2026-11-27T00:00:00Z). Built by an AI agent on
2026-11-26 (Asia/Shanghai). This file is a human-readable summary; the
authoritative record is the agent session transcript uploaded with the
submission bundle.

## Requirements read first

From the competition description and the 24 Nov entry's transcript:

- Entry is a program at `main.py` (Python 3.13) in the repo root that
  writes one image to `/output/entry.png`.
- Image: whole PNG or JPEG, at most 1 MiB, at most 1024x1024 px.
- No network at run time; the program runs twice and both runs must
  write the same bytes.
- Judged by a vision AI comparing images pairwise; the judge has no
  news feed, so the image itself must tell the day's story.
- Free entry; up to 10 submissions/day, 20 total; last one before the
  deadline counts.

## Research

The 24 Nov v4 entry cannot be submitted here: its date and its four
stories are all 24 Nov. Only its layout and code structure were reused.
Five 25 Nov stories were re-checked against two major outlets each
before any copy was written (full source log: candidates.md):

- U.S. tariffs on 14 trading partners — Reuters + Al Jazeera.
- Houthis say they struck the Ras Tanura refinery — Reuters + Gulf News
  (claim attributed; coalition counter-claim carried beside it).
- Pakistani astronaut boards Tiangong aboard Shenzhou-24 — Reuters +
  Dawn + Xinhua.
- Solomon Islands names Australia its security partner — Al Jazeera +
  CNN + Nikkei Asia + the Australian PM's office.
- Ukraine strikes cut power in five regions; Zaporizhzhia plant on
  diesel — Al Jazeera + Reuters (text-only brief; refinery names Reuters
  could not verify are not used).

Dropped: the Huawei verdict and the Gaza security-chief killing (both
24 Nov, already in the 24 Nov entry), the ~490,000 Russian deaths figure
(single leaked-stats claim), the Hormuz mines update (IRGC claim only),
and the Sudan Damazin strike (no major-outlet confirmation).

## Photographs

Four real file photographs, one per photo slot, each viewed against its
story before use: a container port (tariffs lead), the Ras Tanura
refinery and terminal, a Long March 2F launching a Shenzhou crew, and
Parliament House in Canberra. All are captioned as file photographs.
Sources are logged in candidates.md. No 24 Nov photograph was reused.

## Build

- `main.py` is the v4 renderer with new copy, a new folio date
  (WEDNESDAY, 25 NOVEMBER 2026) and new assets; layout, fonts and
  geometry are unchanged from the approved v4 sheet.
- The program was run twice; both runs wrote byte-identical PNGs
  (sha256 recorded below). Output is 1024x1024 and under 1 MiB.
- The render was visually inspected: no clipped text, photographs shown
  whole, page filled to the footer.

## Verification

Layout test (2026-11-26, stand-in photos only — the 24 Nov assets
copied under the new filenames in /tmp, NOT in this repo, to check
geometry and determinism without the real photos):

- Run 1 sha256: 7dd38868e8ab3197996d815678984647698a10df8e7e594c24e94a580c48539a
- Run 2 sha256: 7dd38868e8ab3197996d815678984647698a10df8e7e594c24e94a580c48539a
- Runs byte-identical: yes
- Output size: 585,292 bytes (1024x1024, under the 1 MiB limit)
- Geometry: lead bottom 523, grid bottom 899, brief bottom 991,
  footer text ends at y=1017 (7 px spare). The first render overflowed
  by 88 px; the grid summaries and the Ras Tanura headline were trimmed
  (facts unchanged, all still from the cited outlets) until the page fit.
- The render was visually inspected: no clipped text, photographs shown
  whole, page filled to the footer.

FINAL RENDER (with the real 25 Nov photos, 2026-11-26 09:13 CST):

- Run 1 sha256: d9d287b7a8f241714fc869d8954aa1f05f0ae421dd42a4274a6c64d43811b955
- Run 2 sha256: d9d287b7a8f241714fc869d8954aa1f05f0ae421dd42a4274a6c64d43811b955
- Runs byte-identical: yes
- Output size: 784,719 bytes (1024x1024, under the 1 MiB limit)
- Photos (all downloaded and visually verified, subjects whole, no watermarks): lead_tariffs.jpg (container port, sinotechmarine), ras_tanura.jpg (Ras Tanura refinery, Gulf News), shenzhou.jpg (Long March 2F night launch, Wikimedia Commons), canberra.jpg (Parliament House Canberra, Expatica backup link — the primary professionalplanner link hit a Cloudflare Turnstile block).
- The final render was visually inspected: no clipped text, photographs shown whole, page filled to the footer.

## Repo and submission

- Repo: https://github.com/julianzrn/news-image-20261125 (public)
- Commit SHA: (recorded at push — see below)

## Repo and submission

- Repo: https://github.com/julianzrn/news-image-20261125 (public)
- Commit SHA: (recorded at push — see below)
