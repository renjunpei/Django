#-*- coding:utf-8 -*-
import requests
from InterfaceTest.common.config import Conf

# session = requests.session()
def mylogin(mobile):
    data = {
        'mobile': mobile,
        'clientType': 3,
        'captcha':8888,
        'loginType':'sms',
        'versionAndr':104,
        'version':104,
        'systemVersion':'7.0',
        'imei':'860076030766777',
        'mobileModel':'HUAWEI NXT-AL10'
    }

    result = requests.post(url=Conf.API_ADDRESS + "/sdapp/login", data=data)
    # response = result.json()
    # print(response)
    # print(type(result))
    # cookies = requests.utils.dict_from_cookiejar(session.cookies)
    cookies = result.cookies
    # print(cookies)
    return cookies







if __name__ == '__main__':
    mylogin('18600000002')

