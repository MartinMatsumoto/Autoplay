from tools.color_utils import ColorUtils


# 方形大小
class Rect:
    width: int
    height: int
    # 特征 所有点加起来的值
    feature: int

    # 特征点1 坐标0，0的颜色
    feature_1: int

    # 特征点2 坐标中心点的颜色
    offset_x2: int
    offset_y2: int
    feature_2: int

    # 特征点3 坐标最右下角点的颜色
    # 3个特征点都符合的情况下再计算总值
    feature_3: int

    def __init__(self, width, height, feature):
        self.width = width
        self.height = height
        self.feature = feature


# 方形范围
class RectRange:
    start_x: int
    start_y: int
    end_x: int
    end_y: int

    def __init__(self, start_x, start_y, end_x, end_y):
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y


class RectDetect:
    def __init__(self):
        return

    def detect(self, img, rect: Rect, detect_range: RectRange):
        start_x: int
        start_y: int
        end_x: int
        end_y: int
        if detect_range is not None:
            start_x = detect_range.start_x
            start_y = detect_range.start_y
            end_x = detect_range.end_x
            end_y = detect_range.end_y
        else:
            start_x = 0
            start_y = 0
            end_x = img.width()
            end_y = img.height()
        for y in range(start_y, end_y):
            for x in range(start_x, end_x):
                if img.pixel(x, y) == rect.feature_1 \
                        and img.pixel(x + rect.offset_x2, y + rect.offset_y2) == rect.feature_2 \
                        and img.pixel(x + rect.width, y + rect.height) == rect.feature_3 \
                        and self.calculate_color(img, x, y, rect) == rect.feature:
                    return x, y
        print("找完了")

    # 相加区域所有颜色
    def calculate_color(self, img, start_x, start_y, rect: Rect):
        color_all: int = 0
        for x in range(start_x, start_x + rect.width):
            for y in range(start_y, start_y + rect.height):
                color_all = color_all + img.pixel(x, y)
        return color_all
