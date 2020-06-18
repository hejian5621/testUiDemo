# -*- coding: utf-8 -*-
# 接口调用测试

import requests,json
url = "http://47.106.245.240:8081/eosp/a/login"
pay ={"username":"swyonghu","password":"123456","mobileLogin":"true"}
req = requests.post(url,pay)  # 通过requests 发起请求
data = json.loads(req.text)
data = data["body"]
JSESSIONID = data["JSESSIONID"]
JSESSIONID = "JSESSIONID="+JSESSIONID


