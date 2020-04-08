#-*- coding:utf-8 -*-
#Auther:wenyy
#Date:2019-03-26

class DevelopmentConfig(object):
    API_ADDRESS = 'http://123.157.216.154:8000'#测试环境外网
    # API_ADDRESS = 'http://192.168.11.230:8000'#测试环境内网





class ProductionConfig(object):
    API_ADDRESS = 'https://m.sudian178.com'#H5地址
    # API_ADDRESS = 'https://prerelease.sudian178.com'#预发环境


Conf = DevelopmentConfig