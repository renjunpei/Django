import unittest
import requests
import json
from InterfaceTest.common.config import Conf
from InterfaceTest.common.mylogin import mylogin
import time

class Shopcar(unittest.TestCase):
    def setUp(self):
        self.cookie = mylogin()

    # 购物车列表有效商品
    def test_a_ShopCarIndexOne(self):
        data = {
            'clientType':2,
            'imei':'D439B4B3-DB5D-4505-B38E-4AB6351B158E',
            'mobileModel': 'iPhone 6',
            'systemVersion': '11.1.1',
            'version': 107,
            'versionIos': 107,
            'weexVersion': 127,
        }
        response = requests.get(url=Conf.API_ADDRESS+"/sdapp/shop/car/getShopCarIndexOne",data=data,cookies=self.cookie)
        # result = json.loads(response.content)
        # print(result)
        # time.sleep(1)
        code = response.status_code
        if code == 200:
            result = json.loads(response.content)
            return result["result"][0]["shopCarDtos"][0]["cartId"]

    # 购物车列表无效商品
    def test_b_ShopCarIndexTwo(self):
        data = {
            'clientType': 2,
            'imei': 'D439B4B3-DB5D-4505-B38E-4AB6351B158E',
            'mobileModel': 'iPhone 6',
            'systemVersion': '11.1.1',
            'version': 107,
            'versionIos': 107,
            'weexVersion': 127,
            'page':1,
        }
        print(data)
        response = requests.get(url=Conf.API_ADDRESS + "/sdapp/shop/car/getShopCarIndexTwo", data=data,cookies=self.cookie)
        result = json.loads(response.content)
        print(result)
        time.sleep(1)

    # 清空失效商品
    def test_c_delInvalidShopCar(self):
        data = {
            'clientType': 2,
            'imei': 'D439B4B3-DB5D-4505-B38E-4AB6351B158E',
            'mobileModel': 'iPhone 6',
            'systemVersion': '11.1.1',
            'version': 107,
            'versionIos': 107,
            'weexVersion': 127,
        }
        response = requests.post(url=Conf.API_ADDRESS+"/sdapp/shop/car/delInvalidShopCar",data=data,cookies=self.cookie)
        result = json.loads(response.content)
        print(result)
        time.sleep(1)

    # 购物车数量
    def test_d_carCount(self):
        data = {
            'clientType': 2,
            'imei': 'D439B4B3-DB5D-4505-B38E-4AB6351B158E',
            'mobileModel': 'iPhone 6',
            'systemVersion': '11.1.1',
            'version': 107,
            'versionIos': 107,
            'weexVersion': 127,
        }
        response = requests.post(url=Conf.API_ADDRESS + "/sdapp/shop/car/carCount", data=data,cookies=self.cookie)
        result = json.loads(response.content)
        print(result)
        time.sleep(1)

    # 删除购物车商品数据
    def test_f_defshopcar(self):
        carId = self.test_a_ShopCarIndexOne()
        data = {
            'clientType': 2,
            'imei': 'D439B4B3-DB5D-4505-B38E-4AB6351B158E',
            'mobileModel': 'iPhone 6',
            'systemVersion': '11.1.1',
            'version': 107,
            'versionIos': 107,
            'weexVersion': 127,
            'cartIds':carId,
        }
        response = requests.post(url=Conf.API_ADDRESS+"/sdapp/shop/car/delShopCar",data=data,cookies=self.cookie)
        result = json.loads(response.content)
        print(result)
        time.sleep(1)





if __name__ == '__main__':
    unittest.main()