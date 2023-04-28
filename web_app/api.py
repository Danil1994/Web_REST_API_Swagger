import json
from datetime import datetime
from typing import Any, Dict, List

from dict2xml import dict2xml
from flasgger import swag_from
from flask import Response, abort, request
from flask_restful import Resource

from web_app.constants import MyEnum
from web_app.data_transformation_func import (create_report, get_order,
                                              info_driver_about,
                                              made_driver_info, made_report,
                                              made_short_report)


def output_formatted_data(format_value: MyEnum, info_list: List[Any] | dict) -> Response:
    if format_value == MyEnum.xml:
        resp = dict2xml(info_list, wrap="all", indent=" ")
        return Response(response=resp, status=200, headers={'Content-Type': 'application/xml'})
    else:
        json_str = json.dumps(info_list)
        return Response(response=json_str.encode('utf-8'), status=200, headers={'Content-Type': 'application/json'})


class Report(Resource):
    @swag_from('swagger/report.yml')
    def get(self) -> List[Dict[str, Any]] | Response:
        data = create_report()
        order = get_order(request.args.get('order', default='asc'))
        response_format = MyEnum(request.args.get('format', default='json'))
        response = made_report(data, order)

        return output_formatted_data(response_format, response)


class ShortReport(Resource):
    @swag_from('swagger/short_report.yml')
    def get(self) -> List[Dict[str, Any]] | Response:
        data = create_report()
        order = get_order(request.args.get('order', default=''))
        response_format = MyEnum(request.args.get('format', default='json'))
        response = made_short_report(data, order)

        return output_formatted_data(response_format, response)


class ReportDriver(Resource):

    @swag_from('swagger/report_driver.yml')
    def get(self, driver_abbr: str) -> dict[str, datetime | None | str] | Response:
        data = create_report()
        response_format = MyEnum(request.args.get('format', default='json'))
        driver = info_driver_about(data, driver_abbr)

        if not driver:
            abort(404, response={"message": "Driver {} doesn't exist".format(driver_abbr)})
        response = made_driver_info(driver)

        return output_formatted_data(response_format, response)
