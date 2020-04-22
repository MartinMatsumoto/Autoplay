class BloodDetect:
    blood_point_y = 727
    blue_point_y = 743

    point_x_1 = 615
    point_x_2 = 649
    point_x_3 = 683
    point_x_4 = 717
    point_x_5 = 751

    gray_blood: int = 7960189

    def __init__(self):
        print("初始化血量监测")
        self.curr_blood = 0
        self.curr_blue = 0

    def get_pixel_value(self, img, x, y):
        return int(img.pixelColor(x, y).name().replace("#", ""), 16) != self.gray_blood

    def detect(self, img):
        # for x in range(610, 780):
        # print(img.pixelColor(x, self.blood_point_y).name().replace("#",""))
        # print(int(img.pixelColor(x, self.blood_point_y).name().replace("#", ""), 16))
        # for x in range(610, 780):
        # print(img.pixelColor(x, self.blue_point_y).name().replace("#", ""))
        # print(int(img.pixelColor(x, self.blue_point_y).name().replace("#", ""), 16))

        try:
            if self.get_pixel_value(img, self.point_x_5, self.blood_point_y):
                self.curr_blood = 5
            elif self.get_pixel_value(img, self.point_x_4, self.blood_point_y):
                self.curr_blood = 4
            elif self.get_pixel_value(img, self.point_x_3, self.blood_point_y):
                self.curr_blood = 3
            elif self.get_pixel_value(img, self.point_x_2, self.blood_point_y):
                self.curr_blood = 2
            elif self.get_pixel_value(img, self.point_x_1, self.blood_point_y):
                self.curr_blood = 1
            else:
                self.curr_blood = 0

            if self.get_pixel_value(img, self.point_x_5, self.blue_point_y):
                self.curr_blue = 5
            elif self.get_pixel_value(img, self.point_x_4, self.blue_point_y):
                self.curr_blue = 4
            elif self.get_pixel_value(img, self.point_x_3, self.blue_point_y):
                self.curr_blue = 3
            elif self.get_pixel_value(img, self.point_x_2, self.blue_point_y):
                self.curr_blue = 2
            elif self.get_pixel_value(img, self.point_x_1, self.blue_point_y):
                self.curr_blue = 1
            else:
                self.curr_blue = 0
        except Exception as e:
            print(e)

        return self.curr_blood, self.curr_blue
