import os, time, logging, logging.handlers, sys


def project_log_path():
    time_now = time.strftime("%Y-%m-%d", time.localtime())
    path = "logs/" + time_now
    return path


def project_initial():
    logs_path = project_log_path()
    if not os.path.exists(logs_path):
        os.makedirs(logs_path)
        common_logger().info("Initialize the project")
        common_logger().info("crating logs path:" + logs_path)


def common_logger():
    logfile = project_log_path() + "/all.log"
    handler = logging.handlers.RotatingFileHandler(logfile, maxBytes=1024 * 1024, backupCount=5, encoding="utf-8",
                                                   mode="dev")  # 实例化handler
    fmt = '%(asctime)s - %(filename)s:%(lineno)s - %(levelno)s %(levelname)s %(pathname)s %(module)s %(funcName)s %(created)f %(thread)d %(threadName)s %(process)d %(name)s - %(message)s'  # 定义日志格式
    formatter = logging.Formatter(fmt)  # 实例化formatter。

    logger = logging.getLogger('all')  # 获取名为tst的logger。

    handler.setFormatter(formatter)  # 为handler添加formatter。
    logger.addHandler(handler)  # 为logger添加handler。

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    stream_handler.setLevel(logging.INFO)
    logger.addHandler(stream_handler)  # 为logger添加handler。


    logger.setLevel(logging.DEBUG)
    return logger