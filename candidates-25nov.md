# News-image 25 Nov 2026 — research prep (not a submission)

Prepared 2026-11-26 ~08:53 Asia/Shanghai, for the make.fun contest
`news-image-20261125` — "Sum up 25 November's world news in one image".

## Contest facts (from competitions-open.json snapshot, read 2026-11-26)

- Slug: `news-image-20261125`, $100 pool, top 50 share ($20 / $12 / $6, then $2 / $1.20).
- Deadline: **2026-11-27T00:00:00Z = 2026-11-27 08:00 Asia/Shanghai**.
- Published 2026-11-25T00:00:00Z. Submission count in the snapshot: **2,202** (will have risen since).
- Rules (same as 24 Nov): public GitHub repo (or source bundle) created after
  opening, OSI licence, `main.py` (Python 3.13) or `main.ts` in root, writes one
  image to `/output/entry.png`; PNG/JPEG ≤1 MiB, ≤1024×1024; no network at run
  time; program runs twice, byte-identical; ≤10 submissions/day, 20 total,
  last before deadline counts; agent transcripts uploaded with submission.

## Correction to the 07:55 message today

The 24 Nov v4 **cannot** be submitted to this contest. v4 is dated
"TUESDAY, 24 NOVEMBER 2026" and covers 24 Nov stories (Hormuz 3 vessels,
Riyadh tower, Gaza Hamas security chief, Huawei verdict). This contest is
for **25 November** news. A fresh entry is needed; only the v4 layout/code
structure is reusable.

## What is reusable from v4 (verified 2026-11-26)

- File: `~/workspace/make-fun-entries/news-image-20261124/preview-entry-v4.png`
  (567,435 bytes, sha256 e5197c2f0b1b4bfc344db90d3da6b77d45c914ec5f0e7ef37f9cc4f87d27ccba)
  and `main.py` in the same folder (sha256 b4e4e47b…fe2ee).
- Layout to copy: margins 30 px, column gaps 20 px, lead photo 496×296 with
  text column running its full height, three secondaries in a uniform
  3-column grid (308×190 photos, same block order photo → caption → kicker
  → headline → summary), text-only brief band under the grid. Change folio
  to **WEDNESDAY, 25 NOVEMBER 2026**. Keep the v3/v4 rules the user set:
  real photographs shown whole (no halved subjects), photos matched to
  their stories, plain wire-style headlines, no invented newspaper nameplate.
- v4 assets (`assets/lead_hormuz.jpg`, `gaza_funeral.jpg`, `huawei.jpg`,
  `riyadh_pif.jpg`) are 24 Nov story photos — do **not** reuse them for
  25 Nov stories except a clearly captioned generic file photo, if at all.

## 25 Nov story candidates — researched 2026-11-26 morning (web search)

Confidence tiers matter: several 25 Nov items are so far only in secondary
round-ups / video briefings. The build step must re-check each chosen story
against two major outlets (Reuters / AP / Al Jazeera / BBC) before writing
copy, exactly as v2/v3 did. Do not copy headlines from Facebook reels.

