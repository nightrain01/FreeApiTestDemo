from urllib.parse import urljoin

import requests


class FreeApiGroup0:
    def __init__(self):
        self.base_url = 'https://test.harumoe.cn/'

    def hot(self, list, cache, lang):
        url = urljoin(self.base_url, '/api/other/hot')
        print(url)
        param = {
            'list': list,
            'cache': cache,
            'lang': lang,
        }
        res = requests.get(url, verify=False, params=param)
        return res
