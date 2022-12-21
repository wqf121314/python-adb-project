from ppadb.client import Client as AdbClient
import time, os
from config import config
from utils import Logger


class ADBUtils:
    def __init__(self, device):
        self.device = device

    def lock_screen(self):
        self.device.shell("input keyevent 26")

    def unlock_simple(self):
        self.take_snapshot()
        self.device.shell("input keyevent 26")
        time.sleep(1)
        self.take_snapshot()
        self.device.shell("input swipe 540 1300 540 500 100")

        self.take_snapshot()

    def take_snapshot(self):
        time.sleep(1)
        """
        Create a snapshot and keep a copy on the device
        :param device:
        :return:
        """
        time_now = time.strftime("%Y%m%d%H%M%S", time.localtime())
        filename = "screen_" + time_now + ".png"

        img_path = config.Path.LOG_PATH + time.strftime("%Y-%m-%d", time.localtime()) + '/img/'
        if not os.path.exists(img_path):
            os.makedirs(img_path)

        Logger.info(f'{device.serial} crate a snapshot: {filename}')
        device.shell("screencap -p /sdcard/" + filename)
        device.pull("/sdcard/" + filename, img_path + filename)
        Logger.info(f'updating snapshot path:{img_path}{filename}')

    def take_screenshot(self):
        time.sleep(1)
        """
        Create a snapshot and NOT keep a copy on the device
        :param device:
        :return:
        """
        img_path = config.Path.LOG_PATH + time.strftime("%Y-%m-%d", time.localtime()) + '/img/'
        if not os.path.exists(img_path):
            os.makedirs(img_path)
        time_now = time.strftime("%Y%m%d%H%M%S", time.localtime())
        filename = "screen_" + time_now + ".png"

        img_path = img_path + filename
        result = device.screencap()
        with open(img_path, "wb") as fp:
            fp.write(result)
        Logger.info(f'{device.serial} crate a snapshot: {img_path}')


if __name__ == '__main__':
    device = AdbClient().devices()[0]
    adb = ADBUtils(device)
    # adb.lock_screen()
    adb.unlock_simple()
