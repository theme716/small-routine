from selenium import webdriver
import time

browser= webdriver.Chrome(executable_path=r'E:\software\browser\chromedriver_win32\chromedriver.exe')

# 发起请求
browser.get('http://www.taobao.com')
time.sleep(3)

tag = browser.find_elements_by_css_selector('.nav-bd li a')

for a in tag:
    print(a.text)
    print(a.size)
    print(a.location)
    print(a.get_attribute('href'))