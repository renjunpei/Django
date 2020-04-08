#-*-coding:utf-8 -*-
#Auther:wenyy
#Date:2019-03-26

import xlrd
import os

def readexcel_data():
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    filename=os.path.join(BASE_DIR,'test_data/','interface.xlsx')
    data_file = xlrd.open_workbook(filename)#打开excel
    sheet = data_file.sheet_by_index(0)#读sheet
    nrows = sheet.nrows#行数
    ncols = sheet.ncols#列数
    #表头
    idx = sheet.row_values(0)
    #最终数据列表
    data = []
    #从第1行开始遍历循环所有行，获取每行的数据
    for i in range(1,nrows):
        row_data = sheet.row_values(i)
        #组建每一行数据的字典
        row_data_dict = {}
        #遍历数据的每一项，赋值进行数据字典
        # for j in range(len(row_data)):
        for j in range(ncols):
            ctype = sheet.cell(i,j).ctype
            item = row_data[j]
            if ctype == 2:
                item = str(int(item))
            row_data_dict[idx[j]] = item

            # row_data_dict['mobile'] = int(row_data_dict['mobile'])
        #将数据字典加入到data列表中
        data.append(row_data_dict)
    # print(data)
    return data
    # for i in range(1,nrows):
    #     for j in range(ncols):
    #         ctype = sheet.cell(i,j).ctype
    #         no = sheet.cell(i,j).value
    #         if ctype == 2:
    #             no = str(int(no))
    #         data.append(no)
    # print(data)

if __name__ == '__main__':
    readexcel_data()