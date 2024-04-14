import allure
import pytest


@allure.epic('若依-前后端分离版')
@allure.feature('登录、登出功能测试')
@pytest.mark.freeapi
class TestRuoyiVueLoginLogout:
    """
    测试Ruoyi-Vue的登录登出功能
    """

    @pytest.fixture(scope='function', autouse=True)
    def get_api(self, get_ruoyi_vue_api):
        """
        为每个实例获取api
        """
        self.api = get_ruoyi_vue_api
