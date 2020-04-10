class Map:
    def __init__(self):
        self.map_white = 0
        self.map_index = {
            '神木村': 218,
            '神木村东边森林': 513
        }

    # 地图名字特征 通过白色判断
    def detect(self, img):
        # img = self.screen.grabWindow(self.hwnd, 45, 56, 250, 15).toImage()
        self.map_white = 0
        for start in range(45, 295):
            for end in range(56, 71):
                qc = img.pixelColor(start, end)
                if qc.name() == '#ffffff':
                    self.map_white += 1
        for key, value in self.map_index.items():
            if value == self.map_white:
                print("当前在:{}", key)
                break
