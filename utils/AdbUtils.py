import time, os
from config import config
from utils import Logger
from ppadb.client import Client as AdbClient


def take_snapshot(device):
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


def take_screenshot(device):
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


def set_screen_on(device):
    device.shell("setting put system screen_off_timeout 2147483647")


if __name__ == '__main__':
    device = AdbClient().devices()[0]
    # take_screenshot(device)
    take_snapshot(device)
    # set_screen_on(device)
