from selenium import webdriver
import time,json

start = int(input('请输入起始页：'))
end = int(input('请输入结束页：'))

base_url = 'https://www.douyu.com/directory/all'
browser= webdriver.Chrome(executable_path=r'E:\software\browser\chromedriver_win32\chromedriver.exe')
f = open('douyu.json','w',encoding='utf-8')
browser.get(base_url)
browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
time.sleep(4)
print('=========================1===========================')
def analysi():
    # 找到所有的li
    li_list = browser.find_elements_by_css_selector('#live-list-contentbox li')
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
        f.write(json.dumps(item,ensure_ascii=False)+',\n')

analysi()
# 找到下一页并解析
for i in range(start+1,end+1):
    print('====================='+str(i)+'===========================')
    browser.find_element_by_class_name('shark-pager-next').click()
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(4)
    analysi()
