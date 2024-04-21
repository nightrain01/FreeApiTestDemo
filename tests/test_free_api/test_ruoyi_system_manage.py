import allure
import pytest

from data.data_getters.free_api_data_getter import FreeApiDataGetter


@allure.epic('若依-前后端分离版')
@allure.feature('系统管理功能测试')
@pytest.mark.freeapi
@pytest.mark.ruoyi
class TestRuoyiSystemManage:
    """
    测试Ruoyi-Vue的系统管理功能
    """
    data_getter = FreeApiDataGetter()
    data = data_getter.get_ruoyi_vue_data()

    @pytest.fixture(scope='function', autouse=True)
    def get_api(self, get_ruoyi_vue_api):
        """
        为每个实例获取api
        """
        self.api = get_ruoyi_vue_api

    @pytest.fixture(scope='function', autouse=True)
    def reset_api_session(self):
        """
        结束时重置api的session
        """
        yield
        self.api.reset_session()

    @allure.story('测试获取用户列表功能')
    @pytest.mark.parametrize('testcase_title, login, page_num, page_size, expect_code, expect_msg',
                             data['test_list_system_user'])
    def test_list_system_user(self, testcase_title, login, page_num, page_size, expect_code, expect_msg):
        """
        测试获取用户列表功能
        """
        if login:
            self.api.login()
        res = self.api.list_system_users(page_num, page_size)
        res_json = res.json()
        assert expect_code == res_json['code']
        assert expect_msg == res_json['msg']
        if res_json['code'] == 200:
            total = int(res_json['total'])
            t_page_size = page_size if isinstance(page_size, int) else 10
            real_page_size = len(res_json['rows'])
            assert t_page_size if total > t_page_size else total == real_page_size

    @allure.story('测试获取单个用户信息功能')
    @pytest.mark.parametrize('testcase_title, login, user_id, expect_code, expect_msg', data['test_get_system_user'])
    def test_get_system_user(self, testcase_title, login, user_id, expect_code, expect_msg):
        """
        测试获取单个用户信息功能
        """
        if login:
            self.api.login()
        res = self.api.get_system_user(user_id)
        res_json = res.json()
        assert expect_code == res_json['code']
        assert expect_msg == res_json['msg']

    @allure.story('测试删除用户（演示模式意思意思，不搞太多用例了）')
    @pytest.mark.parametrize('testcase_title, login, user_id, expect_code, expect_msg', data['test_delete_system_user'])
    def test_delete_system_user(self, testcase_title, login, user_id, expect_code, expect_msg):
        """
        测试删除用户功能
        """
        if login:
            self.api.login()
        res = self.api.delete_system_user(user_id)
        res_json = res.json()
        assert expect_code == res_json['code']
        assert expect_msg == res_json['msg']
