import time
import pytest
import requests

BASE_URL = "https://restful-booker.herokuapp.com/booking"
AUTH_URL = "https://restful-booker.herokuapp.com/auth"
PING_URL = "https://restful-booker.herokuapp.com/ping"
STATUS_OK = 200
STATUS_201 = 201

@pytest.fixture(scope='function')
def get_new_booking_id():
    payload = {
        "firstname": "John",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2023-10-10",
            "checkout": "2023-10-17"
        },
        "additionalneeds": "Breakfast"}

    response = requests.post(BASE_URL, json=payload)
    booking_id = response.json()['bookingid']
    yield booking_id


def test_get_all_bookings():
    response = requests.get(BASE_URL)
    # assert response.status_code == STATUS_OK
    print(response.headers)
    assert "Connection" in response.headers, "There is no expected headers"


def test_get_booking_with_id():
    response = requests.get(f'{BASE_URL}/1')
    response_data = response.json()
    print(response_data)
    expected_keys = ['firstname', 'lastname', 'totalprice', 'depositpaid', 'bookingdates']
    #print(len(response_data))
    #assert len(response_data) > 2
    # for key in expected_keys:
    #    assert key in response_data.keys()
    assert response_data['firstname'] == 'Mary'


def test_create_booking():
    payload = {
    "firstname" : "Jim",
    "lastname" : "Brown",
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2023-10-10",
        "checkout" : "2023-10-17"
    },
    "additionalneeds" : "Breakfast"}
    response = requests.post(BASE_URL, json=payload)
    print(response.json())
    assert response.status_code == STATUS_OK
    # надо проверить, что данные попали в базу
    id = response.json()['bookingid']
    get_response = requests.get(f'{BASE_URL}/{id}')
    assert get_response.json()['firstname'] == "Jim"


def test_create_booking_with_fixture(get_new_booking_id):
    response = requests.get(f'{BASE_URL}/{get_new_booking_id}')
    assert response.json()['firstname'] == "John"


# для удаления нужен токен = авторизация
@pytest.fixture(scope='function')
def token():
    payload = {
    "username" : "admin",
    "password" : "password123"}
    response = requests.post(AUTH_URL, json=payload)
    response_data = response.json()
    token = response_data['token']
    # токен нужно сохранить и передать в другой метод = фикстура
    # print(response_data)
    assert response.status_code == STATUS_OK
    yield token


def test_delete_new_booking(get_new_booking_id, token):
    headers = {'Cookie': f'token={token}'}
    response = requests.delete(f'{BASE_URL}/{get_new_booking_id}', headers=headers)
    assert response.status_code == STATUS_201
    # check now
    get_response = requests.get(f'{BASE_URL}/{get_new_booking_id}')
    assert get_response.status_code == 404


def test_booking_health_check():
    response = requests.get(PING_URL)
    print(response.headers)
    assert response.status_code == STATUS_201


def test_update_booking(get_new_booking_id, token):
    payload = {
        "firstname": "NewName",
        "lastname": "AAA",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2023-10-10",
            "checkout": "2023-10-17"
        },
        "additionalneeds": "otheer"}

    headers = {'Cookie': f'token={token}'}
    response = requests.put(f'{BASE_URL}/{get_new_booking_id}', headers=headers, json=payload)
    print(response.json())
    assert response.status_code == STATUS_OK


def test_update_part_booking(get_new_booking_id, token):
    payload = {
        "firstname": "Part Name",
        "lastname": "Update",
        "additionalneeds": "new add"}

    headers = {'Cookie': f'token={token}'}
    response = requests.patch(f'{BASE_URL}/{get_new_booking_id}', headers=headers, json=payload)
    print(response.json())
    assert response.status_code == STATUS_OK

