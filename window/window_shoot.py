import time
import win32gui, win32ui, win32con, win32api
from PyQt5.QtWidgets import QApplication
import sys


class WindowCapture:

    def __init__(self, title_name):
        print("初始化窗口句柄")
        # 获取句柄
        self.hwnd = win32gui.FindWindow(0, title_name)
        # 获取窗口左上角和右下角坐标
        self.app = QApplication(sys.argv)
        # 根据窗口句柄获取窗口的设备上下文DC（Divice Context）
        self.screen = QApplication.primaryScreen()

    def window_capture(self):
        img = self.screen.grabWindow(self.hwnd).toImage()
        img.save("screenshot.jpg")
        return img
