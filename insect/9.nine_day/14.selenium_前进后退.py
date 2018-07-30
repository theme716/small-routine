from selenium import webdriver
import time

browser= webdriver.Chrome(executable_path=r'E:\software\browser\chromedriver_win32\chromedriver.exe')

browser.get('http://www.baidu.com')
time.sleep(1)
browser.get('http://www.taobao.com')
time.sleep(1)
browser.get('http://www.python.org')
time.sleep(2)

browser.back()
time.sleep(1)

browser.back()
time.sleep(1)

browser.forward()
time.sleep(1)
