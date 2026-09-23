from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
import time
import os

# 2. selenium : 자동화 도구
# browser = webdriver.Chrome()
# url = "https://stock.naver.com/market/stock/kr/stocklist/priceTop"
# # 브라우저 열기
# browser.get(url)
# time.sleep(4)
# 파일저장
# soup = BeautifulSoup(browser.page_source,'lxml')
# with open('stock1.html','w',encoding='utf-8') as f:
#     f.write(soup.prettify())

# 파일 BeautifulSoup변환
with open('stock1.html','r',encoding='utf-8') as f:
    soup = BeautifulSoup(f,'lxml')     

#------------------------------------
# 상단제목추가
s_headTitle = []
s_tr = soup.thead.tr
ths = s_tr.find_all('th') #8개 정보
for th in ths:
    s_headTitle.append(th.get_text(strip=True))
    # print(th.get_text(strip=True))
print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*s_headTitle))
print("-"*85)

s_tbody = soup.tbody
# trs = s_tbody.find('tr')      # 1개 sk하이닉스 find,find_all
trs = s_tbody.find_all('tr')  # 100개 정보
for tr in trs:
    tds = tr.find_all('td')      # td 8개
    s_idx = tds[0].find('span',{'class':'index'}).get_text(strip=True)
    s_title = tds[0].find('span',{'class':'SingleLineText_text__HI_cb'})
    s_title = s_title.get_text(strip=True)
    s_price = tds[1].find('span',{'class':'SingleLinePrice_price__g_6VV'})
    s_price = s_price.get_text(strip=True)
    s_compare = tds[2].find('span',{'class':'ModulePriceChange_amount__4QYMz'})
    s_compare = s_compare.get_text(strip=True)
    s_trade = tds[3].find('span',{'class':'SingleLinePrice_price__g_6VV'})
    s_trade = s_trade.get_text(strip=True)
    s_trade_val = tds[4].find('span',{'class':'SingleLinePrice_price__g_6VV'})
    s_trade_val = s_trade_val.get_text(strip=True)
    s_costliness = tds[5].find('span',{'class':'SingleLinePrice_price__g_6VV'})
    s_costliness = s_costliness.get_text(strip=True)
    s_lowprice = tds[6].find('span',{'class':'SingleLinePrice_price__g_6VV'})
    s_lowprice = s_lowprice.get_text(strip=True)
    s_cap = tds[7].find('span',{'class':'SingleLineText_text__HI_cb'})
    s_cap = s_cap.get_text(strip=True)
    print(f"{s_idx}.{s_title}\t{s_price}\t{s_compare}\t{s_trade}\t{s_trade_val}\t{s_costliness}\t{s_lowprice}\t{s_cap}")
    print("-"*85)




# 1. requests
# 단점 : 자바스크립트로 구동되는 소스 가져올수 없다.
# requests정보가져오기 -> css문법변환 -> find,find_all()
# url = "https://www.melon.com/chart/index.htm"
# # User-Agent : Python-requests 정보
# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36'}
# res = requests.get(url,headers=headers)
# res.raise_for_status() #에러시 종료
# # css문법변환
# soup = BeautifulSoup(res.text,'lxml') #html소스 변경-css문법
