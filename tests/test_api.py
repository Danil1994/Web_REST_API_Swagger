import unittest
from unittest.mock import patch

from flask import json

from tests.func_for_test import create_random_drivers_dict
from web_app.create_app import app


class TestReport(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = app.test_client()
        cls.data = create_random_drivers_dict(10)
        cls.one_driver = {'abbr': 'SVF', 'car': 'FERRARI', 'end_time': '2018-05-24_12:04:03.332',
                          'lap_time': '0:01:04.415',
                          'name': 'Sebastian Vettel', 'start_time': '2018-05-24_12:02:58.917'}

    @patch('web_app.api.made_report')
    @patch('web_app.api.create_report')
    def test_report_json(self, mock_create_report, mock_made_report) -> None:
        mock_create_report.return_value = self.data
        mock_made_report.return_value = self.data
        response = self.client.get('/api/v1/report')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
        mock_create_report.assert_called_once()
        mock_made_report.assert_called_once()

    @patch('web_app.api.made_report')
    @patch('web_app.api.create_report')
    def test_report_xml(self, mock_create_report, mock_made_report) -> None:
        mock_create_report.return_value = self.data
        mock_made_report.return_value = self.data
        response = self.client.get('/api/v1/report?format=xml')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/xml')
        mock_create_report.assert_called_once()
        mock_made_report.assert_called_once()

    @patch('web_app.api.made_short_report')
    @patch('web_app.api.create_report')
    def test_short_report_json(self, mock_create_report, mock_short_report) -> None:
        mock_create_report.return_value = self.data
        mock_short_report.return_value = self.data
        response = self.client.get('/api/v1/report/drivers?format=json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
        mock_create_report.assert_called_once()
        mock_short_report.assert_called_once()

    @patch('web_app.api.made_short_report')
    @patch('web_app.api.create_report')
    def test_short_report_xml(self, mock_create_report, mock_short_report) -> None:
        mock_create_report.return_value = self.data
        mock_short_report.return_value = self.data
        response = self.client.get('/api/v1/report/drivers?format=xml')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/xml')
        mock_create_report.assert_called_once()
        mock_short_report.assert_called_once()

    @patch('web_app.api.made_driver_info')
    @patch('web_app.api.info_driver_about')
    @patch('web_app.api.create_report')
    def test_report_driver_json(self, mock_create_report, mock_driver_info, mock_made_driver_info) -> None:
        mock_create_report.return_value = self.data
        mock_driver_info.return_value = self.one_driver
        mock_made_driver_info.return_value = self.one_driver
        response = self.client.get('/api/v1/report/drivers/SVF?format=json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
        mock_create_report.assert_called_once()
        mock_driver_info.asseert_called_once()
        mock_made_driver_info.assert_called_once()

    @patch('web_app.api.made_driver_info')
    @patch('web_app.api.info_driver_about')
    @patch('web_app.api.create_report')
    def test_report_driver_xml(self, mock_create_report, mock_driver_info, mock_made_driver_info) -> None:
        mock_create_report.return_value = self.data
        mock_driver_info.return_value = self.one_driver
        mock_made_driver_info.return_value = self.one_driver
        response = self.client.get('/api/v1/report/drivers/SVF?format=xml')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/xml')
        mock_create_report.assert_called_once()
        mock_driver_info.asseert_called_once()
        mock_made_driver_info.assert_called_once()

    @patch('web_app.api.made_driver_info')
    @patch('web_app.api.info_driver_about')
    @patch('web_app.api.create_report')
    def test_report_driver_not_found(self, mock_create_report, mock_driver_info, mock_made_driver_info) -> None:
        mock_create_report.return_value = self.data
        mock_driver_info.return_value = None
        mock_made_driver_info.return_value = self.one_driver
        response = self.client.get('http://localhost:5080/api/v1/report/drivers/XXX?format=json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
        expected = {"message": "Driver XXX doesn't exist"}
        self.assertEqual(json.loads(response.data), expected)
        mock_create_report.assert_called_once()
        mock_driver_info.asseert_called_once()
        mock_made_driver_info.assert_not_called()
