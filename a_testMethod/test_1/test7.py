from appletConnector import rests
import requests

url = "http://47.106.245.240:8081/eosp/a/login"
pay ={"username":"swyonghu","password":"123456","mobileLogin":"true"}
req = requests.post(url,pay)  # 通过requests 发起请求
# print("req.text:",req.text)
# data = json.loads(req.text)
# print("data:",data)
# data = data["body"]
# JSESSIONID = data["JSESSIONID"]
# JSESSIONID = "JSESSIONID="+JSESSIONID



deviceList = rests(req).repairHandleCount()

print("deviceList:",deviceList)