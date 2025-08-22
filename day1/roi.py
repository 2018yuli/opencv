import cv2
import numpy as py

# BGR
img = cv2.imread('./assets/1.jpg')

part = img[0:200, 0:200]
cv2.imshow('part', part)

# 颜色通道提取，注意不是 rgb
b, g, r = cv2.split(img)
print(b.shape)

# 只保留 R
cur_img = img.copy()
cur_img[:,:,0] = 0
cur_img[:,:,1] = 0
cv2.imshow('R', cur_img)


if cv2.waitKey(10_000) & 0xFF == 27:
    cv2.destroyAllWindows()