from ppadb.client import Client as AdbClient
import time, os, io
from config import config
from utils import Logger
from utils import SwipeDirection


class ADBUtils:
    def __init__(self, device):
        self.device = device

    def lock_screen(self):
        self.take_snapshot()
        self.device.shell("input keyevent 26")
        self.take_snapshot()

    def unlock_simple(self):
        if self.is_screen_lock():
            self.take_snapshot()
            self.device.shell("input keyevent 26")
            time.sleep(0.2)
            self.take_snapshot()
            self.device.shell("input swipe 540 1300 540 500 100")
            self.take_snapshot()

    def swipe(self, direction):
        match (direction):
            case 'UP':
                self.device.shell("input swipe 540 1300 540 500 100")
            case 'up':
                self.device.shell("input swipe 540 1300 540 500 100")
            case _:
                print('NONE')

    def is_screen_lock(self):
        '''
        1、亮屏且有锁 showing=true和 screenState=SCREEN_STATE_ON
        2、灭屏且有锁 showing=true和 screenState=SCREEN_STATE_OFF
        3、亮屏且无锁 showing=false和screenState=SCREEN_STATE_ON
        :return:
        '''
        result = self.device.shell("dumpsys window policy")
        # Logger.debug(f'dumpsys window policy:{result}')
        lines = result.splitlines()
        for i in range(len(lines)):
            if "showing=false" in lines[i]:
                return False
        return True

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
    adb.unlock_simple()

    # print(SwipeDirection.Enum.)
    # adb.swipe("UP")
    # time.sleep(5)
    #
    # adb.lock_screen()
