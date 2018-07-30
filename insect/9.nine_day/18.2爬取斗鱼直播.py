from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
import json

start = int(input('请输入起始页：'))
end = int(input('请输入结束页：'))

base_url = 'https://www.douyu.com/directory/all'
browser= webdriver.Chrome(executable_path=r'E:\software\browser\chromedriver_win32\chromedriver.exe')
browser.get(base_url)
wait = WebDriverWait(browser,20)

wait.until(expected_conditions.element_to_be_clickable((By.CLASS_NAME,'shark-pager-next')))
browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
print('=========================1===========================')
def analysi():
    # 找到所有的li
    li_list = browser.find_elements_by_css_selector('#live-list-contentbox li')
    list_var = []
    for li in li_list:
        per_name = li.find_element_by_css_selector('.dy-name').text
        per_href = li.find_element_by_css_selector('a').get_attribute('href')
        per_title = li.find_element_by_css_selector('a').get_attribute('title')
        per_tag = li.find_element_by_css_selector('.tag ').text
        per_num = li.find_element_by_css_selector('.dy-num').text
        per_img = li.find_element_by_css_selector('.imgbox img').get_attribute('src')
        item = {
            'per_name':per_name,
            'per_href':per_href,
            'per_title':per_title,
            'per_tag':per_tag,
            'per_num':per_num,
            'per_img':per_img
        }
        print(per_name)
        list_var.append(item)
    with open('douyu.json', 'a', encoding='utf-8') as f:
        for i in list_var:
            f.write(json.dumps(i,ensure_ascii=False)+',\n')

analysi()
# 找到下一页并解析
for i in range(start+1,end+1):
    print('====================='+str(i)+'===========================')
    browser.find_element_by_class_name('shark-pager-next').click()
    try:
        wait.until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, 'shark-pager-next')))
        browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        analysi()
    except StaleElementReferenceException as e:
        print(e)
        wait.until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, 'shark-pager-next')))
        browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        analysi()

