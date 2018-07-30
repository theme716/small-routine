from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


base_url = 'http://www.taobao.com'
browser= webdriver.Chrome(executable_path=r'E:\software\browser\chromedriver_win32\chromedriver.exe')

browser.get(base_url)
wait= WebDriverWait(browser,20) #等待加载的过期时间

# 直到id为q的元素加载完成
wait.until(expected_conditions.presence_of_all_elements_located((By.ID,'q')))
browser.find_element_by_id('q').send_keys('世界杯')

# 直到元素可以被点击，则点击
wait.until(expected_conditions.element_to_be_clickable((By.CLASS_NAME,'btn-search')))
browser.find_element_by_class_name('btn-search').click()
