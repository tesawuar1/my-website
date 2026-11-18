# -*- coding: utf-8 -*-
"""One-off tool for the hero photo. Two earlier passes taught us what each
knob actually does:
  - CLAHE (local/adaptive contrast) was what caused the "weird when zoomed"
    artifacts — it forces contrast per-tile, which reads as fake/patchy up
    close. Left out entirely, on purpose.
  - A plain, uniform saturation lift is what makes the colors read as vivid
    island colors instead of the real haze — that part was never the
    problem, so it's back, just dialed to a level that still looks real.
  - A tight, small-radius unsharp mask sharpens actual texture (grass, rock)
    without the big soft halos a wide-radius sharpen leaves on skylines.
"""
import sys

import cv2
import numpy as np


def process(path_in, path_out, sat_mult=1.3, contrast=1.045, sharpen=0.45, radius=1.1):
    img = cv2.imread(path_in).astype(np.float32)

    # even, global S-curve — no CLAHE, so no per-tile "fake HDR" patchiness
    img = (img - 127.5) * contrast + 127.5
    img = np.clip(img, 0, 255).astype(np.uint8)

    # uniform saturation lift (HSV), not local — same effect everywhere in frame
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV).astype(np.float32)
    hsv[:, :, 1] = np.clip(hsv[:, :, 1] * sat_mult, 0, 255)
    img = cv2.cvtColor(hsv.astype(np.uint8), cv2.COLOR_HSV2BGR)

    # small-radius unsharp mask: sharpens fine texture, not big halos on skylines
    blur = cv2.GaussianBlur(img, (0, 0), radius)
    img = cv2.addWeighted(img, 1 + sharpen, blur, -sharpen, 0)

    cv2.imwrite(path_out, img, [cv2.IMWRITE_JPEG_QUALITY, 94])


if __name__ == "__main__":
    process(sys.argv[1], sys.argv[2])
