from ppadb.client import Client as AdbClient
import utils.PhoneUtils

# Default is "127.0.0.1" and 5037
# client = AdbClient(host="127.0.0.1", port=5037)
# print(client.version())
# device = client.devices()[0]
# utils.PhoneUtils.getScreencap(device)
import time
print(time.strftime("%Y%m%d%H%M%S", time.localtime()),round(time.time()*1000))

from datetime import datetime
date= datetime.utcnow() - datetime(1970, 1, 1)
seconds =(date.total_seconds())
milliseconds = round(seconds*1000)

print("Milliseconds since epoch:",milliseconds)

print("Current date:",datetime.utcnow())
