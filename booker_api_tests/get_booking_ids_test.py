from booker_api_tests.conftest import *


@external_decorator
def test_get_booking_ids():
    print(f"\n\t\tfunction {test_get_booking_ids.__name__} called")

    print(f'\n\t\tsending GET to {BASE_URL_BOOKING}')

    r = requests.get(f"{BASE_URL_BOOKING}")
    assert r.status_code == 200, "Unexpected status code"

    print(f'\n\t\treceived {r.status_code = }')

    print("\n\t\tReceived data:")
    print("\t\t", [x for x in r.json()])

    print(f"\n\t\tfunction {test_get_booking_ids.__name__} done")