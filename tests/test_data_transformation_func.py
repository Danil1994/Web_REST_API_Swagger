import unittest
from datetime import datetime
from unittest.mock import patch

from task_6 import time_format

from tests.func_for_test import create_random_drivers_list
from web_app.data_transformation_func import (Driver, create_report,
                                              info_driver_about,
                                              made_driver_info, made_report,
                                              made_short_report)


class TestFunctions(unittest.TestCase):

    def setUp(self):
        self.report = create_random_drivers_list(3)
        self.driver1 = Driver(abbr='SVF',
                              name='Sebastian Vettel',
                              car='FERRARI',
                              start_time=datetime.strptime('2018-05-24_12:02:58.917', time_format),
                              end_time=datetime.strptime('2018-05-24_12:04:03.332', time_format),
                              lap_time='0:01:04.415')

        self.driver2 = Driver(abbr='LHM',
                              name='Lewis Hamilton',
                              car='MERCEDES',
                              start_time=datetime.strptime('2018-05-24_12:03:00.837', time_format),
                              end_time=datetime.strptime('2018-05-24_12:04:05.114', time_format),
                              lap_time='0:01:04.484')
        self.driver3 = Driver(abbr='KRF',
                              name='Kimi Raikkonen',
                              car='RED BULL',
                              start_time=datetime.strptime('2018-05-24_12:03:01.581', time_format),
                              end_time=datetime.strptime('2018-05-24_12:04:07.215', time_format),
                              lap_time='0:01:05.776')

        self.drivers_list = [self.driver1, self.driver2, self.driver3]

    def test_made_report(self):
        expected_output = [{'abbr': 'SVF',
                            'driver_name': 'Sebastian Vettel',
                            'end_time': datetime(2018, 5, 24, 12, 4, 3, 332000),
                            'lap_time': '0:01:04.415',
                            'start_time': datetime(2018, 5, 24, 12, 2, 58, 917000)},
                           {'abbr': 'LHM',
                            'driver_name': 'Lewis Hamilton',
                            'end_time': datetime(2018, 5, 24, 12, 4, 5, 114000),
                            'lap_time': '0:01:04.484',
                            'start_time': datetime(2018, 5, 24, 12, 3, 0, 837000)},
                           {'abbr': 'KRF',
                            'driver_name': 'Kimi Raikkonen',
                            'end_time': datetime(2018, 5, 24, 12, 4, 7, 215000),
                            'lap_time': '0:01:05.776',
                            'start_time': datetime(2018, 5, 24, 12, 3, 1, 581000)}]
        self.assertEqual(made_report(self.drivers_list, False), expected_output)
        expected_output.reverse()
        self.assertEqual(made_report(self.drivers_list, True), expected_output)

    def test_made_short_report(self):
        expected_output = [{'abbr': 'SVF', 'driver_name': 'Sebastian Vettel', 'lap_time': '0:01:04.415'},
                           {'abbr': 'LHM', 'driver_name': 'Lewis Hamilton', 'lap_time': '0:01:04.484'},
                           {'abbr': 'KRF', 'driver_name': 'Kimi Raikkonen', 'lap_time': '0:01:05.776'}]
        self.assertEqual(made_short_report(self.drivers_list, False), expected_output)
        expected_output.reverse()
        self.assertEqual(made_short_report(self.drivers_list, True), expected_output)

    def test_made_driver_info(self):
        expected_output = {'abbr': 'SVF',
                           'driver_name': 'Sebastian Vettel',
                           'end_time': datetime(2018, 5, 24, 12, 4, 3, 332000),
                           'lap_time': '0:01:04.415',
                           'start_time': datetime(2018, 5, 24, 12, 2, 58, 917000)}
        self.assertEqual(made_driver_info(self.driver1), expected_output)

    @patch('web_app.data_transformation_func.create_list_object')
    def test_create_report(self, mock_list_object):
        mock_list_object.return_value = self.report
        self.assertEqual(create_report(), self.report)
        mock_list_object.assert_called_once()

    def test_info_driver_about(self):
        for driver in self.drivers_list:
            self.assertEqual(info_driver_about(self.drivers_list, driver.abbr), driver)
