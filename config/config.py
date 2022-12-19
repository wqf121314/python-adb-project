import sys

module_name = 'Python-Adb-Appium'


class Path:
    if sys.platform == 'darwin':
        BASE_PATH = '/Users/didi/code store/git/' + module_name
    elif sys.platform == 'dev':
        BASE_PATH = sys.path[1] + '/log/'
    else:
        BASE_PATH = sys.path[1]

    LOG_PATH = BASE_PATH + '/log/'
