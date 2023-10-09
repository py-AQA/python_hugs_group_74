from booker_api_tests.conftest import *


@external_decorator
def test_delete_booking(token, bookingid):
    print(f"\n\t\tfunction {test_delete_booking.__name__} called")

    print(f'\n\t\tusing {token = }')
    headers = {"Content-Type": "application/json", "Cookie": f"token={token}"}

    print(f'\n\t\tusing {bookingid = }')

    print(f'\n\t\tsending DELETE to {BASE_URL_BOOKING}/{bookingid}')

    r = requests.delete(f"{BASE_URL_BOOKING}/{bookingid}", headers=headers)

    assert r.status_code == 201, "Unexpected status code"

    print(f'\n\t\treceived {r.status_code = }')
    print(f"\n\t\tfunction {test_delete_booking.__name__} done")