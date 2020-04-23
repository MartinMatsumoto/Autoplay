from PyQt5.QtGui import QColor


class ColorUtils:

    @staticmethod
    def get_hex_color(color: QColor):
        return int(color.name().replace("#", ""), 16)
