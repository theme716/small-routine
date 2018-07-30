from selenium import webdriver
import time

# 生成浏览器对象
browser= webdriver.Chrome(executable_path=r'E:\software\browser\chromedriver_win32\chromedriver.exe')


# 发起请求
browser.get('http://www.taobao.com')
time.sleep(1)
browser.find_element_by_id('q').send_keys('猫')
browser.find_element_by_class_name('btn-search').click()
time.sleep(4)

browser.save_screenshot('猫.png')
print(browser.page_source)

'''
注意：
    1.浏览器内核地址前面必须写r,以url防止被转义
    2.保存图片时候，起名为xxx.png
    3.browser.page_source 不能写为 browser.page_source  
'''