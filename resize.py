from ast import walk
import cv2
import os
def resize(img):
    H, W = img.shape[0], img.shape[1]
    if H < W:
        W = 2 * H + 20
    else:
        H = W * 2 + 20
    return W, H
for _, pub, _ in os.walk("content/publication"): break

for p in pub:
    for _, _, files in os.walk(f"content/publication/{p}"): break
    img_name = None
    for f in files: img_name = f if f.startswith("featured") else img_name
    img = f"content/publication/{p}/{img_name}"
    img = cv2.imread(img)
    W, H = resize(img)
    img = cv2.resize(img, (W, H), interpolation=cv2.INTER_AREA)
    img = img[2:-2, 2:-2]  # 裁掉边上的一点, 避免出现黑边
    cv2.imwrite(f"content/publication/{p}/{img_name}", img)
    print("[img:", p, "]:", H, ",", W, ", 3")
    
