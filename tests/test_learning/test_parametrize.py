import pytest

from util.data.data_getters.learning_data_getter import LearningDataGetter


@pytest.mark.learning
class TestParametrize:
    data_getter = LearningDataGetter()
    data = data_getter.get_parametrize_data()

    @pytest.fixture(autouse=True)
    def get_api(self, api_learning):
        print('get api in class')
        self.api = api_learning

    @pytest.mark.learning
    @pytest.mark.parametrize('list, cache, lang, expect_code, expect_msg', data['test_hot'])
    def test_hot_parametrize(self, list, cache, lang, expect_code, expect_msg):
        res = self.api.hot(list, cache, lang)
        res_json = res.json()
        assert res_json['code'] == expect_code
        assert res_json['msg'] == expect_msg

    @pytest.mark.learning
    @pytest.mark.parametrize('list, cache, lang, expect_code, expect_msg', data['test_hot'])
    def test_hot_parametrize_copy(self, list, cache, lang, expect_code, expect_msg):
        res = self.api.hot(list, cache, lang)
        res_json = res.json()
        assert res_json['code'] == expect_code
        assert res_json['msg'] == expect_msg


if __name__ == '__main__':
    pytest.main()
