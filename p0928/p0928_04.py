from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup
import time
import os
from dotenv import load_dotenv
import undetected_chromedriver as uc

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81"

options = uc.ChromeOptions()

options.add_argument("--no-first-run")
options.add_argument("--no-service-autorun")
options.add_argument("--password-store=basic")

browser = uc.Chrome(options=options)

browser.get(url)

print(browser.title)

# 파일저장
soup = BeautifulSoup(browser.page_source,'lxml')
with open('p0928/file/coupang1.html','w',encoding='utf-8') as f:
    f.write(soup.prettify())
print('완료')  

input()
