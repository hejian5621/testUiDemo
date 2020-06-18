from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait

url = 'http://www.maiziedu.com/'
login_text = '登陆'
account = 'maizi_test@139.com'
pwd = 'abc123456'


def get_ele_times(driver,time,func):
    return WebDriverWait(driver, time).until(func)


def openBrower():
    webdriver_handle = webdriver.Chrome()     # 打开浏览器
    return webdriver_handle


def openUrl(handle,url):
    handle.get(url)                # 获取URL
    handle.maximize_window()       # 最大化浏览器


def findElement(driver,arg):
    if 'text_id' in arg:            # 如果arg 字典里有text_id就执行下面的脚本
        #ele_login = get_ele_times(driver, 10, lambda driver: driver.find_element_by_link_text(arg['text_id']))
        ele_login = driver.find_element_by_css_selector(".a.globalLoginBtn")
        ele_login.click()
        useEle = driver.find_element_by_id(arg['userid'])
        pwdELe = driver.find_element_by_id(arg['pwdid'])
        loginEle = driver.find_element_by_id(arg['loginid'])
        return useEle, pwdELe, loginEle




def sendvals(eletuple,arg):
    listkey = ['uname','pwd']
    i = 0
    for key in listkey:
        eletuple[i].send_keys('')
        eletuple[i].send_keys(arg[key])
        i+=1
    eletuple(2).click()


def checkResuit(d,text):
    try:
        d.find_element_by_link_text('test')
        print("Account And Pwd Error")

    except:
        print("Account And Pwd Ringht!")


def login_test():                               #入口
    driver = openBrower()
    openUrl(driver,url)
    ele_dict = {'text_id': login_text, 'userid': 'id_account_l', 'pwdid': 'id_password_l', 'loginid': 'login_btn'}
    print(ele_dict['text_id'])
    account_dict = {'uname': account,'pwd': pwd}
    ele_tuple = findElement(driver, ele_dict)
    sendvals(ele_tuple,account_dict)
    checkResuit(driver,'该账号不正确')


if __name__ == '__main__':
    login_test()
