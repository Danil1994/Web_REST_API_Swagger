import unittest
from unittest.mock import patch

from flask import json

from tests.func_for_test import create_random_drivers_list, not_random_drivers
from web_app.create_app import app


class TestReport(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = app.test_client()
        cls.random_data = create_random_drivers_list(10)
        cls.not_random = not_random_drivers

    @patch('web_app.api.create_report')
    def test_report_json(self, mock_create_report) -> None:
        mock_create_report.return_value = self.random_data
        response = self.client.get('/api/v1/report')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
        self.assertEqual(self.random_data[0].abbr, response.get_json()[0]['abbr'])
        keys = ('abbr', 'driver_name', 'lap_time', 'start_time', 'end_time')
        for key in keys:
            self.assertTrue(response.get_json()[0][key])
        mock_create_report.assert_called_once()

    @patch('web_app.api.create_report')
    def test_report_xml(self, mock_create_report) -> None:
        mock_create_report.return_value = self.random_data
        response = self.client.get('/api/v1/report?format=xml')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/xml')
        mock_create_report.assert_called_once()

    @patch('web_app.api.create_report')
    def test_short_report_json(self, mock_create_report) -> None:
        mock_create_report.return_value = self.random_data
        response = self.client.get('/api/v1/report/drivers?format=json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
        mock_create_report.assert_called_once()

    @patch('web_app.api.create_report')
    def test_short_report_xml(self, mock_create_report) -> None:
        mock_create_report.return_value = self.random_data
        response = self.client.get('/api/v1/report/drivers?format=xml')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/xml')
        mock_create_report.assert_called_once()

    @patch('web_app.api.create_report')
    def test_report_driver_json(self, mock_create_report) -> None:
        mock_create_report.return_value = self.random_data
        response = self.client.get('/api/v1/report/drivers/SVF?format=json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
        mock_create_report.assert_called_once()

    @patch('web_app.api.create_report')
    def test_report_driver_xml(self, mock_create_report) -> None:
        mock_create_report.return_value = self.not_random
        response = self.client.get('/api/v1/report/drivers/SVF?format=xml')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/xml')
        mock_create_report.assert_called_once()

    @patch('web_app.api.create_report')
    def test_report_driver_not_found(self, mock_create_report) -> None:
        mock_create_report.return_value = self.random_data
        response = self.client.get('/api/v1/report/drivers/XXX?format=json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
        expected = {"message": "Driver XXX doesn't exist"}
        self.assertEqual(json.loads(response.data), expected)
        mock_create_report.assert_called_once()
