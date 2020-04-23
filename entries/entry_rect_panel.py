import sys
from PyQt5.QtWidgets import QApplication
from panel.panel_cut_rect import PanelCutRect
from window.window_shoot import WindowCapture

# 每一pyqt5应用程序必须创建一个应用程序对象。sys.argv参数是一个列表，从命令行输入参数。
app = QApplication(sys.argv)
# 获取窗口左上角和右下角坐标
# 根据窗口句柄获取窗口的设备上下文DC（Divice Context）

screen = QApplication.primaryScreen()
window_capture = WindowCapture("钉钉", screen)
img = window_capture.window_capture()
img.save("../screenshot.jpg")
panel_cut_rect = PanelCutRect(img)
panel_cut_rect.show()
# 系统exit()方法确保应用程序干净的退出
# 的exec_()方法有下划线。因为执行是一个Python关键词。因此，exec_()代替
sys.exit(app.exec_())
