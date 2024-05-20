from utils import logger_utils
import datetime
import traceback


def query_workitems_list(rtc_client, area, query_type, query_year):
    returned_properties = "dc:identifier,dc:created,rtc_cm:projectArea,dc:title,dc:type,rtc_cm:config_item,rtc_cm:configuration_item"
    first_day_of_year = datetime.datetime.now().date().replace(year=int(query_year), month=1, day=1).strftime(
        "%Y-%m-%dT%H:%M:%SZ")
    last_day_of_year = datetime.datetime.now().date().replace(year=int(query_year), month=12, day=31).strftime(
        "%Y-%m-%dT%H:%M:%SZ")
    query_str = 'dc:type="{}"  and dc:created >= "{}" and  dc:created <= "{}"'.format(query_type,
                                                                                      first_day_of_year,
                                                                                      last_day_of_year)
    logger_utils.set_logger_info("query => " + query_str)
    print("query => " + query_str)
    try:
        workitems = rtc_client.queryWorkitems(query_str,
                                              projectarea_id=area.id,
                                              projectarea_name=area.title,
                                              returned_properties=returned_properties)
        if workitems is None:
            logger_utils.set_logger_info("no workitems on this query")
    except Exception:
        print("An exception occurred")
        logger_utils.set_logger_critical(traceback.format_exc())
    return workitems
