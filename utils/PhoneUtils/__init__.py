import os, time
import utils.CommonUtils

PATH = utils.CommonUtils.project_log_path()+"/imgs"
LOGGER=utils.CommonUtils.common_logger()

def create_logfile():
    if not os.path.exists(PATH):
        LOGGER.info('创建目录'+PATH)
        os.makedirs(PATH)

def take_snapshot(device):
    create_logfile()
    time_now = time.strftime("%Y%m%d%H%M%S", time.localtime())
    filename = "screen_" + time_now + ".png"
    device.shell("screencap -p /sdcard/" + filename)
    device.pull("/sdcard/" + filename, PATH + "/" + filename)

    # print("屏幕截取中...请稍候!")
    # os.system("adb shell screencap -p /sdcard/a.png")
    # os.system("adb pull /sdcard/a.png .")
    # print("截图完毕！")
