class MiniMapRect:
    left: int
    top: int
    right: int
    bottom: int

    def __init__(self, left, top):
        self.left = left
        self.top = top


class MiniMap:
    def __init__(self):
        # 从上往下数多少个开始遍历
        self.offset: int = 60
        self.offset_right: int = 90

        self.left: int = 9
        self.top: int = 84
        self.right: int = self.left + self.offset
        self.bottom: int = self.top + self.offset

        # 多少个连成颜色
        self.range = 10

        self.white: str = '#ffffff'
        self.gray: str = '#dddddd'

    def detect(self, img):
        all_white = False
        max_width: int = img.width()
        max_height: int = img.height()
        mini_map_rect: MiniMapRect = MiniMapRect(self.left, self.top)

        # 找下边框
        while all_white is False:
            self.bottom += 1
            white = True
            # y(self.bottom)为从纵60开始的变动值 x在横60-70像素之间
            for x in range(self.offset, self.offset + self.range):
                # 第一个点为白色才往下走
                if img.pixelColor(x, self.bottom).name() != self.white:
                    white = False
                    break
            # 通过了10个点均为白色 即可算出底部坐标
            if white:
                all_white = True
            # 找到截图的底部了 还是没找到边缘
            if max_height <= self.bottom:
                break
        if all_white is False:
            print("没找到minimap底部")

        arr = []
        # 找右边框
        all_gray = False
        i = 0
        while all_gray is False:
            self.right += 1
            i += 1
            gray = True
            # x 为从横60开始 y在60-70像素之间
            for y in range(self.offset_right, self.offset_right + self.range):
                arr.append(img.pixelColor(self.right, y).name())
                if img.pixelColor(self.right, y).name() != self.gray:
                    gray = False
                    break
            if gray:
                all_gray = True
            arr = []
            if max_width <= self.right:
                break
        if all_gray is False:
            print("没找到minimap右边")

        mini_map_rect.bottom = self.bottom
        mini_map_rect.right = self.right

        self.bottom: int = self.top + self.offset
        self.right: int = self.left + self.offset
        return mini_map_rect
