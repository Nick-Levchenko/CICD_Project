import logging
import os.path
import sys
from logging.handlers import RotatingFileHandler
from typing import Union

from logger.logger_config import LoggerConfig


class Logger:
    if not os.path.isdir(LoggerConfig.LOGS_DIRECTORY):
        os.makedirs(LoggerConfig.LOGS_DIRECTORY)
    __logger = logging.getLogger(LoggerConfig.LOGGER_NAME)
    __logger.setLevel(LoggerConfig.LOGS_LEVEL)
    __handler1 = RotatingFileHandler(LoggerConfig.LOGS_FILENAME, maxBytes=LoggerConfig.MAX_BYTES,
                                     backupCount=LoggerConfig.BACKUP_COUNT)
    __handler2 = logging.StreamHandler(sys.stdout)
    __formatter = logging.Formatter(LoggerConfig.FORMAT)
    __handler1.setFormatter(__formatter)
    __handler2.setFormatter(__formatter)
    __logger.addHandler(__handler1)
    __logger.addHandler(__handler2)

    @staticmethod
    def set_level(level: Union[int, str]) -> None:
        Logger.__logger.setLevel(level)

    @staticmethod
    def info(message: str) -> None:
        Logger.__logger.info(message)

    @staticmethod
    def debug(message: str) -> None:
        Logger.__logger.debug(message)

    @staticmethod
    def warning(message: str) -> None:
        Logger.__logger.warning(message)

    @staticmethod
    def error(message: str) -> None:
        Logger.__logger.error(message)

    @staticmethod
    def fatal(message: str) -> None:
        Logger.__logger.fatal(message)
