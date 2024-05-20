import traceback
from utils import logger_utils
from utils.rtc_utils import get_attachments_multiples_project_areas, get_attachments_single_project_area, start_rtc_client, download_attachments
from utils.Directory_utils import read_rethrow_file
from properties.properties import rtc_areas


def start_attachment_download():
    rtc_client = start_rtc_client()
    if rtc_areas == "":
        try:
            get_attachments_multiples_project_areas(rtc_client, True)
        except Exception:
            print("An exception occurred")
            logger_utils.set_logger_critical(traceback.format_exc())
    elif rtc_areas.__contains__(','):
        try:
            get_attachments_multiples_project_areas(rtc_client, False)
        except Exception:
            print("An exception occurred")
            logger_utils.set_logger_critical(traceback.format_exc())
    else:
        try:
            get_attachments_single_project_area(rtc_client, rtc_areas)
        except Exception:
            print("An exception occurred")
            logger_utils.set_logger_critical(traceback.format_exc())


def start_download_rethrow_file():
    rtc_client = start_rtc_client()
    workitems_array = read_rethrow_file()
    try:
        download_attachments(workitems_array, rtc_client)
    except Exception:
        print("An exception occurred")
        logger_utils.set_logger_critical(traceback.format_exc())