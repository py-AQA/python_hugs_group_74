from booker_api_tests.conftest import *


@external_decorator
def test_health_check():
    print(f"\n\t\tfunction {test_health_check.__name__} called")

    print(f'\n\t\tsending GET to {BASE_URL_PING = }')

    r = requests.get(f"{BASE_URL_PING}")

    assert r.status_code == 201, "Unexpected status code"

    print(f'\n\t\treceived {r.status_code = }')
    print(f"\n\t\tfunction {test_health_check.__name__} done")
