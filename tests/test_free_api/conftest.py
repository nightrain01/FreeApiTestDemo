import pytest

from api.free_api_group0 import FreeApiGroup0
from api.ruoyi_vue_api import RuoyiVueApi


@pytest.fixture(scope='package')
def get_free_api_group0():
    """
    package级获取api实例
    提供给测试类实例注入
    """
    return FreeApiGroup0()


@pytest.fixture(scope='package')
def get_ruoyi_vue_api():
    """
    package级获取ruoyi-vue的api实例
    :return:
    """
    return RuoyiVueApi()
