# -*- coding: utf-8 -*-
"""One-off tool: the hero photo reads hazy (flat sky, muted hills/water) because
of real atmospheric haze in the shot, not just low saturation — a CSS filter
can punch up color but can't undo that flatness. This applies local contrast
(CLAHE, which is what actually cuts through haze), a saturation lift, a mild
S-curve for punch, and a light sharpen, baked into the file itself.
"""
import sys

import cv2
import numpy as np


def process(path_in, path_out, clahe_clip=2.6, sat_mult=1.38, contrast=1.08, sharpen=0.35):
    img = cv2.imread(path_in)
    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=clahe_clip, tileGridSize=(8, 8))
    l = clahe.apply(l)
    lab = cv2.merge([l, a, b])
    img = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV).astype(np.float32)
    hsv[:, :, 1] = np.clip(hsv[:, :, 1] * sat_mult, 0, 255)
    img = cv2.cvtColor(hsv.astype(np.uint8), cv2.COLOR_HSV2BGR)

    img = img.astype(np.float32)
    img = (img - 127.5) * contrast + 127.5
    img = np.clip(img, 0, 255).astype(np.uint8)

    blur = cv2.GaussianBlur(img, (0, 0), 3)
    img = cv2.addWeighted(img, 1 + sharpen, blur, -sharpen, 0)

    cv2.imwrite(path_out, img, [cv2.IMWRITE_JPEG_QUALITY, 92])


if __name__ == "__main__":
    process(sys.argv[1], sys.argv[2])
