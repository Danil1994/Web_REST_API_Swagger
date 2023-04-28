from datetime import datetime
from typing import Any, List

from task_6 import Driver, create_list_object, sorting_order_by

from config import PATH_FILE


def create_report() -> List[Driver]:
    return create_list_object(PATH_FILE)


def get_order(response_order: str) -> bool:
    return response_order.lower() == 'desc'


def normalize_string(data: str) -> str:
    return data.upper().strip()


def info_driver_about(order_list: List, driver_abbr: str) -> Driver | None:
    driver_info = None
    driver_abbr = normalize_string(driver_abbr)
    for driver in order_list:
        if driver.abbr == driver_abbr:
            driver_info = driver

    return driver_info


def made_report(data: [Driver], report: bool) -> list[dict[str, Any]]:
    drivers_list = []
    sorting_order = sorting_order_by(data, report)
    for driver in sorting_order:
        driver_info = {"abbr": driver.abbr, "driver_name": driver.name, "lap_time": driver.lap_time,
                       "start_time": driver.start_time, "end_time": driver.end_time}

        drivers_list.append(driver_info)
    return drivers_list


def made_short_report(data: [Driver], report: bool) -> list[dict[str, Any]]:
    short_drivers_list = []
    sorting_order = sorting_order_by(data, report)
    for driver in sorting_order:
        driver_info = {"abbr": driver.abbr, "driver_name": driver.name, "lap_time": driver.lap_time}

        short_drivers_list.append(driver_info)
    return short_drivers_list


def made_driver_info(driver: Driver) -> dict[str, datetime | None | str]:
    info = {"driver_name": driver.name, "abbr": driver.abbr,
            "lap_time": driver.lap_time,
            "start_time": driver.start_time,
            "end_time": driver.end_time}

    return info
