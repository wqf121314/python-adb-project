import os

import utils.AdbUtils
from utils import Logger
from ppadb.client import Client as AdbClient


class Demo:
    def __init__(self):
        pass

    def testLogger(self):
        # logger = utils.CommonUtils.common_logger()
        Logger.debug("11111")
        Logger.info("11111")
        Logger.warning("11111")
        Logger.error("11111")
        Logger.critical("11111")

    def test_snapshot(self):
        # os.system('adb devices')
        # Default is "127.0.0.1" and 5037
        client = AdbClient(host="127.0.0.1", port=5037)
        # print(client.version())
        device = client.devices()[0]
        utils.AdbUtils.take_snapshot(device)
        client.remote_disconnect()


# test_adb()
if __name__ == '__main__':
    d = Demo()
    # d.testLogger()
    d.test_snapshot()
