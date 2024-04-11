import pprint

import pytest
import requests


@pytest.mark.learning
@pytest.mark.usefixtures('fixture_function', 'fixture_class', 'fixture_module', 'fixture_package', 'fixture_session')
def test_demo():
    print('my test demo')
    assert 1 == 1


@pytest.mark.learning
@pytest.mark.usefixtures('fixture_function', 'fixture_class', 'fixture_module', 'fixture_package', 'fixture_session')
def test_api_demo():
    print('test api demo')
    param = {
        'list': 'csdn',
        'cache': False,
        'lang': 'zh-cn',
    }
    res = requests.get('https://test.harumoe.cn/api/other/hot', verify=False, params=param)
    res_json = res.json()
    # print(res_json)
    # pprint.pprint(res_json)
    assert res_json['code'] == 200
    assert res_json['msg'] == '数据请求成功！'


@pytest.mark.learning
@pytest.mark.usefixtures('fixture_function', 'fixture_class', 'fixture_module', 'fixture_package', 'fixture_session')
def test_https_demo():
    print('test https demo')
    res = requests.get('https://www.baidu.com')
    # print(res.text)
    assert True


@pytest.mark.learning
def test_ruoyi():
    data = {
        'username': 'admin',
        'password': 'admin123',
        'code': '0',
        'uuid': '6be948213a9f4d2691b8c089d0426505'
    }
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/json;charset=UTF-8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
    }
    res = requests.post('https://vue.ruoyi.vip/prod-api/login', json=data, headers=headers)
    pprint.pprint(res.json())


if __name__ == '__main__':
    pytest.main()
