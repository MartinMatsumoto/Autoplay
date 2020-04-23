from window.window_shoot import WindowCapture
from tools.rect_detect import RectDetect, Rect, RectRange
from PyQt5.QtWidgets import QApplication
import sys

app = QApplication(sys.argv)
screen = QApplication.primaryScreen()
window_capture = WindowCapture("钉钉", screen)
img = window_capture.window_capture()
img.save("../screenshot.jpg")

rect_detect = RectDetect()
rect = Rect(50, 50)
rect_range = RectRange(0, 0, 50, 50)
rect_detect.detect(img, rect, rect_range)
