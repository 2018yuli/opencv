import cv2
import matplotlib.pyplot as plt
import numpy as py

# BGR
img = cv2.imread('./assets/1.jpg')


# 图像的 shape (RGB)
print(img.shape)

# 转换成 灰度图
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

print("灰度图的sharp", gray_img.shape)

# 图像的类型
print(type(img))

# 图像的大小
print(img.size)


cv2.imshow("img", img)
cv2.imshow("gray_img", gray_img)
cv2.waitKey(10_000)
cv2.destroyAllWindows()