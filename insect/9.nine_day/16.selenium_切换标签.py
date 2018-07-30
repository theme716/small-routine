from selenium import webdriver
import time

base_url = 'http://www.baidu.com'
browser= webdriver.Chrome(executable_path=r'E:\software\browser\chromedriver_win32\chromedriver.exe')

browser.get(base_url)
time.sleep(1)

browser.execute_script('window.open()') #新建标签页

# 切换标签
browser.switch_to.window(browser.window_handles[1]) #0是一开始打开的标签
browser.get('http://www.jd.com')
time.sleep(2)
browser.switch_to.window(browser.window_handles[0])
browser.get('http://www.taobao.com')
browser.switch_to.window(browser.window_handles[1])
browser.execute_script('window.close()')