#!/usr/bin/env python3
"""Chroma-key the green background out of paper-puppet PNGs (Plan WP-I; BC-137).

Usage: python3 tools/keyout.py <src.png> <dst.png> [--low N] [--high N] [--preview out.jpg]

The image models return a *near*-green background (G 185-240, R/B < 45) that varies
per image, so the key is on greenness = G - max(R, B) rather than an exact colour:
  greenness <= LOW  -> fully opaque (foreground)
  greenness >= HIGH -> fully transparent (background)
  between           -> linear alpha ramp (anti-aliased edge)
Fringe pixels are despilled (G pulled down toward max(R, B)). A small erosion of the
alpha matte removes the 1-px halo that soft edges leave on a chroma plate.
"""
import argparse
import numpy as np
from PIL import Image, ImageFilter

def key(src, dst, low=60, high=120, preview=None, edge=10):
    im = Image.open(src).convert('RGBA')
    a = np.asarray(im).astype(np.int16)
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    greenness = g - np.maximum(r, b)
    alpha = np.clip(1.0 - (greenness - low) / float(high - low), 0.0, 1.0)
    alpha[greenness <= low] = 1.0
    alpha[greenness >= high] = 0.0
    # erode the matte by one pixel to kill the green halo, then keep the soft ramp
    matte = Image.fromarray((alpha * 255).astype(np.uint8))
    matte = matte.filter(ImageFilter.MinFilter(3))
    alpha = np.asarray(matte).astype(np.float32) / 255.0
    # despill, edge-aware: green light bleeds into hair and cloth along the silhouette,
    # so within EDGE px of the matte edge cap green hard; inside the figure only cap
    # strong spill so olive/green clothing keeps its colour.
    m = np.maximum(r, b)
    edge_mask = Image.fromarray(((alpha < 1.0) * 255).astype(np.uint8)).filter(ImageFilter.MaxFilter(2 * edge + 1))
    near_edge = np.asarray(edge_mask) > 0
    g_edge = np.minimum(g, m + 6)
    g_core = np.where((g - m) > 25, np.minimum(g, m + 20), g)
    g2 = np.where(near_edge, g_edge, g_core)
    out = np.stack([r, g2, b, (alpha * 255).round()], axis=-1).clip(0, 255).astype(np.uint8)
    Image.fromarray(out, 'RGBA').save(dst, optimize=True)
    if preview:
        h, w = out.shape[:2]
        bg = np.zeros((h, w, 3), np.uint8)
        ys, xs = np.mgrid[0:h, 0:w]
        bg[((ys // 32 + xs // 32) % 2) == 0] = 70
        bg[((ys // 32 + xs // 32) % 2) == 1] = 30
        fg = out[..., :3].astype(np.float32); al = out[..., 3:4].astype(np.float32) / 255.0
        comp = (fg * al + bg * (1 - al)).astype(np.uint8)
        Image.fromarray(comp).resize((w // 2, h // 2)).save(preview, quality=82)
    return float((alpha == 0).mean()), float(((alpha > 0) & (alpha < 1)).mean())

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('src'); p.add_argument('dst')
    p.add_argument('--low', type=int, default=60); p.add_argument('--high', type=int, default=120)
    p.add_argument('--preview'); p.add_argument('--edge', type=int, default=10)
    ns = p.parse_args()
    t, s = key(ns.src, ns.dst, ns.low, ns.high, ns.preview, ns.edge)
    print(f'{ns.dst}: transparent {t*100:.1f}%  soft-edge {s*100:.2f}%')
