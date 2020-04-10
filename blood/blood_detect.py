class BloodDetect:

    def __init__(self):
        print("初始化血量监测")
        self.blood_point1 = BloodPoint(1, 1)
        self.blood_point2 = BloodPoint(1, 2)
        self.blood_point3 = BloodPoint(1, 3)
        self.curr_blood = 100

    def detect(self, img):
        qc = img.pixelColor(self.blood_point1.x, self.blood_point1.y)
        print(qc.name())
        return self.curr_blood


class BloodPoint:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
