from window.window_shoot import WindowCapture
from tools.rect_detect import RectDetect, Rect, RectRange
from PyQt5.QtWidgets import QApplication
import sys

app = QApplication(sys.argv)
screen = QApplication.primaryScreen()
window_capture = WindowCapture("钉钉", screen)
img = window_capture.window_capture()
img.save("../screenshot.jpg")

# 110 510 30 30
# 3860727491662
rect_detect = RectDetect()
rect = Rect(30, 30, 3860727491662)
rect.feature_1 = 4279304482
rect.feature_2 = 4287658348
rect.offset_x2 = 15
rect.offset_y2 = 15
rect.feature_3 = 4288492093

# 寻找范围 不是每个像素都找的
rect_range = RectRange(0, 0, 1000, 1000)
print(rect_detect.detect(img, rect, rect_range))
