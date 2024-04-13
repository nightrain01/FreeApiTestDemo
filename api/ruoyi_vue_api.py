from urllib.parse import urljoin

import requests

from util.captcha_image_process import manual_get_captcha


class RuoyiVueApi:
    """
    Ruoyi-Vue的Api
    用于测试
    """

    def __init__(self):
        self.base_url = 'https://vue.ruoyi.vip/'
        self.session = requests.Session()
        self.session_init()

    def session_init(self):
        header = {
            'Content-Type': 'application/json;charset=UTF-8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/123.0.0.0 Safari/537.36',
        }
        self.session.headers.update(header)

    def login(self):
        """
        登录
        :return:
        """
        url = urljoin(self.base_url, '/prod-api/login')
        uuid, captcha_img_base64 = self.get_captcha_image()
        captcha_res = manual_get_captcha(captcha_img_base64)
        json_data = {
            'username': 'admin',
            'password': 'admin123',
            'uuid': uuid,
            'code': captcha_res,
        }
        res = self.session.post(url, json=json_data)
        self.session.headers.update({'Authorization': 'Bearer ' + res.json()['token']})
        return res

    def logout(self):
        """
        登出
        :return:
        """
        pass

    def get_info(self):
        """
        获取信息
        :return:
        """
        url = urljoin(self.base_url, '/prod-api/getInfo')
        res = requests.get(url)
        return res

    def get_captcha_image(self):
        """
        获取验证码
        :return: uuid, captcha_img_base64
        """
        url = urljoin(self.base_url, '/prod-api/captchaImage')
        res = self.session.get(url)
        res_json = res.json()
        uuid = res_json['uuid']
        captcha_img_base64 = res_json['img']
        return uuid, captcha_img_base64


if __name__ == '__main__':
    api = RuoyiVueApi()
    print(api.login().json())
    print(api.get_info().json())
    print(api.session.cookies.get_dict())
