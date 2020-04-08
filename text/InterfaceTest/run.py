# -*- coding:utf-8-*-
import unittest
import time
from InterfaceTest import HTMLTestRunner
import os


# def report(testreport):#查找最新的测试报告
#     lists = os.listdir(testreport)#返回指定的文件夹包含的文件或文件夹的名字列表
#     lists.sort(key=lambda fn:os.path.getatime(testreport+"\\"+fn))#通过sort()方法重新按时间对目录下的文件进行排序
#     filename = os.path.join(testreport,lists[-1])#list[-1]取最新生成的文件或者文件夹
#     return filename

if __name__ == '__main__':
    case_path = os.path.join(os.getcwd(),'testcase')
    report_path = os.path.join(os.getcwd(),'report')
    discover = unittest.defaultTestLoader.discover(case_path,pattern='*.py',top_level_dir=None)
    time = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = os.path.join(report_path,time+'_result.html')
    fp = open(filename,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream = fp, title =u'接口测试报告', description='The results are following:')
    runner.run(discover)
    fp.close()
    # test_report = './report'
    # rep = report(test_report)

