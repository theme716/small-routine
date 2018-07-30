from selenium import webdriver
import time

# 返回浏览器对象
browser = webdriver.PhantomJS(executable_path=r'E:\software\browser\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe')

#发起请求
browser.get('http://www.baidu.com')
time.sleep(0.5)  #等浏览器加载出来之后再执行网页操作

browser.find_element_by_id('kw').send_keys('世界杯')
browser.find_element_by_class_name('s_btn').click()

time.sleep(1) #等网页加载出来
browser.save_screenshot('baidu.png')  #保存网页截图

print(browser.page_source) #获取当前页面源码
browser.close() #关闭浏览器