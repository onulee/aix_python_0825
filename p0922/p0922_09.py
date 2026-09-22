import requests
from bs4 import BeautifulSoup
import os

url = "https://www.melon.com/chart/index.htm"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36'}
res = requests.get(url,headers=headers)
res.raise_for_status() #에러시 종료

soup = BeautifulSoup(res.text,'lxml') #html소스 변경-css문법

#파일저장
# with open('melon1.html','w',encoding='utf-8') as f:
#     f.write(res.text)

# with open('melon2.html','w',encoding='utf-8') as f:
#     f.write(soup.prettify())  
# 
print("-"*50)
# 1개 find, 여러개 find_all
s_tbody = soup.tbody
trs = s_tbody.find_all("tr")  #타입:list
for idx,tr in enumerate(trs):
    tds = tr.find_all("td")
    try:
        print("순위 : ",tds[1].find("span",{"class":"rank"}).get_text()+"위")
        img = tds[3].find("img")['src']
        print("링크 :",img)  #[],attrs

        #------------------------
        # img정보를 가지고 호출을 다시해야 함. - img의 정보파일을 가져옴.
        os.makedirs("./melon_img",exist_ok=True) #exist_ok:폴더가 존재하면 무시
        img_res = requests.get(img,headers=headers)
        with open(f"melon_img/melon_2026_{idx+1}.jpg","wb") as f:
            f.write(img_res.content)
        #------------------------
        s_as = tds[5].find_all("a")
        print("제목명: ",s_as[0].get_text())  #노래제목
        print("가수명 :",s_as[1].get_text())  #가수명
        print("앨범명 :",tds[6].find("a").get_text())  #앨범명
        print("-"*30)
    except Exception as e:
        print(e)   

print("완료!!")     
