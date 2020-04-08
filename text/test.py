#encoding:utf-8
import json

def a():
    i = 0   # 统计响应码不为200的
    count = 0  #  统计文件的行数
    # f = open('12.csv', 'r')

    for line in open('12.csv'):
        count += 1
        b = line.strip()
        # print(type(b))
        user_dict = json.loads(b)
        # print(type(user_dict))
        # print(line.strip())
        code = (user_dict["code"])
        # print(code)
        if code != 200:
            print(line.split())
            f = open(r"1.csv","a+")
            a = json.dumps(user_dict)
            f.writelines(a+"\n")
            i+=1

    f.close()
    print("总访问的接口数：%s" %count)
    print("返回code不为200的：%s" %i)
    print(str((i / count)*100) + '%')


if __name__ == '__main__':
    a()

