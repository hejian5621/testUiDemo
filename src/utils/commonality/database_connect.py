# 数据库连接

import pymysql
from config.readconfig import ProfileDataProcessing
import  time


class ReadDatabase():


    def __init__(self,sql):
        # sql语句
        self.sql =sql
        self.platform =None


    """
    1、连接数据库
    2、数据库增删改查
    """
    def ConnectToDatabase(self):
        """
        数据查询学校运维测试服
        :param sql: sql语句
        :return: 在数据库查到的数据
        """
        ConnectToDatabase=1;list_data=None
        self.platform = ProfileDataProcessing.allocation()
        n = 1
        m = False
        while n <=10 and m == False:
            if  self.platform =="school_":
                try:
                    ConnectToDatabase = pymysql.connect(host='47.106.245.240', port=3306, user='root', passwd='Root123..'
                                                        , db='jeeplus_ani_big', charset='utf8')
                    m = True
                except:
                    print("数据库连接失败，第%r次连接数据库" % n)
                    m = False
                    n = n + 1
                    time.sleep(2)
            elif  self.platform =="statecos_":
                try:
                    ConnectToDatabase = pymysql.connect(host='47.106.245.240', port=3306, user='root', passwd='Root123..'
                                                        , db='jeeplus_ani_big_zq', charset='utf8')
                    m = True
                except:
                    print("数据库连接失败，第%r次连接数据库" % n)
                    m = False
                    n = n + 1
                    time.sleep(2)
            if m  and n > 1:
                print("数据库连接成功")
        nonius = ConnectToDatabase.cursor()  # 获取游标
        try:
            list_data = nonius.execute(self.sql)    # 输入sql语句
        except:
            print("sql语句错误,错误的SQL：",self.sql)
        col = nonius.description           # 获取数据库表里的列表名
        list_name = []
        list_information =[]
        for i in range(len(col)):
            list_name.append(col[i][0])
        results = nonius.fetchmany(list_data)  # 获取所有记录列表
        for i in results:
            data = dict(zip(list_name,i))
            list_information.append(data)
        nonius.close()  # 关闭游标
        ConnectToDatabase.close()  # 关闭数据库连接
        return  list_information








    def AssetManagementLibrary(self):
        """
        数据查询资产管理
        :param sql: sql语句
        :return: 在数据库查到的数据
        """
        ConnectToDatabase=1
        self.platform = ProfileDataProcessing.allocation()
        n = 1
        m = False
        while n <= 10 and m == False:
            try:
                ConnectToDatabase = pymysql.connect(host='47.106.245.240', port=3306, user='root', passwd='Root123..'
                                                    ,db='eams', charset='utf8')
                m = True
            except:
                print("数据库连接失败，第%r次连接数据库" % n)
                m = False
                n = n + 1
                time.sleep(2)
            if m and n>1 :
                print("数据库连接成功")
        nonius = ConnectToDatabase.cursor()  # 获取游标
        list_data = nonius.execute(self.sql)    # 输入sql语句
        col = nonius.description           # 获取数据库表里的列表名
        list_name = []
        list_information =[]
        for i in range(len(col)):
            list_name.append(col[i][0])
        results = nonius.fetchmany(list_data)  # 获取所有记录列表
        for i in results:
            data = dict(zip(list_name,i))
            list_information.append(data)
        nonius.close()  # 关闭游标
        ConnectToDatabase.close()  # 关闭数据库连接
        return  list_information