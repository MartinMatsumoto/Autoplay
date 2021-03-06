import time

from PyQt5.QtCore import QThread, pyqtSignal

from blood.blood_detect import BloodDetect
from map.coordinate_detect import CoordinateDetect
from map.map_detect import MapDetect
from map.xml_parser import XmlParser
from map.mini_map import MiniMap, MiniMapRect
from panel.panel_map import MapInfo
from window.window_shoot import WindowCapture


class UIThread(QThread):
    loop = True
    map_changing = False
    sleep_time: float = 0.5
    curr_map: MapInfo = MapInfo()
    curr_map_code = 0
    mini_map_rect: MiniMapRect

    reload_map = pyqtSignal(MapInfo)
    show_blood = pyqtSignal(int, int)

    def __init__(self, screen):
        super(UIThread, self).__init__()
        self.screen = screen
        self.blood_detect = BloodDetect()
        self.map_detect = MapDetect()
        self.coordinate_detect = CoordinateDetect()
        self.mini_map = MiniMap()
        self.xml_parser = XmlParser()

    def run(self):
        print("开始线程")
        window_capture = WindowCapture("MapleStory", self.screen)

        while self.loop:
            # 获取软件图片
            img = window_capture.window_capture()
            self.detect_map_change(img)
            if not self.map_changing:
                blood, blue = self.blood_detect.detect(img)
                self.blood_show(blood, blue)
                self.coordinate_detect.detect_character(img, self.mini_map_rect)
            time.sleep(self.sleep_time)
            # self.loop = False

    def detect_map_change(self, img):
        map_code, map_name = self.map_detect.detect(img)
        if map_code == 0:
            self.map_changing = True
            map_info = MapInfo()
            map_info.map_name = '地图切换中'
            self.reload_map.emit(map_info)
        else:
            self.map_changing = False
            if self.curr_map_code != map_code:
                curr_map = self.xml_parser.parse_file('resources/map/{map_code}.html'.format(map_code=map_code))
                curr_map.map_name = map_name
                curr_map.map_code = map_code
                # 发送添加信号
                self.reload_map.emit(curr_map)
                self.curr_map_code = map_code
                # 重新找到小地图边框
                self.mini_map_rect = self.mini_map.detect(img)

    def blood_show(self, blood, blue):
        self.show_blood.emit(blood, blue)
