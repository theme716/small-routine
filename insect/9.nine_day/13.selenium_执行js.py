from selenium import webdriver
import time

browser= webdriver.Chrome(executable_path=r'E:\software\browser\chromedriver_win32\chromedriver.exe')

base_url = 'http://www.baidu.com/s?wd=世界杯'
browser.get(base_url)
time.sleep(2)

# 执行js
browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')



