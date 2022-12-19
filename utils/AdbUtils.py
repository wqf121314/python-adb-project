import time, os
from config import config


def take_snapshot(device):
    time_now = time.strftime("%Y%m%d%H%M%S", time.localtime())
    filename = "screen_" + time_now + ".png"
    device.shell("screencap -p /sdcard/" + filename)
    img_path = config.Path.LOG_PATH + time.strftime("%Y-%m-%d", time.localtime()) + '/img'
    if not os.path.exists(img_path):
        os.makedirs(img_path)
    device.pull("/sdcard/" + filename, img_path + "/" + filename)
