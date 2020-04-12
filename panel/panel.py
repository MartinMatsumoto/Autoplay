# 这里我们提供必要的引用。基本控件位于pyqt5.qtwidgets模块中。
from PyQt5.QtWidgets import QTabWidget
from PyQt5.QtWidgets import QApplication
from panel.panel_main import PanelMain
from panel.panel_map import PanelMap, MapInfo
from tools.ui_thread import UIThread


# QWidget部件是pyqt5所有用户界面对象的基类。他为QWidget提供默认构造函数。默认构造函数没有父类。
class Panel(QTabWidget):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.tab_main = PanelMain()
        self.tab_map = PanelMap()
        self.init_widget()
        self.ui_thread = UIThread(screen)
        self.init_worker_thread()
        # 显示在屏幕上
        self.show()

    def init_widget(self):
        # 创建2个选项卡小控件窗口
        self.addTab(self.tab_main, "设置")
        self.addTab(self.tab_map, "地图")
        # resize()方法调整窗口的大小。这离是250px宽150px高
        # w.resize(250, 150)
        # move()方法移动窗口在屏幕上的位置到x = 300，y = 300坐标。
        # w.move(300, 300)
        # 设置窗口的标题
        self.setWindowTitle('自动化脚本')

    def init_worker_thread(self):
        self.ui_thread.start()
        # 绑定增加控件函数
        self.ui_thread.reload_map.connect(self.map_nodes_receive)
        self.ui_thread.show_blood.connect(self.blood_receive)

    def map_nodes_receive(self, curr_map: MapInfo):
        self.tab_map.reload_map(curr_map)
        self.tab_main.set_map_name(curr_map.map_name)

    def blood_receive(self, blood: int, blue: int):
        self.tab_main.set_blood(blood, blue)
