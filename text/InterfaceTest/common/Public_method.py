import unittest
import requests
import json
from InterfaceTest.common.config import Conf
from InterfaceTest.common.mylogin import mylogin
from InterfaceTest.testcase import goodsDetail
import time

class Public_method(unittest.TestCase):
    def setUp(self):
        self.cookie = mylogin()
        dict = goodsDetail.GoodsDetail.test_a_goodsDetail(self)
        self.skuId = dict["skuId"]

    """"字典表数据获取"""
    def test_a_dict(self):
        data = {
            'clientType': 2,
            'dataId': 256814540000430,
            'mobileModel': 'iPhone_X',
            'systemVersion': '12.1',
            'version': 105,
            'versionIos': 105,
            "type": 5,
        }
        response = requests.post(url=Conf.API_ADDRESS + "/sdapp/core/getParCode", data=data, cookies=self.cookie)
        result = json.loads(response.content)
        print(result)
        time.sleep(1)

    """客服咨询"""
    def test_b_selectAllCoreService(self):

        response = requests.get(url=Conf.API_ADDRESS+"/sdapp/core/coreService/selectAllCoreService",cookies=self.cookie)
        # result = json.loads(response.content)
        # print(result)
        # time.sleep(1)
        code = response.status_code
        if code == 200:
            result = json.loads(response.content)
            return result["result"][0]["list"][0]["id"]

    """客服咨询标题详细内容的查询"""
    def test_c_selectDetailContent(self):
        id = self.test_b_selectAllCoreService()
        data = {
            'id':id,
            'relation':'true',
        }
        response = requests.post(url=Conf.API_ADDRESS+"/sdapp/core/coreService/selectDetailContent",data=data,cookies=self.cookie)
        result = json.loads(response.content)
        print(result)
        time.sleep(1)

    """查询是否有未读消息"""
    def test_d_queryNotReadAnnouncement(self):

        response = requests.get(url=Conf.API_ADDRESS+"/sdapp/core/queryNotReadAnnouncement",cookies=self.cookie)
        result = json.loads(response.content)
        print(result)
        time.sleep(1)

    """修改版本号"""
    def  test_e_version(self):
        data = {
            'clientType': 2,
            'imei': 'D439B4B3-DB5D-4505-B38E-4AB6351B158E',
            'mobileModel': 'iPhone 6',
            'systemVersion': '11.1.1',
            'version': 108,
            'versionIos': 108,
            'weexVersion': 127,
        }
        response = requests.post(url=Conf.API_ADDRESS+"/sdapp/core/getCoreSysVer",data=data,cookies=self.cookie)
        result = json.loads(response.content)
        print(result)
        time.sleep(1)

    """省市区查询"""
    def test_f_arr(self):
        data = {
            'clientType': 2,
            'imei': 'D439B4B3-DB5D-4505-B38E-4AB6351B158E',
            'mobileModel': 'iPhone 6',
            'systemVersion': '11.1.1',
            'version': 108,
            'versionIos': 108,
            'weexVersion': 127,
        }
        response = requests.post(url=Conf.API_ADDRESS+"/sdapp/core/queryAllProvinces",data=data,cookies=self.cookie)
        result = json.loads(response.content)
        print(result)
        time.sleep(1)

    """链接地址接口"""
    def test_g_urlarr(self):
        data = {
            'clientType': 2,
            'imei': 'D439B4B3-DB5D-4505-B38E-4AB6351B158E',
            'mobileModel': 'iPhone 6',
            'systemVersion': '11.1.1',
            'version': 108,
            'versionIos': 108,
            'weexVersion': 127,
        }
        response = requests.post(url=Conf.API_ADDRESS + "/sdapp/core/url/findUrlList", data=data, cookies=self.cookie)
        result = json.loads(response.content)
        print(result)
        time.sleep(1)

    """校验库存"""
    def test_i_checkStock(self):
        tradeSkuVO = [{"num": 1, "skuId": "{}".format(self.skuId)}]
        data = {
            'clientType': 2,
            'imei': 'D439B4B3-DB5D-4505-B38E-4AB6351B158E',
            'mobileModel': 'iPhone 6',
            'systemVersion': '11.1.1',
            'version': 108,
            'versionIos': 108,
            'weexVersion': 127,
            'tradeSkuVO': '{}'.format(tradeSkuVO)
        }
        response = requests.post(url=Conf.API_ADDRESS+"/sdapp/trade/confirm/checkStock",data=data,cookies=self.cookie)
        result = json.loads(response.content)
        print(result)
        time.sleep(1)

    """玩客分享图片获取"""
    def test_j_playShare(self):
        data = {
            'imgUrl':'https://image.sudian178.com/sd/dictionary/one.jpg'
        }
        response = requests.post(url=Conf.API_ADDRESS+"/sdapp/core/share/playShare",data=data,cookies=self.cookie)
        result = json.loads(response.content)
        print(result)
        time.sleep(1)


    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()






