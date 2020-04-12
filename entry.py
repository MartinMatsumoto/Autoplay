# pip install opencv-python -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
# pip install PyQt5 -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
# pip install pypiwin32 -i http://pypi.douban.com/simple --trusted-host pypi.douban.com


from panel.panel import Panel
from PyQt5.QtWidgets import QApplication
import sys


# 每一pyqt5应用程序必须创建一个应用程序对象。sys.argv参数是一个列表，从命令行输入参数。
app = QApplication(sys.argv)
# 获取窗口左上角和右下角坐标
# 根据窗口句柄获取窗口的设备上下文DC（Divice Context）
screen = QApplication.primaryScreen()
panel = Panel(screen)
# 系统exit()方法确保应用程序干净的退出
# 的exec_()方法有下划线。因为执行是一个Python关键词。因此，exec_()代替
sys.exit(app.exec_())
