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
    res = requests.get('https://www.baidu.com', verify=False)
    print(res.text)