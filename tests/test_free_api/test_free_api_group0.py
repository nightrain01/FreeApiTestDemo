import allure
import pytest

from util.data.data_getters.free_api_data_getter import FreeApiDataGetter


@allure.epic('测试免费Api')
@allure.feature('免费Api测试（第0组）')
@pytest.mark.freeapi
class TestFreeApiGroup0:
    data_getter = FreeApiDataGetter()
    data = data_getter.get_free_api_group0_data()

    @pytest.fixture(scope="function", autouse=True)
    def get_api(self, get_free_api_group0):
        self.api = get_free_api_group0

    @allure.story('测试热搜Api')
    @allure.title('{usecase_title}')
    @pytest.mark.parametrize('usecase_title, website_list, cache, lang, expect_code, expect_msg', data['test_hot'])
    def test_hot(self, usecase_title, website_list, cache, lang, expect_code, expect_msg):
        res = self.api.hot(website_list, cache, lang)
        res_json = res.json()
        assert expect_code == res_json['code']
        assert expect_msg == res_json['msg']


if __name__ == '__main__':
    pytest.main()
