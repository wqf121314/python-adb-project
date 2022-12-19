import time
import sys
import os
import logging
from logging import handlers
from config import config


class __LoggingFactory:
    def __init__(self, name, log_filename='debug.log', *, loglevel=logging.DEBUG, stdout=False, back_count=4):
        self.name = name
        formatter = logging.Formatter('%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s')
        _logger = logging.getLogger(self.name)
        _logger.setLevel(level=loglevel)

        today = time.strftime("%Y-%m-%d", time.localtime())
        logs_path = config.Path.LOG_PATH + today
        if not os.path.exists(logs_path):
            os.makedirs(logs_path)

        file_logger = handlers.TimedRotatingFileHandler(filename=f'{config.Path.LOG_PATH}/{today}/{log_filename}',
                                                        backupCount=back_count,
                                                        encoding='utf-8')

        file_logger.suffix = "%Y%m%d%H"

        stdout_logger = stdout and logging.StreamHandler(sys.stdout)

        stdout_logger and stdout_logger.setLevel(loglevel)
        stdout_logger and stdout_logger.setFormatter(formatter)
        stdout_logger and _logger.addHandler(stdout_logger)

        file_logger and file_logger.setLevel(loglevel)
        file_logger and file_logger.setFormatter(formatter)
        file_logger and _logger.addHandler(file_logger)

    @property
    def logger(self):
        return logging.getLogger(self.name)


__debug_logger = __LoggingFactory('debug', log_filename='debug.log', stdout=True).logger
__info_logger = __LoggingFactory('info', log_filename='info.log', stdout=True).logger
__wf_logger = __LoggingFactory('wf', log_filename='wf.log', stdout=True).logger


def debug(info):
    __debug_logger.debug(info, stacklevel=2)


def info(info):
    __info_logger.info(info, stacklevel=2)


def warning(info):
    __wf_logger.warning(info, stacklevel=2)


def error(info):
    __wf_logger.error(info, stacklevel=2)


def critical(info):
    __wf_logger.critical(info, stacklevel=2)


if __name__ == '__main__':
    for i in range(4):
        debug('debug')
        info('info')
        warning('warning')
        error('error')
        critical('critical')
        time.sleep(1)
