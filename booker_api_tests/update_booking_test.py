from booker_api_tests.conftest import *


@external_decorator
def test_update_booking(token, bookingid):
    print(f"\n\t\tfunction {test_update_booking.__name__} called")

    print(f'\n\t\tvalue {bookingid = }')

    print(f'\n\t\tusing {token = }')
    headers = {"Content-Type": "application/json",
               "Accept": "application/json",
               "Cookie": f"token={token}"}
    body = {
        "firstname": "J___s",
        "lastname": "B___n",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    print(f'\n\t\tusing {bookingid = }')

    print(f'\n\t\tsending PUT to {BASE_URL_BOOKING}/{bookingid}')

    r = requests.put(f"{BASE_URL_BOOKING}/{bookingid}", headers=headers, json=body)

    assert r.status_code == 200, "Unexpected status code"

    print(f'\n\t\treceived {r.status_code = }')
    print(f"\n\t\tfunction {test_update_booking.__name__} done")
