import cv2

# 读取图像
image = cv2.imread('./assets/1.jpg')  # 替换为你图像的路径

# 检查图像是否加载成功
if image is None:
    print("Error: Unable to load image.")
else:
    # 显示图像
    cv2.imshow('Loaded Image', image)

    # 等待用户按键
    cv2.waitKey(0)

    # 关闭所有 OpenCV 窗口
    cv2.destroyAllWindows()
    
