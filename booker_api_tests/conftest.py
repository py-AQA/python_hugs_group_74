import pytest
import requests
from functools import wraps


BASE_URL_BOOKING = "https://restful-booker.herokuapp.com/booking"
BASE_URL_AUTH = "https://restful-booker.herokuapp.com/auth"
BASE_URL_PING = "https://restful-booker.herokuapp.com/ping"

auth = {
    "username": "admin",
    "password": "password123"
}


@pytest.fixture(scope='function')
def token():
    print(f"\n\t\tfixture {token.__name__} called")

    print(f'\n\t\tsending POST to  {BASE_URL_AUTH = }')

    r = requests.post(f"{BASE_URL_AUTH}", json=auth)
    assert r.status_code == 200, "Unexpected status code"

    print(f'\n\t\treceived {r.status_code = }')

    print("\n\t\tReceived data:")
    print("\t\t", [x for x in r.json().items()])

    print(f'\n\t\tyield { r.json()["token"] = }')

    yield r.json()['token']

    print(f"\n\t\tfixture {token.__name__} continue execution after yield")
    print(f"\n\t\tfixture {token.__name__} done")


@pytest.fixture(scope='function')
def bookingid():
    print(f"\n\t\tfixture {bookingid.__name__} called")

    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    body = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    print(f'\n\t\tsending POST to  {BASE_URL_BOOKING = }')

    r = requests.post(f"{BASE_URL_BOOKING}", json=body, headers=headers)
    assert r.status_code == 200, "Unexpected status code"

    print(f'\n\t\treceived {r.status_code = }')

    print("\n\t\tReceived data:")
    print("\t\t", [x for x in r.json().items()])

    print(f'\n\t\tyield { r.json()["bookingid"] = }')

    yield r.json()["bookingid"]

    print(f"\n\t\tfixture {bookingid.__name__} continue execution after yield")
    print(f"\n\t\tfixture {bookingid.__name__} done")


def external_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"\n\t*external_decorator: Вызвана функция {func.__name__} с аргументами {args} и ключевыми аргументами {kwargs}.")
        result = func(*args, **kwargs)
        print(f"\n\t*external_decorator: Функция {func.__name__} вернула {result}.")
        return result
    return wrapper