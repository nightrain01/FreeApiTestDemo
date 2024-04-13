import requests


def get_ip():
    """
    获取本机公网ip
    :return: 本机公网ip
    """
    res = requests.get('https://checkip.amazonaws.com')
    return res.text.strip()
