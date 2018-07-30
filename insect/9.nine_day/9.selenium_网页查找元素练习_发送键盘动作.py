from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

browser= webdriver.Chrome(executable_path=r'E:\software\browser\chromedriver_win32\chromedriver.exe')

# 发起请求
browser.get('http://www.taobao.com')
time.sleep(2)

# 1.通过id查找
# res = browser.find_element_by_id('q') #<selenium.webdriver.remote.webelement.WebElement (session="33a395cdce8d9a8bfea710ea53736ec8", element="0.9605032685056796-1")>

# 2.通过类名查找（如果有多个类，传入一个就可以了）
# res = browser.find_element_by_class_name('search-combobox-input-wrap')

# 3.通过标签名查找
# res = browser.find_element_by_tag_name('title')

# 4.通过xpath规则查找
# res = browser.find_element_by_xpath('//*[@id="q"]')

# 5.通过css查找
# res = browser.find_element_by_css_selector('.service-bd li').text

# 6.强大而通用的查找方式（需要借助from selenium.webdriver.common.by import By）
# res = browser.find_element(By.XPATH,value='//*[@id="q"]')

# 7.查找多个元素 (返回一个对象列表)
# res = browser.find_elements_by_class_name('J_Cat')
# res = browser.find_elements(By.XPATH,value='//li')

# print(res)

# 发送键盘动作：（需要借助from selenium.webdriver.common.keys import Keys）
browser.find_element(By.XPATH,value='//*[@id="q"]').send_keys('世界杯')
browser.find_element(By.XPATH,value='//*[@id="q"]').send_keys(Keys.ENTER)