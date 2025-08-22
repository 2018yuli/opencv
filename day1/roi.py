import cv2
import numpy as py

# BGR
img = cv2.imread('./assets/1.jpg')

part = img[0:200, 0:200]
cv2.imshow('part', part)

# 颜色通道提取



i

if cv2.waitKey(10_000) & 0xFF == 27:
    cv2.destroyAllWindows()