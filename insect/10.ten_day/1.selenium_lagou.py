from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup

browser= webdriver.Chrome(executable_path=r'E:\software\browser\chromedriver_win32\chromedriver.exe')
wait = WebDriverWait(browser,20)
browser.get('https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=')

f = open('lagou.csv',mode='w',encoding='utf-8')

while True:
    # 获取页面
    html = browser.page_source
    # 提取数据
    html = BeautifulSoup(html,'lxml')
    li_list = html.select('.item_con_list li')

    for li in li_list:
        p_name = li.select('h3')[0].text #职位名称
        p_time = li.select('.format-time')[0].text #发布时间
        p_company = li['data-company'] #公司
        p_money = li.select('.money')[0].text #薪资
        p_exp = li.select('.p_bot .li_b_l')[0].text.split('k')[-1].strip() #经验和学历
        p_xueli = p_exp.split('/')[-1].strip() # 学历要求
        p_exp = p_exp.split('/')[0]

        p_location = li.select('.add')[0].text #工作地点
        p_tags = li.select('.list_item_bot span') #工作性质（后端开发、服务器端）
        p_tags = ','.join([tag.text for tag in p_tags])

        p_data = li.select('.li_b_r')[0].text #工作情况
        p_hangye = li.select('.industry')[0].text.strip() #行业
        data = [p_name,p_time,p_company,p_money,p_exp,p_xueli,p_location,p_tags,p_data,p_hangye]
        f.write(','.join(data)+'\n')
        print(p_name)
    if 'pager_next_disabled' not in html:
        wait.until(expected_conditions.element_to_be_clickable((By.CLASS_NAME,'pager_next')))
        browser.find_element_by_class_name('pager_next').click()
        time.sleep(2)
    else:
        browser.close()
        break

f.close()