import unittest
import requests
import json
from InterfaceTest.common.config import Conf
from InterfaceTest.common.mylogin import mylogin
import time

class Brand(unittest.TestCase):

    def setUp(self):
        self.cookie = mylogin()

    # 一级分类
    def test_a_firstclass(self):
        data = {
            'clientType': 2,
            'imei': 'D439B4B3-DB5D-4505-B38E-4AB6351B158E',
            'mobileModel': 'iPhone 6',
            'systemVersion': '11.1.1',
            'version': 107,
            'versionIos': 107,
            'weexVersion': 200,
            'ifHavBrand':2
        }
        response = requests.post(url=Conf.API_ADDRESS+"/sdapp/goods/queryCategoryList",data=data,cookies=self.cookie)
        # result = json.loads(response.content)
        # print(result)
        code = response.status_code
        if code == 200:
            result = json.loads(response.content)
            return result["result"][0]["id"]

    # 根据一级分类搜索二三级分类，品牌
    def test_b_brandshar(self):
        id = self.test_a_firstclass()
        data = {
            'clientType': 2,
            'imei': 'D439B4B3-DB5D-4505-B38E-4AB6351B158E',
            'mobileModel': 'iPhone 6',
            'systemVersion': '11.1.1',
            'version': 108,
            'versionIos': 108,
            'weexVersion': 127,
            'categoryId':id
        }
        response = requests.post(url=Conf.API_ADDRESS+"/sdapp/goods/queryCategoryTwoAndBrandList",data=data,cookies=self.cookie)
        result = json.loads(response.content)
        print(result)
        time.sleep(1)

    # 根据一级得到三级分类
    def test_c_brandshar(self):
        id = self.test_a_firstclass()
        data = {
                'clientType': 2,
                'imei': 'D439B4B3-DB5D-4505-B38E-4AB6351B158E',
                'mobileModel': 'iPhone 6',
                'systemVersion': '11.1.1',
                'version': 108,
                'versionIos': 108,
                'weexVersion': 127,
                'categoryId': id
        }
        response = requests.post(url=Conf.API_ADDRESS + "/sdapp/goods//category/queryThreeByCategoryId", data=data,
                                     cookies=self.cookie)
        result = json.loads(response.content)
        print(result)
        time.sleep(1)

    # 分类品牌搜索
    def test_d_brandshar(self):
        id = self.test_a_firstclass()
        # print(id)
        data = {
                'clientType': 2,
                'imei': 'D439B4B3-DB5D-4505-B38E-4AB6351B158E',
                'mobileModel': 'iPhone 6',
                'systemVersion': '11.1.1',
                'version': 108,
                'versionIos': 108,
                'weexVersion': 127,
                'categoryId':id,
        }
        response = requests.post(url=Conf.API_ADDRESS + "/sdapp/goods/queryBrandTopCategoryList", data=data,cookies=self.cookie)
        result = json.loads(response.content)
        print(result)
        time.sleep(1)

    # 品牌墙
    def test_e_brandwall(self):
        data = {
            'clientType': 2,
            'imei': 'D439B4B3-DB5D-4505-B38E-4AB6351B158E',
            'mobileModel': 'iPhone 6',
            'systemVersion': '11.1.1',
            'version': 108,
            'versionIos': 108,
            'weexVersion': 127,
        }
        response = requests.post(url=Conf.API_ADDRESS+"/sdapp/goods/queryBrandCategoryList",data=data,cookies=self.cookie)
        # result = json.loads(response.content)
        # print(result)
        # time.sleep(1)
        code = response.status_code
        if code == 200:
            result = json.loads(response.content)
            return result["result"]["categoryList"][0]["brandList"][0]["id"]
    # 品牌详情
    def test_f_branddetail(self):
        brandId = self.test_e_brandwall()
        # print(brandId)
        data = {
            'clientType': 2,
            'imei': 'D439B4B3-DB5D-4505-B38E-4AB6351B158E',
            'mobileModel': 'iPhone 6',
            'systemVersion': '11.1.1',
            'version': 108,
            'versionIos': 108,
            'weexVersion': 127,
            'brandId':brandId,
        }
        response = requests.post(url=Conf.API_ADDRESS+"/sdapp/goods/brand/detail",data=data,cookies=self.cookie)
        result = json.loads(response.content)
        print(result)
        time.sleep(1)


        # # 一级分类
    # def test_g_firstclass(self):
    #     data = {
    #             'clientType': 2,
    #             'imei': 'D439B4B3-DB5D-4505-B38E-4AB6351B158E',
    #             'mobileModel': 'iPhone 6',
    #             'systemVersion': '11.1.1',
    #             'version': 107,
    #             'versionIos': 107,
    #             'weexVersion': 200,
    #             'ifHavBrand': 1
    #     }
    #     response = requests.post(url=Conf.API_ADDRESS + "/sdapp/goods/queryCategoryList", data=data,cookies=self.cookie)
    #     result = json.loads(response.content)
    #     print(result)
    #     time.sleep(1)







if __name__ == '__main__':
        unittest.main()