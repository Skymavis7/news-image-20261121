// news-image-20261121 entry (Node 22, standard library only).
// The image is drawn once, deterministically, by make_image.py (Python + PIL,
// no network, no randomness, no timestamps) and stored as entry.png beside
// this file. This program copies those exact bytes to /output/entry.png, so
// every run writes the same bytes. Outside the grader's container,
// MAKEFUN_OUTPUT_DIR stands in for /output:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, existsSync, mkdirSync } from "node:fs";
import { join } from "node:path";
import { fileURLToPath } from "node:url";

const here = fileURLToPath(new URL(".", import.meta.url));
const out = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
const src = join(here, "entry.png");
const dst = join(out, "entry.png");

if (!existsSync(src)) {
  throw new Error(`entry.png not found beside main.ts (${src})`);
}
mkdirSync(out, { recursive: true });
copyFileSync(src, dst);