### Strong — direct major-outlet reporting seen
1. **US proposes new tariffs on 14 trading partners** — Reuters, 25 Nov
   (https://www.reuters.com/world/china/us-proposes-new-tariffs-14-trading-partners-fight-excess-factory-capacity-2026-11-25/).
   Highest rates on China; framed as fighting excess industrial capacity.
   Good secondary/grid story; photo needs a real trade/port image.
2. **Pakistani astronaut first foreigner aboard China's Tiangong station**
   — Reuters, 25 Nov (Shenzhou-24 / Muhammad Zeeshan Ali). Distinctive,
   non-war story; good for the grid.
3. **Houthi drone hit Riyadh's tallest tower, second time in a week, 11 injured**
   — carried in Reuters Gulf piece 25 Nov
   (https://www.reuters.com/world/middle-east/where-are-gulfs-pledged-trillions-2026-11-25/)
   and Just Security Early Edition 25 Nov. This is a 24 Nov event still
   developing on 25 Nov; only use if the 25 Nov angle (second hit in a
   week / coalition response) is the headline, not a repeat of v4.
4. **Houthis claim attack on Ras Tanura refinery** — Just Security Early
   Edition 25 Nov (https://www.justsecurity.org/165910/early-edition-november-25-2026/)
   and OneTurn conflict brief 25 Nov; Houthi spokesman Yahya Saree said it
   caused fires; Saudi side said drones downed. Claim + counter-claim:
   headline must attribute ("Houthis say…"), do not state fires as fact.

### Usable with a second major-outlet check at build time
5. **Ukraine drones hit Samara refineries; Russian strikes hit power in five
   regions, at least 5 killed** — Just Security + EGazette daily brief 25 Nov
   (https://egazette.ai/daily/2026-11-25). Needs Reuters/AP confirmation of
   the casualty/region numbers before use.
6. **Australia–Solomon Islands security treaty ($740m aid, no foreign base)**
   — in several 25 Nov round-ups; needs a Reuters/AP/Guardian check at build
   time. If confirmed, a strong Pacific/diplomacy grid story.
7. **Zaporizhzhia nuclear plant lost external power, on diesel generators**
   — IAEA via EGazette 25 Nov brief. Needs IAEA/Reuters check; if confirmed,
   a strong text-only brief (no usable photo likely).
8. **Hormuz, 25 Nov update: IRGC says two tankers struck mines** — Just
   Security / EGazette. Claim only, no maritime authority confirmation.
   If used, attribute to IRGC and do not repeat v4's "three vessels" line.

### Do NOT use as 25 Nov stories
- **Huawei convicted 10 of 12 counts** — the verdict is 24 Nov news (v4
  already covered it); Reuters 25 Nov only carries it in a podcast recap.
  Reusing it as a 25 Nov headline would repeat yesterday's entry.
- **Gaza Hamas security chief killed** — 24 Nov story (v4). A second killing
  was reported in some 25 Nov round-ups (Naeem Abu Nahel + 6 others) — only
  use if separately verified as a distinct 25 Nov event, not the v4 one.
- **Sudan RSF drone strike, Damazin, 19 civilians dead** — only in a
  secondary video round-up so far; unverified for a headline. Brief-only
  at most, and only after a major-outlet check.
- **Leaked ~490,000 Russian war deaths** — single leaked-stats claim in
  OneTurn; do not headline.

## Blocker — checked 2026-11-26 ~08:50

- `gh auth status` in this VM: **"You are not logged into any GitHub hosts."**
  Yesterday's miss was exactly this step (repo never created). Local clones
  exist under `~/workspace/make-fun-work/repos/` (e.g. `one-line-one-chill`,
  remote `https://github.com/julianzrn/one-line-one-chill`), but no login
  state is present now, so creating/pushing `news-image-20261125` will fail
  until GitHub login is restored. Fix this **first**, before building, or
  the same last-minute failure repeats.
- The make.fun agent submission channel (local Solana keypair, local signing)
  worked for the 23 one-line entries; the submission step itself is not the
  blocker — the GitHub repo is.

## Suggested build order (for the main agent)

1. Restore GitHub login; create empty public repo `julianzrn/news-image-20261125`
   immediately (do not wait for the finished image).
2. Re-check stories 1–8 above against two major outlets each; drop any that
   fail; pick lead + 3 grid + 1 text brief.
3. Source real photos for the chosen stories only; view each photo against
   its story (v2/v3 rule); no halved subjects.
4. Adapt v4 `main.py`: new folio date, new copy, new assets; run twice,
   byte-identical sha256; render and visually inspect (no clipped text,
   photos whole, page filled).
5. Push, run the platform source check, submit — aim for the evening of
   2026-11-26, a full night before the 2026-11-27 08:00 deadline, not the
   last hour.
