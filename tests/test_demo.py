import pprint

import pytest
import requests


def test_demo():
    print('my test demo')
    assert 1 == 1


def test_api_demo():
    param = {
        'list': 'csdn',
        'cache': False,
        'lang': 'zh-cn',
    }
    res = requests.get('https://test.harumoe.cn/api/other/hot', verify=False, params=param)
    res_json = res.json()
    print(res_json)
    # pprint.pprint(res_json)
    assert res_json['code'] == 200
    assert res_json['msg'] == '数据请求成功！'


def test_https_demo():
    res = requests.get('https://www.baidu.com')
    print(res.text)
    assert True


if __name__ == '__main__':
    pytest.main()
