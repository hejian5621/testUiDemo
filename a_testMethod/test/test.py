# -*- coding: utf-8 -*-
# 连接数据库方法



import pymysql

ConnectToDatabase = pymysql.connect(host='47.106.245.240',port=3306,user='root',passwd='Root123..'
                                            ,db='jeeplus_ani_big',charset='utf8')
nonius = ConnectToDatabase.cursor() # 获取游标
sql = "SELECT * FROM sys_user"
list_data = nonius.execute(sql)
col = nonius.description
list = []
for i in range(len(col)):
    list.append(col[i][0])
print("list",list)
# 获取所有记录列表
results =nonius.fetchmany(list_data)
print("results:",results)
for i in results :
    print(i)
nonius.close()  # 关闭游标
ConnectToDatabase.close() #关闭数据库连接


