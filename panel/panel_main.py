from PyQt5.QtWidgets import QWidget, QCheckBox, QGridLayout, QLabel


class PanelMain(QWidget):
    def __init__(self):
        super().__init__()
        self.grid = QGridLayout()
        self.map_label = QLabel(self)
        self.cb1 = QCheckBox('复选框1')
        self.cb2 = QCheckBox('复选框2')

        self.init_ui()

    def init_ui(self):
        self.grid.setSpacing(10)

        self.grid.addWidget(self.map_label)

        self.cb1.stateChanged.connect(self.change_check_box)
        self.grid.addWidget(self.cb1)
        self.cb1.setDisabled(True)

        self.cb2.stateChanged.connect(self.change_check_box)
        self.grid.addWidget(self.cb2)

        self.setLayout(self.grid)

    def set_map_name(self, map_name):
        self.map_label.setText(map_name)

    def change_check_box(self):
        print("点了checkbox")
