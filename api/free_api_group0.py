from urllib.parse import urljoin

import requests


class FreeApiGroup0:
    def __init__(self):
        self.base_url = 'https://test.harumoe.cn/'

    def hot(self, website_list, cache, lang):
        '''
        api文档：https://www.free-api.com/doc/615
        '''
        url = urljoin(self.base_url, '/api/other/hot')
        param = {
            'list': website_list,
            'cache': cache,
            'lang': lang,
        }
        res = requests.get(url, verify=False, params=param)
        return res
