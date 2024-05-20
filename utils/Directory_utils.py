import os
import shutil
import time
import traceback
from utils import logger_utils
from properties.properties import download_path


def create_dirs(directories):
    path = os.path.join(download_path, directories)
    os.makedirs(path, exist_ok=True)
    return path


def get_path():
    path = os.getcwd()
    return path


def get_parent_path():
    path = os.getcwd()
    path = os.path.abspath(os.path.join(path, os.pardir))
    return path


def create_or_update_rethrow_file(workitem_id):
    filename = 'workitems_rethrows.txt'
    path = get_path() + "\\rethrows\\"
    if os.path.exists(path + filename):
        append_write = 'a+'  # append if already exists
    else:
        append_write = 'w+'  # make a new file if not

    rethrow_file = open(path + filename, append_write)
    rethrow_file.write(str(workitem_id) + ';')
    rethrow_file.close()


def read_rethrow_file():
    filename = 'workitems_rethrows.txt'
    path = get_path() + "\\rethrows\\"
    try:
        f = open(path + filename, "r")
        contents = f.read()
        workitem_list = contents.split(';')
        f.close()
        return workitem_list
    except Exception:
        return


def rotate_logs():
    source_path = get_path() + "\\logs\\"
    rtc_attachment_downloader_log = source_path + 'rtc_attachment_downloader.log'
    destination_path = source_path + "\\rotate_logs\\"
    timestr = time.strftime("%Y%m%d-%H%M%S")
    file = 'rtc_attachment_downloader_{}.log'.format(timestr)
    try:
        shutil.move(rtc_attachment_downloader_log, destination_path + file)
    except PermissionError:
        logger_utils.set_logger_critical(traceback.format_exc())
    except Exception:
        print("An exception occurred")
        logger_utils.set_logger_critical(traceback.format_exc())