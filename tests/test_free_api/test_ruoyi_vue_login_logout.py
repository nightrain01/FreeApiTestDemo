import allure
import pytest

from data.data_getters.free_api_data_getter import FreeApiDataGetter
from util.get_ip import get_ip


@allure.epic('若依-前后端分离版')
@allure.feature('登录、登出功能测试')
@pytest.mark.freeapi
class TestRuoyiVueLoginLogout:
    """
    测试Ruoyi-Vue的登录登出功能
    """
    data_getter = FreeApiDataGetter()
    data = data_getter.get_ruoyi_vue_data()

    @pytest.fixture(scope='function', autouse=True)
    def get_api(self, get_ruoyi_vue_api):
        """
        为每个实例获取api
        """
        self.api = get_ruoyi_vue_api

    @pytest.fixture(scope='function')
    def reset_api_session(self):
        """
        结束时重置api的session
        """
        yield
        self.api.reset_session()

    @allure.story('测试登录功能')
    @pytest.mark.usefixtures('reset_api_session')
    @pytest.mark.parametrize('testcase_title, username, password, expect_code, expect_msg', data['test_login'])
    def test_login(self, testcase_title, username, password, expect_code, expect_msg):
        """
        测试登录功能
        """
        res = self.api.login(username, password)
        res_json = res.json()
        assert expect_code == res_json['code']
        assert expect_msg == res_json['msg']


if __name__ == '__main__':
    pytest.main()
