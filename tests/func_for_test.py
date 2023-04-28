from typing import Any

from faker import Faker
from task_6 import time_format

from web_app.data_transformation_func import Driver

not_random_drivers = [Driver(abbr='SVF', name='Sebastian Vallet', car='Ferrari'),
                      Driver(abbr="VBM", name="Valtteri Bottas", car='BMW'),
                      Driver(abbr="SVM", name="Stoffel Vandoorne", car='Volvo')]


def random_driver() -> Driver:
    fake = Faker()
    random_name = fake.name()
    random_car = fake.uuid4()
    random_abbr = fake.pystr(3, 3)
    start_time = fake.pystr_format(time_format)
    end_time = fake.pystr_format(time_format)
    lap_time = fake.pystr_format(time_format)
    return Driver(random_abbr, random_name, random_car, start_time, end_time, lap_time)


def create_random_drivers_list(number) -> list[Driver]:
    drivers = []
    for _ in range(number):
        driver = random_driver()
        drivers.append(driver)

    return drivers


def create_random_drivers_dict(number) -> list[dict[str, Any]]:
    drivers = []
    for _ in range(number):
        driver = random_driver()
        data_driver_dict = {'abbr': driver.abbr, 'car': driver.car, 'end_time': driver.end_time,
                            'lap_time': driver.lap_time,
                            'name': driver.name, 'start_time': driver.start_time}
        drivers.append(data_driver_dict)

    return drivers
