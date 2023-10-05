from booker_api_tests.conftest import *


def test_create_token():
    print(f"\n\t\tfunction {test_create_token.__name__} called")

    r = requests.post(f"{BASE_URL_AUTH}", json=auth)
    assert r.status_code == 200, "Unexpected status code"

    print(f'\n\t\treceived {r.status_code = }')

    print("\n\t\tReceived data:")
    print("\t\t", [x for x in r.json().items()])

    print(f"\n\t\tfunction {test_create_token.__name__} done")
