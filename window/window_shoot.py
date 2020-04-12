import time
import win32gui, win32ui, win32con, win32api
from PyQt5.QtWidgets import QApplication
import sys


class WindowCapture:

    def __init__(self, title_name, screen):
        print("初始化窗口句柄")
        # 获取句柄
        self.hwnd = win32gui.FindWindow(0, title_name)
        self.screen = screen

    def window_capture(self):
        # map name
        # img = self.screen.grabWindow(self.hwnd, 45, 56, 250, 15).toImage()
        # blood
        # img = self.screen.grabWindow(self.hwnd, 610, 727, 170, 1).toImage()
        # img.save("screenshot.jpg")
        # blue
        # img = self.screen.grabWindow(self.hwnd, 610, 743, 170, 1).toImage()
        # img.save("screenshot.jpg")
        img = self.screen.grabWindow(self.hwnd).toImage()
        img.save("screenshot.jpg")
        return img
