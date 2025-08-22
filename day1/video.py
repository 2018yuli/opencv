import cv2
import numpy as py

vc = cv2.VideoCapture("./assets/test.mp4")

if vc.isOpened():
    open, frame = vc.read()
else:
    open = False

while open:
    ret, frame = vc.read()
    if frame is None:
        break
    if ret == True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('result', gray)
        # 每帧等待时间
        if cv2.waitKey(100) & 0xFF == 27: # 在 虚拟机上，而不是控制台，退出键 ESC
            break
vc.release()
cv2.destroyAllWindows()