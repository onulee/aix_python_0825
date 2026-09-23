from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup
import time
import os
from dotenv import load_dotenv

# # 2. selenium : 자동화 구현
# # 상단 제어창문구 삭제
# options = Options()
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option("useAutomationExtension", False)
# options.add_argument("--disable-blink-features=AutomationControlled")
# browser = webdriver.Chrome(options=options)
# browser.maximize_window() # 화면 최대창 확대
# url = "https://www.yeogi.com/domestic-accommodations?keyword=%EA%B2%BD%EC%A3%BC&autoKeyword=%EA%B2%BD%EB%B6%81+%EA%B2%BD%EC%A3%BC%EC%8B%9C&checkIn=2026-09-23&checkOut=2026-09-24&personal=2"
# browser.get(url)
# time.sleep(2)
# # 자바스크립트를 통해 브라우저 높이 가져오기
# pre_height = browser.execute_script('return document.body.scrollHeight')
# print("처음 높이 : ",pre_height)
# while True:
#     # 스크롤 내리기
#     browser.execute_script('window.scroll(0,document.body.scrollHeight)')
#     time.sleep(3) # 내용추가하는데 시간대기

#     # 다시 높이 가져오기
#     next_height = browser.execute_script('return document.body.scrollHeight')
#     print('변경된 높이 : ',next_height)

#     if pre_height==next_height: break
#     else : pre_height = next_height

# print('더 이상 높이 변경이 없음')
# time.sleep(1)

# 파일저장해서 저장한 파일을 가지고 정보를 가져오기
# 이미지, 숙소명, 별점, 리뷰수, 금액
# # 파일저장
# soup = BeautifulSoup(browser.page_source,'lxml')
# with open('yeogi1.html','w',encoding='utf-8') as f:
#     f.write(soup.prettify())
# input()


# 파일 BeautifulSoup변환
with open('yeogi1.html','r',encoding='utf-8') as f:
    soup = BeautifulSoup(f,'lxml')  
# 정보가져오기    
s_ul = soup.find('ul',{'class':'css-y5z6rw'})
lis = s_ul.find_all('li')
for idx,li in enumerate(lis):
    print(f"{idx+1}.")
    try:
        # 1. 이미지링크
        s_img = li.find('img')['src']
        print("이미지 : ",s_img)
        # 2. 숙소명
        s_title = li.find('h3',{'class':'gc-thumbnail-type-seller-card-title css-1gsfgy5'}).get_text(strip=True)
        print("숙소명 : ",s_title)
        # 3. 별점
        s_star = li.find('span',{'class':'css-ry30z7'}).get_text(strip=True)
        s_star = float(s_star)
        print("평점 : ",s_star)
        # 4. 평가수
        s_view = li.find('span',{'class':'css-144z61f'}).get_text(strip=True)
        s_view = int(s_view[:-4].replace(',',''))
        print("평가수 : ",s_view)
        s_price = li.find('span',{'class':'css-1llao6q'}).get_text(strip=True)
        s_price = int(s_price.replace(',',''))
        print("금액 : ",s_price)
        print("-"*60)
    except Exception as e:
        print(e)


