from selenium import webdriver
from selenium.webdriver import ActionChains #引入动作链
from selenium.webdriver.common.keys import Keys
import time


browser= webdriver.Chrome(executable_path=r'E:\software\browser\chromedriver_win32\chromedriver.exe')

# 发起请求
browser.get('http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
time.sleep(1)

# 切换框架
browser.switch_to.frame('iframeResult')

drap = browser.find_element_by_css_selector('#draggable') #要操作的元素1
drop = browser.find_element_by_css_selector('#droppable') #要操作的元素2

# 实例化一个动作链对象(参数要实行动作的窗口对象（要在哪个网页时执行动作）)
action = ActionChains(browser)

# 要执行的动作
action.drag_and_drop(drap,drop)

# 执行动作
action.perform()
time.sleep(1)
browser.switch_to.alert()

