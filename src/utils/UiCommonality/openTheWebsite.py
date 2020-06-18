#操作浏览器
from selenium import webdriver
import time



class operation_Browser:
    """操作浏览器"""


    def __init__(self,url):
        self.url = url
        self.driver = None


    def openBrowser_URL(self):
        """打开浏览器并输入URL，返回浏览器对象"""
        self.driver = webdriver.Chrome()     #打开谷歌浏览器
        self.driver.maximize_window()    #最大化火狐浏览器方法
        self.driver.get(self.url)
        return self.driver


