import os,datetime

def mkdir():
    filepath="logs\\"+datetime.date.today()
    os.mkdir(filepath)

def getScreencap(device,filename):
    result = device.screencap()
    with open("/imgs/screen.png", "wb") as fp:
        fp.write(result)