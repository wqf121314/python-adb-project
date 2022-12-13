import time


def project_log_path():
    time_now = time.strftime("%Y-%m-%d", time.localtime())
    return "logs/" + time_now
