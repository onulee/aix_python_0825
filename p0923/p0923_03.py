from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup
import time
import os
from dotenv import load_dotenv

# 2. selenium : 자동화 구현
# 상단 제어창문구 삭제
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
options.add_argument("--disable-blink-features=AutomationControlled")
browser = webdriver.Chrome(options=options)
browser.maximize_window() # 화면 최대창 확대
url = "https://www.naver.com/"

# 검색부분 - 날씨 입력 > enter : 온도, 날씨를 출력하시오.
browser.get(url)
# 검색클릭 > 날씨입력 > enter키
elem = browser.find_element(By.ID,'query')
elem.click()
elem.send_keys('날씨')
elem.send_keys(Keys.ENTER)
# 온도 가져오기
time.sleep(3)
soup = BeautifulSoup(browser.page_source,'lxml')
temp = soup.find('div',{'class':'temperature_text'}).get_text(strip=True)
print(temp)

input()


# # 브라우저 열기
# browser.get(url)
# browser.find_element(By.CLASS_NAME,'MyView-module__link_login___VlF7z').click()
# time.sleep(3)
# elem = browser.find_element(By.ID,'id')
# elem.send_keys('aaa')
# elem2 = browser.find_element(By.ID,'pw')
# elem2.send_keys('1111')
# input()



# # .env파일 읽기
# load_dotenv()
# print(os.getenv('naver_id'))