# 문자열함수
# split, strip, replace, find, rfind
# upper-영문자 모두 대문자로 출력,lower-소문자로 출력


paper = """\
네팔 대홍수 참사 수습이 언제 끝날지도 모르는 상황에서 
2차 홍수가 덮칠 수 있다는 관측이 나오고 있습니다. 
이번 홍수의 원인으로 지목된 것처럼 산 위의 빙하가 붕괴되면서 
비 한 방울 없이 홍수가 또 일어날 수 있다는 겁니다.\
"""
print(paper)
print(len(paper))

str1 = "1,홍길동,100,100,100,300,100" #문자열타입
s = str1.split(",")  # split 특정문자를 기준으로 분리를 해줌.
print(s)
print(s[2])
str2 = "2026-08-28"
s2 = str2.split("-")
print(s2)
print(s2[2])
str3 = "안녕 반가워 다음에 봐"
s3 = str3.split(" ")
print(s3)
print(s3[1])

str4 = "EDMS,307-2E-PS-W-611-W008,VF5770"
s4 = str4.split(",")
print(s4)
print(s4[2])

# strip - 공백제거
aaa1 = "       안녕하세요      "
print(aaa1)
print(aaa1.strip())

aaa2 = "   안녕   하세요   "
print(aaa2.strip())

# replace - 문자를 다른문자로 대체
aaa3 = "aabbccddaaeea"
aaa4 = aaa3.replace("a","k")
print(aaa4)

aaa2 = "   안녕   하세요   "
aaa5 = aaa2.replace(" ","")
print(aaa5)


# find : 검색함수 왼쪽부터 검색시작, 있으면 위치를 반환, 없으면 -1
bb = "abcdefghicba"
print(bb.find("k")) 
# rfind : 오른쪽에서 부터 검색 시작
print(bb.rfind("c"))

cc = "aabbccddee"
print(cc.upper())

dd = "AaBbCCddEE"
print(dd.lower())

