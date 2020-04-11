# pip install opencv-python -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
# pip install PyQt5 -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
# pip install pypiwin32 -i http://pypi.douban.com/simple --trusted-host pypi.douban.com

from window.window_shoot import WindowCapture
from blood.blood_detect import BloodDetect
from map.map_detect import Map
from panel.panel import Panel
import os, time

sleep_time = 1
loop = True

window_capture = WindowCapture("钉钉")
blood_detect = BloodDetect()
panel = Panel()
map_detect = Map()

while loop:
    # 获取软件图片
    img = window_capture.window_capture()
    blood_detect.detect(img)
    # map_detect.detect(img)
    time.sleep(sleep_time)
    loop = False
