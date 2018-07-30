from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

browser= webdriver.Chrome(executable_path=r'E:\software\browser\chromedriver_win32\chromedriver.exe')

# 发起请求
browser.get('http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
time.sleep(2)

# 切换框架
browser.switch_to.frame('iframeResult')

# 查找框架中的元素
# res = browser.find_element_by_class_name('ui-droppable')

# 查找框架中不存在的元素
try:
    res = browser.find_element_by_class_name('logo')
    print(res)
except NoSuchElementException as e:
    print(e)
    # 切换到父级框架
    browser.switch_to.parent_frame()
    res = browser.find_element_by_class_name('logo')
    print(res)

