import configparser
import os

cf = configparser.ConfigParser()
# 获取当前位置
curpath = os.path.dirname(os.path.realpath(__file__))
location = os.path.join(curpath, "config.ini")
print(location)  # config.ini的路径
# 找到配置文件
cf.read(location,encoding='utf-8')
secs = cf.sections()
options=cf.options("school_role")
print("options",options)
items = cf.items("school_role")
print("items",items)
url = cf.get("school_role", "domesticConsumer")
cf.options("school_role")