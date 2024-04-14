from urllib.parse import urljoin

import requests

from util.captcha_image_process import ocr_get_captcha, manual_get_captcha, \
    calculate_captcha_recognition_get_ruoyi_captcha


class RuoyiVueApi:
    """
    Ruoyi-Vue的Api
    用于测试
    """

    def __init__(self):
        self.base_url = 'https://vue.ruoyi.vip/'
        self.session = requests.Session()
        self._session_init()

    def _session_init(self):
        """
        session初始化
        :return:
        """
        header = {
            'Content-Type': 'application/json;charset=UTF-8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/123.0.0.0 Safari/537.36',
        }
        self.session.headers.update(header)

    def reset_session(self):
        """
        重置session
        :return:
        """
        self.session.close()
        self.session = requests.Session()
        self._session_init()

    def login(self, username='admin', password='admin123', retry_times=5):
        """
        带重试的登录
        验证码识别不是很准！
        尽可能保证能登录
        :param username:
        :param password:
        :param retry_times: 重试次数
        :return:
        """
        res = self._login(username, password)
        res_json = res.json()
        for i in range(retry_times):
            if res_json['code'] == 500 and res_json['msg'] == '验证码错误':
                res = self._login(username, password)
                res_json = res.json()
            else:
                break
        return res

    def _login(self, username='admin', password='admin123'):
        """
        登录
        :param username:
        :param password:
        :return:
        """
        url = urljoin(self.base_url, '/prod-api/login')
        uuid, captcha_img_base64 = self._get_captcha_image()
        captcha = calculate_captcha_recognition_get_ruoyi_captcha(captcha_img_base64)
        json_data = {
            'username': username,
            'password': password,
            'uuid': uuid,
            'code': captcha,
        }
        res = self.session.post(url, json=json_data)
        self._authorization(res)
        return res

    def logout(self):
        """
        登出
        :return:
        """
        url = urljoin(self.base_url, '/prod-api/logout')
        res = self.session.post(url)
        return res

    def get_info(self):
        """
        获取信息
        :return:
        """
        url = urljoin(self.base_url, '/prod-api/getInfo')
        res = self.session.get(url)
        return res

    def _authorization(self, res):
        """
        认证信息添加
        :return:
        """
        try:
            res_json = res.json()
            token = res_json['token']
            self.session.headers.update({'Authorization': f'Bearer {token}'})
        except KeyError as e:
            print(f'KeyError:{e}')

    def _get_captcha_image(self):
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
    print(api.login('asdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdf', 'aaa').json())
    print(api.login().json())
    print(api.get_info().json())
    print(api.logout().json())
    print(api.get_info().json())
