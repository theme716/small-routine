from selenium import webdriver
import time

base_url = 'http://www.baidu.com'
browser= webdriver.Chrome(executable_path=r'E:\software\browser\chromedriver_win32\chromedriver.exe')

browser.get(base_url)

cookies = browser.get_cookies() #获取全部cookie
for i in cookies:
    print(i)

print('设置cookie')
# 手动添加cookie
browser.add_cookie({'name':'name','value':'ckttty','domain':'.baidu.com'})#这几个是必须的元素
cookies = browser.get_cookies()
for i in cookies:
    print(i)


print('删除某条cookie')
browser.delete_cookie('H_PS_PSSID')
for i in browser.get_cookies():
    print(i)


print('删除所有cookies')
browser.delete_all_cookies()
print(browser.get_cookies())


