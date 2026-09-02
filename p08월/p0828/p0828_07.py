a = [1,2,3,4,5]
print(a)
print(*a)
print(a[0],a[1],a[2],a[3],a[4])


# # # split() 구분자로 분리
# # str1 = "1,홍길동,100,100,99"
# # s = str1.split(",")
# # print(s)    # 리스트-문자열
# # print(s[4]) # 타입:문자열

# # 번호,이름,국어,영어,수학,합계,평균을 출력하시오.
# str1 = "1,홍길동,100,100,99"
# s = str1.split(",") #['1','홍길동','100','100','99'] - 문자열
# s[2] = int(s[2]) # 국어
# s[3] = int(s[3])
# s[4] = int(s[4])
# s.append(s[2]+s[3]+s[4]) # 합계추가
# s.append(s[5]/3)         # 평균추가

# print("[학생성적프로그램]")
# print("번호\t이름\t국어\t영어\t수학\t합계\t평균")
# print("-"*60)  #문자*반복

# # *s : 구조분해할당 (s[0],s[1],s[2],s[3],s[4],s[5],s[6])
# print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}".format(s[0],s[1],s[2],s[3],s[4],s[5],s[6]))
# print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}".format(*s))
# print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]:.2f}")




# in 함수
# paper = "네팔 대홍수 참사 수습이 언제 끝날지도 모르는 상황에서\
#       2차 홍수가 덮칠 수 있다는 관측이 나오고 있습니다.\
#       이번 홍수의 원인으로 지목된 것처럼 산 위의 빙하가 붕괴되면서\
#           비 한 방울 없이 홍수가 또 일어날 수 있다는 겁니다."

# if "코치" in paper:
#     print("있음")
# else:
#     print("없음") 


# alist = ["딸기","포도","바나나"]
# if "포도" in alist:
#     print("있음")
# else:
#     print("없음")           


# paper = "네팔 대홍수 참사 수습이 언제 끝날지도 모르는 상황에서\
#       2차 홍수가 덮칠 수 있다는 관측이 나오고 있습니다.\
#       이번 홍수의 원인으로 지목된 것처럼 산 위의 빙하가 붕괴되면서\
#           비 한 방울 없이 홍수가 또 일어날 수 있다는 겁니다."

# result1 = paper.find("홍수")
# print(result1)   # 4

# # find(검색내용,시작위치,종료위치)
# result2 = paper.find("홍수",5)
# print(result2)



# result1 = paper.find("홍수")
# print(result1)

# result2 = paper.rfind("홍수")
# print(result2)

# result3 = paper.count("홍수")
# print(result3)

#### 홍수 라는 글자가 어디어디에 있는지 위치점을 알고 싶어요.



# print("[ 로그인페이지 ]")
# while(True):
#     id = input("아이디 : ")
#     pw = input("패스워드 : ")
#     if id=="aaa" and pw=="1111":
#         print("로그인성공! 메인페이지로 이동합니다.")
#         break
#     else:
#         print("아이디 또는 패스워드가 일치하지 않습니다. 다시 로그인해주세요.")

# print("메인페이지가 열립니다.")







# name=input("이름입력 : ")
# while(True):
#     kor = input("국어점수 입력 : ")
#     if kor.isdigit():
#         kor = int(kor)
#         break
#     else:
#         print("숫자가 아닙니다. 다시 입력해주세요.") 

# print(name,kor)




# 문자인지 아닌지 확인
# 이름을 입력을 받는데 영문이름
# name = input("이름을 입력하세요.")
# if name.isalpha():  # 특수문자나 숫자인지 확인가능
#     print("문자 알파벳으로 되어 있습니다.")
# else:
#     print("특수문자나 숫자가 입력되었습니다.")        
# print(name)

#-----------------------

# num = input("숫자를 입력하세요.>>> ")
# if num.isdigit():
#     num = int(num)
#     num += 100
#     print("입력숫자 : ",num)
# else:
#     print(num)    


# # format함수
# a = 10
# print("{}".format(a))
# print("{:10d}".format(a))
# print("{:+010d}".format(a))      # + : 숫자앞에 부호를 붙여줌
# print("{:+010d}".format(-10))
# print("{:3,d}".format(123456789))  # 천단위 표시
# print("{:012.2f}".format(12.12345))  # 소수점제한


