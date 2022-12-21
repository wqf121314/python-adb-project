from ppadb.client import Client as AdbClient
from utils import Logger


class OPPO:
    def __init__(self, device):
        self.device = device

    def get_info(self):
        project_name = self.device.shell("getprop ro.separate.soft").strip('\n')
        global_name = self.device.shell("settings get global device_name").strip('\n')
        device_name = self.device.shell("settings get secure oppo_device_name").strip('\n')

        model_name = self.device.shell("getprop ro.product.name").strip('\n')
        colorOS_version = self.device.shell("getprop ro.build.version.opporom").strip('\n')
        releaseVer = self.device.shell("getprop ro.build.version.release").strip('\n')
        OTA_version = self.device.shell("getprop ro.build.version.ota").strip('\n')
        Selected_region = self.device.shell("getprop persist.sys.oplus.region").strip('\n')

        self.info = {"ProjectName": project_name, "GlobalName": global_name, "device_name": device_name,
                     "ModelName": model_name, "ColorOSVersion": colorOS_version, "ReleaseVer": releaseVer,
                     "OTA_version": OTA_version, "SelectedRegion": Selected_region}
        return self.info


if __name__ == '__main__':
    device = AdbClient().devices()[0]
    info = OPPO(device).get_info()
    Logger.info(info)
