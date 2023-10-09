from booker_api_tests.conftest import *


@external_decorator
def test_create_booking():
    print(f"\n\t\tfunction {test_create_booking.__name__} called")

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

    print(f"\n\t\tfunction {test_create_booking.__name__} done")


