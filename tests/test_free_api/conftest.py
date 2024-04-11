import pytest

from api.free_api_group0 import FreeApiGroup0


@pytest.fixture(scope='package')
def get_free_api_group0():
    return FreeApiGroup0()
