import requests

res = requests.get("https://www.google.com/")
res.raise_for_status() #에러코드시 프로그램 종료
print(res.text) # html모든 소스를 가져오기
print(len(res.text))

# 파일저장
with open('google1.html','w',encoding="utf-8") as f:
    f.write(res.text)  #html

print("파일저장 완료")    


# res.status_code : 코드 확인
# res = requests.get("https://www.melon.com/")
# res.raise_for_status() # 에러가 나면 프로그램을 자동종료시킴
# # print(res.text) # 모든데이터 읽어오기
# print("응답 코드 : ",res.status_code)
# print("프로그램을 종료합니다.")
# # print("html소스 : ",res.text)

# if res.status_code != 200:
#     pass