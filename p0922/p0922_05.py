import requests
from bs4 import BeautifulSoup

# url = "https://n.news.naver.com/article/094/0000013820?cds=news_media_pc&type=editn"
url = "https://www.melon.com/chart/index.htm"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36'}
res = requests.get(url,headers=headers)
res.raise_for_status() #에러시 종료
# 파일을 전체저장 res.text
# 필요한 부분만 저장 - 파싱후 원하는 부분 저장

soup = BeautifulSoup(res.text,'lxml') #html소스 변경-css문법
print("-"*50)
# print(soup.prettify())
# 태그로 찾는 방법, 속성1개, 속성모두 찾는방법
# print(soup.title) #태그가져오기
# print(soup.title.get_text()) # 태그글자가져오기
# print(soup.a['href']) # 속성 1개
# print(soup.div.attrs) # 속성값 모두 가져오기
# print(soup.tbody)

# id,class 찾는 방법
# print(soup.find("div",{"id":"header"}))
# print(soup.find("div",{"id":"util_menu"}))
# print(soup.find("tr",{"class":"lst50"}))
# print(soup.find("div",{"class":"wrap t_right"}))
print(soup.find("input",{"class":"input_check d_checkall"})['title'])


# print(soup.prettify()) # 코드가 정렬이 되어 저장이 됨.
# print(res.text)
# print("a 태그 : ",soup.a)
# print("a 태그 : ",soup.a['href'])
# print("a 태그 : ",soup.a.attrs) #a태그의 모든 속성값을 가져옴.
# print("title 제목 :",soup.title)  #태그 title
# print("title 제목 :",soup.title.get_text())  #태그 title


