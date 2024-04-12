import pytest

from api.free_api_group0 import FreeApiGroup0


@pytest.fixture(scope='package')
def get_free_api_group0():
    """
    package级获取api实例
    提供给测试类实例注入
    """
    return FreeApiGroup0()
