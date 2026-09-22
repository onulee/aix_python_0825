import requests   #웹접근
from bs4 import BeautifulSoup  # html로 파싱
# url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent/"
# url = "https://www.melon.com/chart/index.htm"
url = "http://www.naver.com"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36'}
res = requests.get(url,headers=headers)
res.raise_for_status() #에러시 종료
# print(res.status_code) #상태코드

print(res.text)

with open("naver1.html",'w',encoding='utf-8') as f:
    f.write(res.text)

print("저장완료")
# f = open('stu.txt','w',encoding='utf-8')
# f.close()

