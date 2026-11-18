# -*- coding: utf-8 -*-
"""One-off tool: a light touch on the hero photo — real detail and clarity,
not a color grade. The first pass (strong CLAHE + saturation) looked punchy
but stopped looking like the real island, and showed artifacts when zoomed.
This version barely touches color (a small, even contrast lift only — no
CLAHE, no saturation push) and spends its effort on a tight, small-radius
unsharp mask that sharpens actual texture (grass, rock) without the big soft
halos a wide-radius sharpen leaves around mountain silhouettes.
"""
import sys

import cv2
import numpy as np


def process(path_in, path_out, contrast=1.035, sharpen=0.45, radius=1.1):
    img = cv2.imread(path_in).astype(np.float32)

    # gentle, even S-curve — no CLAHE, so no locally-forced "fake HDR" contrast
    img = (img - 127.5) * contrast + 127.5
    img = np.clip(img, 0, 255).astype(np.uint8)

    # small-radius unsharp mask: sharpens fine texture, not big halos on skylines
    blur = cv2.GaussianBlur(img, (0, 0), radius)
    img = cv2.addWeighted(img, 1 + sharpen, blur, -sharpen, 0)

    cv2.imwrite(path_out, img, [cv2.IMWRITE_JPEG_QUALITY, 94])


if __name__ == "__main__":
    process(sys.argv[1], sys.argv[2])
