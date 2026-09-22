import requests

url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent/"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status() # 에러나면 프로그램 종료


with open('melon2.html','w',encoding='utf-8') as f:
    f.write(res.text)

print("저장완료")