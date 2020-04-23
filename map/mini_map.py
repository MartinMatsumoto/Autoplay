class MiniMap:
    def __init__(self):
        # 从上往下数多少个开始遍历
        self.offset: int = 60

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

        # 找右边框
        all_gray = False
        while all_gray is False:
            self.right += 1
            gray = True
            # x 为从横60开始 y在60-70像素之间
            for y in range(self.offset, self.offset + self.range):
                if img.pixelColor(self.right, y).name() != self.gray:
                    gray = False
                    break
            if gray:
                all_gray = True
            if max_width <= self.right:
                break
        if all_gray is False:
            print("没找到minimap右边")

        print("bottom=" + str(self.bottom))
        print("right=" + str(self.right))
        self.bottom: int = self.top + self.offset
        self.right: int = self.left + self.offset
