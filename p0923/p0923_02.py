from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
import time
import os

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36'}
# # 2. selenium : 자동화 도구
# browser = webdriver.Chrome()
# url = "https://comic.naver.com/bestChallenge?sortType=starscore"
# # 브라우저 열기
# browser.get(url)
# time.sleep(4)

# # 파일저장
# soup = BeautifulSoup(browser.page_source,'lxml')
# with open('webtoon1.html','w',encoding='utf-8') as f:
#     f.write(soup.prettify())

# 파일 BeautifulSoup변환
with open('webtoon1.html','r',encoding='utf-8') as f:
    soup = BeautifulSoup(f,'lxml')  

s_ul = soup.find('ul',{'class':'BestChallengeView__challenge_list--sUqhh'})
lis = s_ul.find_all('li')
view_total = 0
view_avg = 0
for i in range(3):
    s_contitle = lis[i].find('span',{'class':'ContentTitle__title--e3qXt'})
    s_title = s_contitle.find('span',{'class':'text'}).get_text(strip=True)
    print(s_title)
    s_author = lis[i].find('a',{'class':'ContentAuthor__author--CTAAP'}).get_text(strip=True)
    print(s_author)
    s_constar = lis[i].find('span',{'class':'Rating__star_area--dFzsb'})
    s_star = float(s_constar.find('span',{'class':'text'}).get_text(strip=True))
    print(s_star)
    s_conview = lis[i].find('span',{'class':'Rating__view_area--GQb_S'})
    s_view = int(s_conview.find('span',{'class':'text'}).get_text(strip=True)[:-1].replace(",",""))
    view_total += s_view
    print(s_view)

    # 이미지
    s_img = lis[i].find('img')['src']
    print(s_img)
    # 이미지 저장
    img_res = requests.get(s_img,headers=headers)
    os.makedirs('./p0923/webtoon',exist_ok=True) # 폴더생성
    with open(f'p0923/webtoon/w_{i}.jpg','wb') as f:
        f.write(img_res.content)
    print("-"*50)

view_avg = view_total/3
print(f"평균 조회수 : {view_avg:.2f}만")
print('완료')


# a = float("9.92")
# b = float("8.0")
# c = float("9.1")
# print((a+b+c)/3)

# aa = int("1,023".replace(",",""))
# bb = int("2,120".replace(",",""))
# cc = int("3,023".replace(",",""))
# print((aa+bb+cc)/3)

# a = '1,123만원'
# print(a[:-1])
# print(a[:-2])
# print(a[-2:])
# print(a[-1])
# a_int = int(a[:-2].replace(",",""))
# print(a_int)
