class MiniMap:
    def __init__(self):
        # 从上往下数多少个开始遍历
        self.offset: int = 60

        self.left: int = 9
        self.top: int = 84
        self.right: int = self.left + self.offset
        self.bottom: int = self.top + self.offset

        # 多少个连成白色
        self.range = 10

        self.white: str = '#ffffff'
        self.gray: str = '#dddddd'

    def detect(self, img):
        all_white = False
        while all_white is False:
            self.bottom += 1
            white = True
            for x in range(self.offset, self.offset + self.range):
                if img.pixelColor(x, self.bottom).name() != self.white:
                    white = False
                    break
            if white:
                all_white = True

        color = []
        all_gray = False
        self.right += 300
        while all_gray is False:
            self.right += 1
            gray = True
            for x in range(self.offset, self.offset + self.range):
                color.append(img.pixelColor(x, self.right).name())
                # if img.pixelColor(x, self.right).name() != self.gray:
                #     gray = False
                #     break
            # if gray:
            #     all_gray = True
            print(self.right, color)
            color = []

        print("bottom=" + str(self.bottom))
        print("right=" + str(self.right))
        self.bottom: int = self.top + self.offset
        self.right: int = self.left + self.offset
