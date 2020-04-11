import sys

# 这里我们提供必要的引用。基本控件位于pyqt5.qtwidgets模块中。
from PyQt5.QtWidgets import QWidget, QTabWidget, QCheckBox, QApplication, QGridLayout

from panel.panel_map import PanelMap


# QWidget部件是pyqt5所有用户界面对象的基类。他为QWidget提供默认构造函数。默认构造函数没有父类。
class Panel(QTabWidget):
    def __init__(self):
        super().__init__()
        # 每一pyqt5应用程序必须创建一个应用程序对象。sys.argv参数是一个列表，从命令行输入参数。
        self.app = QApplication(sys.argv)
        self.tab_choose = QWidget()
        self.tab_map = PanelMap()
        self.init_widget()
        self.init_ui()
        # 显示在屏幕上
        self.show()

        # 系统exit()方法确保应用程序干净的退出
        # 的exec_()方法有下划线。因为执行是一个Python关键词。因此，exec_()代替
        sys.exit(self.app.exec_())

    def init_widget(self):
        # 创建2个选项卡小控件窗口
        self.addTab(self.tab_choose, "选项卡1")
        self.addTab(self.tab_map, "选项卡2")
        # resize()方法调整窗口的大小。这离是250px宽150px高
        # w.resize(250, 150)
        # move()方法移动窗口在屏幕上的位置到x = 300，y = 300坐标。
        # w.move(300, 300)
        # 设置窗口的标题
        self.setWindowTitle('界面')

    def init_ui(self):
        grid = QGridLayout()
        grid.setSpacing(10)

        cb1 = QCheckBox('复选框1')
        cb1.stateChanged.connect(self.change_check_box)
        grid.addWidget(cb1)
        cb1.setDisabled(True)

        cb2 = QCheckBox('复选框2')
        cb2.stateChanged.connect(self.change_check_box)
        grid.addWidget(cb2)

        self.tab_choose.setLayout(grid)

    def change_check_box(self):
        print("点了checkbox")
