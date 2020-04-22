from PyQt5.QtWidgets import QWidget, QTabWidget, QCheckBox, QApplication, QGridLayout
from PyQt5.QtGui import QPainter, QPen, QPaintEvent, QColor
from PyQt5.QtCore import Qt


class PanelMap(QWidget):
    curr_map = None

    def __init__(self):
        super().__init__()
        self.curr_map = MapInfo()

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
        pen = QPen(Qt.black, 2, Qt.SolidLine)
        qp.setPen(pen)

        for node in self.curr_map.map_nodes:
            if node.forbid_fall_down == 1:
                pen.setColor(Qt.red)
                qp.setPen(pen)
            else:
                pen.setColor(Qt.black)
                qp.setPen(pen)
            qp.drawLine(node.x1 / 3 + self.curr_map.center_x / 3,
                        node.y1 / 3 + self.curr_map.center_y / 3,
                        node.x2 / 3 + self.curr_map.center_x / 3,
                        node.y2 / 3 + self.curr_map.center_y / 3)
            # qp.drawText(node.x2 / 3 + self.curr_map.center_x / 3, node.y2 / 3 + self.curr_map.center_y / 3,
            #             str(node.index))

        pen.setColor(Qt.blue)
        qp.setPen(pen)
        for map_rope in self.curr_map.map_ropes:
            qp.drawLine(map_rope.x / 3 + self.curr_map.center_x / 3,
                        map_rope.y1 / 3 + self.curr_map.center_y / 3,
                        map_rope.x / 3 + self.curr_map.center_x / 3,
                        map_rope.y2 / 3 + self.curr_map.center_y / 3)

        for map_portal in self.curr_map.map_portals:
            if map_portal.tm != 999999999:
                qp.drawEllipse(map_portal.x / 3 + self.curr_map.center_x / 3, map_portal.y / 3 + self.curr_map.center_y / 3,
                               2, 2)
                qp.drawText(map_portal.x / 3 + self.curr_map.center_x / 3, map_portal.y / 3 + self.curr_map.center_y / 3,
                            str(map_portal.index))

        qp.end()


class MapInfo:
    map_nodes: list = []
    map_ropes: list = []
    map_portals: list = []
    center_x: float = 0
    center_y: float = 0
    map_name: str
    map_code: str


class MapNode:
    x1: float
    x2: float
    y1: float
    y2: float
    prev: int
    next: int
    index: int
    forbid_fall_down: int = 0


class MapRope:
    x: float
    y1: float
    y2: float
    index: int


class MapPortal:
    x: float
    y: float
    index: int
    tm: int
