class BloodDetect:
    blood_point_y = 727
    blue_point_y = 743

    point_x_1 = 648
    point_x_2 = 680
    point_x_3 = 712
    point_x_4 = 744
    point_x_5 = 776

    blood_1 = '#fa4ba4'
    blood_2 = '#fb51a8'
    blood_3 = '#fb5bad'
    blood_4 = '#fb69b7'
    blood_5 = '#fc79c2'

    blue_1 = '#15e4f4'
    blue_2 = '#2de7f5'
    blue_3 = '#b1f5ff'
    blue_4 = '#56ebf8'
    blue_5 = '#27e6f5'

    def __init__(self):
        print("初始化血量监测")
        self.curr_blood = 5
        self.curr_blue = 5

    def detect(self, img):
        if img.pixelColor(self.point_x_5, self.blood_point_y).name() == self.blood_5:
            self.curr_blood = 5
        elif img.pixelColor(self.point_x_4, self.blood_point_y).name() == self.blood_4:
            self.curr_blood = 4
        elif img.pixelColor(self.point_x_3, self.blood_point_y).name() == self.blood_3:
            self.curr_blood = 3
        elif img.pixelColor(self.point_x_2, self.blood_point_y).name() == self.blood_2:
            self.curr_blood = 2
        elif img.pixelColor(self.point_x_1, self.blood_point_y).name() == self.blood_1:
            self.curr_blood = 1
        else:
            self.curr_blood = 0

        if img.pixelColor(self.point_x_5, self.blue_point_y).name() == self.blue_5:
            self.curr_blue = 5
        elif img.pixelColor(self.point_x_4, self.blue_point_y).name() == self.blue_4:
            self.curr_blue = 4
        elif img.pixelColor(self.point_x_3, self.blue_point_y).name() == self.blue_3:
            self.curr_blue = 3
        elif img.pixelColor(self.point_x_2, self.blue_point_y).name() == self.blue_2:
            self.curr_blue = 2
        elif img.pixelColor(self.point_x_1, self.blue_point_y).name() == self.blue_1:
            self.curr_blue = 1
        else:
            self.curr_blue = 0

        return self.curr_blood, self.curr_blue
