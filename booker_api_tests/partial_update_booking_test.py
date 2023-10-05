from booker_api_tests.conftest import *


@external_decorator
def test_partial_update_booking(token, bookingid):
    print(f"\n\t\tfunction {test_partial_update_booking.__name__} called")

    print(f'\n\t\tusing {token = }')
    headers = {"Content-Type": "application/json",
               "Accept": "application/json",
               "Cookie": f"token={token}"}
    body = {"firstname": "James",
            "lastname": "Brown"}

    print(f'\n\t\tusing {bookingid = }')
    print(f'\n\t\tsending PATCH to {BASE_URL_BOOKING}/{bookingid}')

    r = requests.patch(f"{BASE_URL_BOOKING}/{bookingid}", headers=headers, json=body)

    assert r.status_code == 200, "Unexpected status code"

    print(f'\n\t\treceived {r.status_code = }')
    print(f"\n\t\tfunction {test_partial_update_booking.__name__} done")
