# from ppadb.client import Client as AdbClient
# import utils.PhoneUtils
import utils.CommonUtils

utils.CommonUtils.project_initial()

# Default is "127.0.0.1" and 5037
# client = AdbClient(host="127.0.0.1", port=5037)
# print(client.version())
# device = client.devices()[0]
# utils.PhoneUtils.take_snapshot(device)
logger = utils.CommonUtils.common_logger()
# logger = utils.CommonUtils.logger()

logger.debug("11111")
logger.info("11111")
logger.warning("11111")
logger.error("11111")
logger.critical("11111")