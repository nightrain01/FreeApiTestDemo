from urllib.parse import urljoin

import requests


class FreeApiGroup0:
    def __init__(self):
        self.base_url0 = 'https://test.harumoe.cn/'
        self.base_url1 = 'http://realip.cc/'

    def hot(self, website_list, cache, lang):
        """
        api文档：https://www.free-api.com/doc/615
        :param website_list: 网站列表，逗号分隔
        :param cache: 是否缓存（True or False）
        :param lang: 语言（zh-cn默认，ru-ru，us-en...）
        :return 返回http请求结果
        """
        url = urljoin(self.base_url0, '/api/other/hot')
        param = {
            'list': website_list,
            'cache': cache,
            'lang': lang,
        }
        res = requests.get(url, verify=False, params=param)
        return res

    def ip(self, ip):
        """
        api文档：https://www.free-api.com/doc/561
        :param ip: ip地址
        :return: ip详细信息
        """
        url = urljoin(self.base_url1, '/')
        param = {
            'ip': ip,
        }
        res = requests.get(url, params=param)
        return res
