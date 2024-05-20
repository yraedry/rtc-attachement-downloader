import logging
from logging.handlers import RotatingFileHandler
from utils.Directory_utils import get_path


def set_logger_debug(body_log):
    path = get_path()
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    if not logger.handlers:
        fh = logging.FileHandler(path + '/logs/rtc_attachment_downloader.log')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        fh.close()
    logger.debug(body_log)


def set_logger_info(body_log):
    path = get_path()
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    if not logger.handlers:
        fh = logging.FileHandler(path + '/logs/rtc_attachment_downloader.log')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        fh.close()
    logger.info(body_log)


def set_logger_warning(body_log):
    path = get_path()
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.WARNING)
    if not logger.handlers:
        fh = logging.FileHandler(path + '/logs/rtc_attachment_downloader.log')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        fh.close()
    logger.warning(body_log)


def set_logger_error(body_log):
    path = get_path()
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.ERROR)
    if not logger.handlers:
        fh = logging.FileHandler(path + '/logs/rtc_attachment_downloader.log')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        fh.close()
    logger.error(body_log)


def set_logger_critical(body_log):
    path = get_path()
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.CRITICAL)
    if not logger.handlers:
        fh = logging.FileHandler(path + '/logs/rtc_attachment_downloader.log')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        fh.close()
    logger.critical(body_log)
