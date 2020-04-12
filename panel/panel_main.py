from PyQt5.QtWidgets import QWidget, QCheckBox, QGridLayout, QLabel


class PanelMain(QWidget):
    def __init__(self):
        super().__init__()
        self.grid = QGridLayout()
        self.map_label = QLabel(self)
        self.blood_label = QLabel(self)
        self.blue_label = QLabel(self)
        self.cb1 = QCheckBox('复选框1')
        self.cb2 = QCheckBox('复选框2')

        self.init_ui()

    def init_ui(self):
        self.grid.setSpacing(5)

        map_container = QLabel(self)
        map_container.setText("当前地图：")
        map_container.setBuddy(self.map_label)
        self.grid.addWidget(map_container, 0, 0)
        self.grid.addWidget(self.map_label, 0, 1, 1, 2)

        blood_container = QLabel(self)
        blood_container.setText("当前血量：")
        blood_container.setBuddy(self.blood_label)
        self.grid.addWidget(blood_container, 1, 0)
        self.grid.addWidget(self.blood_label, 1, 1, 1, 2)

        blue_container = QLabel(self)
        blue_container.setText("当前蓝量：")
        blue_container.setBuddy(self.blue_label)
        self.grid.addWidget(blue_container, 2, 0)
        self.grid.addWidget(self.blue_label, 2, 1, 1, 2)

        self.cb1.stateChanged.connect(self.change_check_box)
        self.grid.addWidget(self.cb1, 3, 0)
        self.cb1.setDisabled(True)

        self.cb2.stateChanged.connect(self.change_check_box)
        self.grid.addWidget(self.cb2, 4, 0)

        self.setLayout(self.grid)

    def set_map_name(self, map_name):
        self.map_label.setText(map_name)

    def set_blood(self, blood, blue):
        self.blood_label.setText(str(blood))
        self.blue_label.setText(str(blue))

    def change_check_box(self):
        print("点了checkbox")
