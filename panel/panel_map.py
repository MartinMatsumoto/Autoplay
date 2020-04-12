from PyQt5.QtWidgets import QWidget, QTabWidget, QCheckBox, QApplication, QGridLayout
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt


class PanelMap(QWidget):
    curr_map = None

    def __init__(self):
        super().__init__()
        self.curr_map = MapInfo()
        self.pen = QPen(Qt.black, 2, Qt.SolidLine)

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.draw_lines(qp)
        qp.end()

    def draw_lines(self, qp):
        # pen.setStyle(Qt.DashLine)
        # pen.setStyle(Qt.DashDotLine)
        # pen.setStyle(Qt.DotLine)
        # pen.setStyle(Qt.DashDotDotLine)
        qp.setPen(self.pen)
        for node in self.curr_map.map_nodes:
            try:
                qp.drawLine(node.x1 / 10 + self.curr_map.center_x / 10,
                            node.y1 / 10 + self.curr_map.center_y / 10,
                            node.x2 / 10 + self.curr_map.center_x / 10,
                            node.y2 / 10 + self.curr_map.center_y / 10)
            except Exception as e:
                print(e)
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
