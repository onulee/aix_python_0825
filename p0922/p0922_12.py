from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
import time
import os

# 2.selenium 파일저장
# browser = webdriver.Chrome()
# url = "https://stock.naver.com/market/stock/kr/stocklist/priceTop"
# browser.get(url)
# time.sleep(3)
# soup = BeautifulSoup(browser.page_source,'lxml')
# with open('stock1.html','w',encoding='utf-8') as f:
#     f.write(soup.prettify())


# 파일 BeautifulSoup변환
with open('stock1.html','r',encoding='utf-8') as f:
    soup = BeautifulSoup(f,'lxml')    

s_tbody = soup.find("tbody",{'class':'Table_tbody__EJrOg'})
trs = s_tbody.find_all('tr')
tds = trs[0].find_all('td')
print(tds[0].find('span',{'class':'SingleLineText_text__HI_cb'}).get_text(strip=True))