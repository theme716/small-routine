from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from lxml import etree
import requests

browser= webdriver.Chrome(executable_path=r'E:\software\browser\chromedriver_win32\chromedriver.exe')
wait = WebDriverWait(browser,20)
browser.get('http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=美女')

while True:

    print('==============')
    # 提取图片链接，并保存图片
    html = browser.page_source
    html = etree.HTML(html)
    img_content = html.xpath('//div[@id="imgid"]/div[last()]//li/@data-objurl')
    for img in img_content:
        try:
            img_name = img[img.rfind('/'):]
            response = requests.get(img)
            img_text = response.content
            with open('./baidupic'+img_name,'wb') as f:
                f.write(img_text)
            print(img_name)
        except Exception as e:
            print(e)
            print(img,'失败')

    # 翻页
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(4)


