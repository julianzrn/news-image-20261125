# Sum up 25 November's world news in one image

A program that writes one image summarising the world's news of Wednesday,
25 November 2026, in the style of a newspaper front page: one lead story
(U.S. proposes new tariffs on 14 trading partners) with a container-port
photograph, three more stories in a grid (Houthis say they hit the Ras Tanura
refinery; a Pakistani astronaut boards China's space station; Solomon Islands
names Australia its security partner), and a brief on the Russian strikes
that cut power across five regions of Ukraine.

Run `python3 main.py` to write the image to `/output/entry.png`
(1024×1024 PNG, under 1 MiB). The run is deterministic: two runs produce
byte-identical output. All photographs are file photographs, captioned as
such; every story was verified against at least two major news outlets
before it was written in (see `candidates.md`).

Entry for the make.fun competition `news-image-20261125`.
