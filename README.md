[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/Skymavis7/news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/Skymavis7/news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

# The World in One Day — Saturday 21 November 2026

A single image summing up the world's news of Saturday 21 November 2026,
built for make.fun's news-image-20261121 bounty ($100). The image is
`entry.png` (1024×1024, PNG). It is drawn programmatically by
`make_image.py` (Python + PIL, no network, no randomness, no timestamps) and
`main.ts` copies those exact bytes to `/output/entry.png`, so every run
writes identical bytes.

## What the image shows

- **Lead — Iran strikes Bahrain.** Iran's Revolutionary Guards say they hit
  two US bases; Bahrain reports an industrial fire, no injuries, and air
  defences intercepting other attacks, as Gulf tensions flare.
- **Mexico — El Chapo Isidro captured.** Mexican forces seize the FBI
  most-wanted cartel boss Fausto Isidro Meza Flores in Sinaloa; at least 11
  dead in the violence that followed.
- **Climate — COP31 nears a deal.** The Antalya talks run past their
  deadline and close in on a final pact as nations wrestle over fossil fuels.
- **War — Russian ship burns.** A drone strike sets the cargo ship Sparta II
  ablaze in the Gulf of Finland; missiles also land in Poland.
- **Health — Dengue breakthrough.** Specially bred mosquitoes cut dengue in
  children by about 69% in a major Brazil study.

Sources: Reuters, AP, CNN, AFP — 21 November 2026.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
# writes out/entry.png (byte-identical on every run)
```

## License

MIT — see `LICENSE`.
