from PyQt5.QtCore import QRect
from PyQt5.QtGui import QPainter, QPaintEvent, QImage
from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout, QLabel, QLineEdit


class PanelCutRect(QWidget):
    img: QImage = None
    default_num: int = 50
    x: int = default_num
    y: int = default_num
    width: int = default_num
    height: int = default_num

    def __init__(self, img: QImage):
        super().__init__()
        self.grid = QGridLayout()
        self.grid.setSpacing(5)
        self.img = img
        self.x_edit = QLineEdit(self)
        self.y_edit = QLineEdit(self)
        self.width_edit = QLineEdit(self)
        self.height_edit = QLineEdit(self)
        self.total_edit = QLineEdit(self)

        self.init_widget()

    def init_widget(self):
        # 出现位置
        # self.setGeometry(700, 700, 250, 150)
        # 设置大小
        self.resize(700, 700)

        x_label = QLabel(self)
        x_label.setText("x：")
        x_label.move(10, 15)
        self.x_edit.move(70, 10)
        self.x_edit.setText(str(self.default_num))

        y_label = QLabel(self)
        y_label.setText("y：")
        y_label.move(10, 55)
        self.y_edit.move(70, 50)
        self.y_edit.setText(str(self.default_num))

        width_label = QLabel(self)
        width_label.setText("width：")
        width_label.move(10, 95)
        self.width_edit.move(70, 90)
        self.width_edit.setText(str(self.default_num))

        height_label = QLabel(self)
        height_label.setText("height：")
        height_label.move(10, 135)
        self.height_edit.move(70, 130)
        self.height_edit.setText(str(self.default_num))

        total_label = QLabel(self)
        total_label.setText("total：")
        total_label.move(10, 175)
        self.total_edit.move(70, 170)

        shoot = QPushButton('截图', self)
        shoot.setCheckable(True)
        shoot.move(10, 210)
        shoot.clicked[bool].connect(self.cut_rect)

    def cut_rect(self, b):
        self.x = int(self.x_edit.text())
        self.y = int(self.y_edit.text())
        self.width = int(self.width_edit.text())
        self.height = int(self.height_edit.text())
        self.total_edit.setText(str(self.calculate_color(self.x, self.y, self.width, self.height)))
        self.update()

    # 相加区域所有颜色
    def calculate_color(self, start_x, start_y, width, height):
        color_all: int = 0
        for x in range(start_x, start_x + width):
            for y in range(start_y, start_y + height):
                color_all = color_all + self.img.pixel(x, y)
        return color_all

    def paintEvent(self, e: QPaintEvent):
        qp = QPainter(self)
        # 反锯齿
        qp.setRenderHint(QPainter.Antialiasing)
        qp.begin(self)
        target = QRect(10, 250, self.width, self.height)
        source = QRect(self.x, self.y, self.width, self.height)
        # 将源图像文件中(0.0, 0.0, 70.0, 40.0)位置的图像画到目标绘图设备中的(10.0, 20.0, 80.0, 60.0)位置上，大小自适应
        qp.drawImage(target, self.img, source)
        qp.end()
