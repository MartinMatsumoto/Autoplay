from PyQt5.QtWidgets import QWidget, QTabWidget, QCheckBox, QApplication, QGridLayout
from PyQt5.QtGui import QPainter, QPen, QPaintEvent, QColor
from PyQt5.QtCore import Qt


class PanelMap(QWidget):
    curr_map = None

    def __init__(self):
        super().__init__()
        self.curr_map = MapInfo()
        self.pen = QPen(Qt.black, 1, Qt.SolidLine)

    def reload_map(self, curr_map):
        self.curr_map = curr_map
        self.update()

    def paintEvent(self, e: QPaintEvent):
        qp = QPainter(self)
        # 反锯齿
        qp.setRenderHint(QPainter.Antialiasing)
        qp.begin(self)
        self.draw_lines(qp)
        qp.end()

    def draw_lines(self, qp):
        # pen.setStyle(Qt.DashLine)
        # pen.setStyle(Qt.DashDotLine)
        # pen.setStyle(Qt.DotLine)
        # pen.setStyle(Qt.DashDotDotLine)
        qp.setPen(self.pen)

        i = 0
        for node in self.curr_map.map_nodes:
            # if i % 2 == 0:
            #     self.pen.setColor(QColor(255, 182, 193))
            # else:
            #     self.pen.setColor(Qt.blue)

            try:
                qp.drawLine(node.x1 / 3 + self.curr_map.center_x / 3,
                            node.y1 / 3 + self.curr_map.center_y / 3,
                            node.x2 / 3 + self.curr_map.center_x / 3,
                            node.y2 / 3 + self.curr_map.center_y / 3)
                qp.drawText(node.x2 / 3, node.y2 / 3, str(i))
            except Exception as e:
                print(e)
            i += 1
        qp.end()


class MapInfo:
    map_nodes: list = []
    center_x: float = 0
    center_y: float = 0
    map_name: str
    map_code: str


class MapNode:
    x1: float
    x2: float
    y1: float
    y2: float
    prev: float
    next: float
    forbid_fall_down: int

    def __init__(self):
        return
