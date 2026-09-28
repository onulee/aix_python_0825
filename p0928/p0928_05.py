from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup
import time
import os
from dotenv import load_dotenv


# 2. selenium : 자동화 도구 - 스크롤없이 가져옴
url = "https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/"
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
options.add_argument("--disable-blink-features=AutomationControlled")
browser = webdriver.Chrome(options=options)
browser.maximize_window() # 화면 최대창 확대
browser.get(url)
time.sleep(3)

load_dotenv()
naver_id = os.getenv('naver_id')
naver_pw = os.getenv('naver_pw')
# 아이디/패스워드 입력
# browser.find_element(By.XPATH,'//*[@id="id"]').click()
# browser.find_element(By.XPATH,'//*[@id="id"]').send_keys('onulee')
# browser.find_element(By.XPATH,'//*[@id="pw"]').click()
# browser.find_element(By.XPATH,'//*[@id="pw"]').send_keys('1111')

input_js = 'document.getElementById("id").value = "{id}";\
            document.getElementById("pw").value = "{pw}";\
            '.format(id=naver_id,pw=naver_pw)
browser.execute_script(input_js)
time.sleep(3)
browser.find_element(By.XPATH,'//*[@id="loginBtn_row"]').click()

input()