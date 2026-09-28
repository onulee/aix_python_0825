from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup
import time
import os
from dotenv import load_dotenv


# 1. requests 파일 가져오기
sum = 0
for i in range(1,6):
    page = i
    url = f"https://search.danawa.com/dsearch.php?query=%EB%85%B8%ED%8A%B8%EB%B6%81&originalQuery=%EB%85%B8%ED%8A%B8%EB%B6%81&checkedInfo=N&volumeType=allvs&page={page}&limit=40&sort=saveDESC&list=list&boost=true&tab=goods&addDelivery=N&simpleDescOpen=Y&mode=simple&isInitTireSmartFinder=N&recommendedSort=N&defaultUICategoryCode=112758&defaultPhysicsCategoryCode=860%7C869%7C10580%7C0&defaultVmTab=104290&defaultVaTab=8809942&isZeroPrice=Y&quickProductYN=N&priceUnitSort=N&priceUnitSortOrder=A"
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36'}
    res = requests.get(url,headers=headers)
    res.raise_for_status() #에러시 종료
    soup = BeautifulSoup(res.text,'lxml') #html소스 변경-css문법
    p_ul = soup.find('ul',{'class':'product_list'})
    lis = p_ul.find_all('li')
    for li in lis:
        try:
            prod_name = li.find('p',{'class':'prod_name'}).get_text(strip=True)
            prod_link = li.find('a',{'class':'click_log_product_standard_price_'})['href']
            prod_price = li.find('a',{'class':'click_log_product_standard_price_'}).get_text(strip=True)[:-1]
            prod_price_int = int(prod_price.replace(',',''))
            if prod_price_int<1500000:
                print(f"{prod_name} : {prod_price} ",prod_price_int)
                print("링크 : ",prod_link)
            else:
                print('150만원 이상 제외')
            print("-"*50)
            # print("개수 : ",len(lis))
        except:
            print('이름/가격없음')




# # 1. requests 파일 가져오기
# for i in range(1,2):
#     page = i
#     url = f"https://search.danawa.com/dsearch.php?query=%EB%85%B8%ED%8A%B8%EB%B6%81&originalQuery=%EB%85%B8%ED%8A%B8%EB%B6%81&checkedInfo=N&volumeType=allvs&page={page}&limit=40&sort=saveDESC&list=list&boost=true&tab=goods&addDelivery=N&simpleDescOpen=Y&mode=simple&isInitTireSmartFinder=N&recommendedSort=N&defaultUICategoryCode=112758&defaultPhysicsCategoryCode=860%7C869%7C10580%7C0&defaultVmTab=104290&defaultVaTab=8809942&isZeroPrice=Y&quickProductYN=N&priceUnitSort=N&priceUnitSortOrder=A"
#     headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36'}
#     res = requests.get(url,headers=headers)
#     res.raise_for_status() #에러시 종료
#     soup = BeautifulSoup(res.text,'lxml') #html소스 변경-css문법
#     print("-"*50)
#     ul = soup.find('ul',{'class':'product_list'})
#     lis = ul.find_all('li',{'class':'prod_item'})
#     for li in lis:
#         try:
#             print(li.find('p',{'class':'prod_name'}).get_text(strip=True))
#             price_li = li.find('li',{'class':'rank_one'})
#             price_li_str = price_li.a.get_text(strip=True)[:-1]
#             price_li_int = int(price_li_str.replace(',',''))
#             print(price_li.a.get_text(strip=True))
#             print(price_li_int)
#         except:
#             print('이름 / 값 없음')    
#         print("-"*10)
#     print(i,":",len(lis))




# 2. selenium : 자동화 도구 - 스크롤없이 가져옴
# url = "https://nol.yanolja.com/discovery/list/PRODUCT_CATEGORY_KOREA_ACCOMMODATION/HOTEL/900584"
# options = Options()
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option("useAutomationExtension", False)
# options.add_argument("--disable-blink-features=AutomationControlled")
# browser = webdriver.Chrome(options=options)
# browser.maximize_window() # 화면 최대창 확대
# browser.get(url)
# time.sleep(2)
# # 파일저장
# soup = BeautifulSoup(browser.page_source,'lxml')
# with open('p0928/file/ya1.html','w',encoding='utf-8') as f:
#     f.write(soup.prettify())
