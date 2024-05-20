import requests
from clint.textui import progress
from utils.Directory_utils import create_dirs, create_or_update_rethrow_file
from querys.querys import query_workitems_list
from rtcclient.utils import setup_basic_logging
from rtcclient import RTCClient
import logging
import traceback
from utils import logger_utils
from utils.Directory_utils import get_path
from properties.properties import rtc_url, rtc_username, rtc_password, rtc_areas, query_type, query_year, query_configItem


def start_rtc_client():
    # you can remove this if you don't need logger
    # default debug logger for console output
    path = get_path()
    # logging.basicConfig(level=logging.DEBUG, filename=path + '/logs/rtc_client.log')
    # logging.debug(setup_basic_logging())
    try:
        rtc_client = RTCClient(rtc_url, rtc_username, rtc_password, proxies=None, searchpath=None, ends_with_jazz=True)
    except Exception:
        print("An exception occurred")
        logger_utils.set_logger_critical(traceback.format_exc())
    return rtc_client


def download_attachments(workitems_list, rtc_client):
    for workitem in workitems_list:
        if type(workitem) == str:
            workitem_id = workitem
        else:
            workitem_id = workitem.identifier
        try:
            print("WorkItem ID => " + workitem_id + "-- Configuration Item => " + workitem.config_item)
        except AttributeError:
            print("WorkItem ID => " + workitem_id + "-- Configuration Item => " + workitem.configuration_item)
        logger_utils.set_logger_info("WorkItem ID => " + workitem_id)
        returned_properties = "dc:created,rtc_cm:projectArea,dc:title,dc:type,dc:identifier,rtc_cm:config_item,rtc_cm:configuration_item"
        wk = rtc_client.getWorkitem(workitem_id, returned_properties=returned_properties)
        attachment_exist = wk.getAttachments()
        if attachment_exist is None:
            print("There is no attachment for this workitem")
            logger_utils.set_logger_info("There is no attachment for this workitem")
        if attachment_exist is not None:
            for attachments in attachment_exist:
                workitem_title = remove_special_characters(wk.title)
                try:
                    path_created = create_dirs(
                        wk.projectArea + "\\" + wk.type + "\\" + wk.created.split('-')[0] + "\\" + workitem_id + " - " + workitem_title.rstrip()[:200])
                except Exception:
                    print('Add item to rethrow file =>' + str(workitem_id))
                    create_or_update_rethrow_file(workitem_id)
                    logger_utils.set_logger_warning("Add item to rethrow file => " + str(workitem_id))
                    logger_utils.set_logger_error(traceback.format_exc())
                attachment_name = attachments.title
                print("Attachment ID=> " + attachments.identifier)
                logger_utils.set_logger_info("Attachment => " + attachment_name)
                attachment_path = path_created + "\\" + attachments.identifier + " - " + attachment_name
                headers = {
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=.08',
                    'Origin': '{}'.format(attachments.url),
                    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.17 (KHTML, like Gecko)  Chrome/24.0.1312.57 Safari/537.17',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Referer': '{}'.format(attachments.content),
                    'Accept-Encoding': 'gzip,deflate,br',
                    'Accept-Language': 'en-US,en;q=0.5',
                }
                headers.update(rtc_client.headers)
                try:
                    attachment_download = requests.get(attachments.content, headers=headers, verify=False, stream=True)
                    if not attachment_download.status_code == 200:
                        print('Add item to rethrow file =>' + str(workitem_id))
                        create_or_update_rethrow_file(workitem_id)
                        logger_utils.set_logger_warning("Add item to rethrow file => " + str(workitem_id))
                        return
                    with open(attachment_path, "wb") as binary_content:
                        total_length = int(attachment_download.headers.get('content-length'))
                        for ch in progress.bar(attachment_download.iter_content(chunk_size=2391975),
                                               expected_size=(total_length / 1024) + 1):
                            if ch:
                                binary_content.write(ch)
                except Exception:
                    print('Add item to rethrow file =>' + str(workitem_id))
                    create_or_update_rethrow_file(workitem_id)
                    logger_utils.set_logger_warning("Add item to rethrow file => " + str(workitem_id))
                    logger_utils.set_logger_critical(traceback.format_exc())


def get_attachments_multiples_project_areas(rtc_client, all_areas):
    try:
        if all_areas:
            list_areas = rtc_client.getProjectAreas()
        else:
            list_areas = rtc_areas.split(',')
    except Exception:
        print("An exception occurred")
        logger_utils.set_logger_critical(traceback.format_exc())
    for area in list_areas:
        print("area => " + str(area))
        logger_utils.set_logger_info("area => " + str(area))
        if all_areas is False:
            area = rtc_client.getProjectArea(area)
        query_type_list = query_type.split(',')
        query_year_list = query_year.split(',')
        try:
            for rtc_type in query_type_list:
                for rtc_year in query_year_list:
                    workitems_list = query_workitems_list(rtc_client, area, rtc_type, rtc_year)
                    workitem_config_list = []
                    if workitems_list is not None:
                        for workitem_config_list_check in workitems_list:
                            if hasattr(workitem_config_list_check, 'config_item') or hasattr(workitem_config_list_check, 'configuration_item'):
                                if workitem_config_list_check.config_item == query_configItem:
                                    workitem_config_list.append(workitem_config_list_check)
                        download_attachments(workitem_config_list, rtc_client)
        except AttributeError:
            for workitem_config_list_check in workitems_list:
                if hasattr(workitem_config_list_check, 'configuration_item'):
                    if workitem_config_list_check.configuration_item == query_configItem:
                        workitem_config_list.append(workitem_config_list_check)
            download_attachments(workitem_config_list, rtc_client)
        except Exception:
            print("An exception occurred")
            logger_utils.set_logger_critical(traceback.format_exc())


def get_attachments_single_project_area(rtc_client, rtc_area):
    print("area => " + str(rtc_area))
    logger_utils.set_logger_info("area => " + str(rtc_area))
    area = rtc_client.getProjectArea(rtc_area)
    query_type_list = query_type.split(',')
    query_year_list = query_year.split(',')
    try:
        for rtc_type in query_type_list:
            for rtc_year in query_year_list:
                workitems_list = query_workitems_list(rtc_client, area, rtc_type, rtc_year)
                workitem_config_list = []
                if workitems_list is not None:
                    for workitem_config_list_check in workitems_list:
                        if hasattr(workitem_config_list_check, 'config_item') or hasattr(workitem_config_list_check, 'configuration_item'):
                            if workitem_config_list_check.config_item == query_configItem:
                                workitem_config_list.append(workitem_config_list_check)
                    download_attachments(workitem_config_list, rtc_client)
    except AttributeError:
        for workitem_config_list_check in workitems_list:
            if hasattr(workitem_config_list_check, 'configuration_item'):
                if workitem_config_list_check.configuration_item == query_configItem:
                    workitem_config_list.append(workitem_config_list_check)
        download_attachments(workitem_config_list, rtc_client)
    except Exception:
        print(traceback.format_exc())
        logger_utils.set_logger_critical(traceback.format_exc())


def remove_special_characters(special_string):
    remove_special_chars = special_string.translate({ord(c): " " for c in "!@#$%^&*()[]{};:,./<>?\|`~-=_+"})
    return remove_special_chars
