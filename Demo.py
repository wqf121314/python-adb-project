from ppadb.client import Client as AdbClient
import utils.PhoneUtils

# Default is "127.0.0.1" and 5037
client = AdbClient(host="127.0.0.1", port=5037)
print(client.version())
# device = client.devices()[0]
# utils.PhoneUtils.getScreencap(device)