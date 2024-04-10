import pytest
import requests

from util.read_data import DataGetter


@pytest.mark.learning
@pytest.mark.parametrize('list, cache, lang, expect_code, expect_msg', DataGetter.get_parametrize_data()['test_hot'])
def test_hot_parametrize(api, list, cache, lang, expect_code, expect_msg):
    res = api.hot(list, cache, lang)
    res_json = res.json()
    assert res_json['code'] == expect_code
    assert res_json['msg'] == expect_msg


@pytest.mark.learning
@pytest.mark.parametrize('list, cache, lang, expect_code, expect_msg', DataGetter.get_parametrize_data()['test_hot'])
def test_hot_parametrize_copy(api, list, cache, lang, expect_code, expect_msg):
    res = api.hot(list, cache, lang)
    res_json = res.json()
    assert res_json['code'] == expect_code
    assert res_json['msg'] == expect_msg


if __name__ == '__main__':
    pytest.main()
