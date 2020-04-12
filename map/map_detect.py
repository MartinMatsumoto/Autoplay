class MapDetect:
    def __init__(self):
        self.map_white: int = 0
        self.map_code: int = 0
        self.map_name: str = ''
        self.map_index = {
            '神木村': 218,
            '神木村东边森林': 513,
            '射手村:100000000': 208,
            '射手村北部小山:100010000': 471,
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
        # print(self.map_white)
        if self.map_white == 0:
            self.map_name = ''
            self.map_code = 0
            return self.map_code, self.map_name
        for key, value in self.map_index.items():
            if value == self.map_white:
                self.map_name = key.split(":")[0]
                self.map_code = int(key.split(":")[1])
                break
        return self.map_code, self.map_name
