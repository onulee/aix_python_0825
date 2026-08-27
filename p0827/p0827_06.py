score = 65
# score 60점이상이면 합격,불합격
if score>=60: print("합격")
else: print("불합격") 

# if문 축약
reuslt = "합격" if score>=60 else "불합격"


# # 날짜함수를 사용하려면
# import datetime
# now = datetime.datetime.now()

# # 해당월에 따라 봄,여름,가을,겨울이라고 출력하시오.
# # 겨울 12,1,2 봄 3,4,5 여름 6,7,8 가을 9,10,11
# # 비교문을 사용해서 
# # 해당월 계절을 출력하시오.
# # now.month 

# month = now.month
# month = int(input("월을 입력하세요."))
# if month==12 or 1<=month<=2:
#     print("겨울입니다.")
# elif 8>=month>=6:
#     print("여름입니다.")    
# elif 5>=month>=3:
#     print("봄입니다.")
# else:
#     print("가을입니다.")  


# if 11>=month>=9:
#     print("가을입니다.")
# elif 8>=month>=6:
#     print("여름입니다.")    
# elif 5>=month>=3:
#     print("봄입니다.")
# else:
#     print("겨울입니다.")        


# # if : 조건문
# # if
# # if - else
# # if elif else
# # if elif elif else

# # if 조건문:
# #    들여쓰기 되어야 함.
# # else:
# #    들여쓰기 되어야 함.

# if 10>5:
#     pass   # 출력이나 기타 프로그램이 없을시 pass
#     # 빈공백이면 에러감.
# print("프로그램")    

# if 10>5: pass
# if 10>5: print("참")  # if 한줄가능
# if 10>5:
#     print("참")

# if 10>5:    # 명령어가 2줄이상이면 다음줄에 넣어야 함. 
#    print("참")
#    print("좋아요")    



# import random
# # 랜덤점수를 생성해서
# # 90점이상 A, 80점이상 B,70-C,60-D,F 출력하시오.
# # 90-92점 A-, 93-97 A, 98 A+
# # 80-82점 B-, 83-87 B, 88 B+
# # 70-72점 C-, 73-77 C, 78 C+
# # 랜덤점수 출력하시오. 

# num = random.randint(0,100)
# if num>=90:
#     if num>=99:
#         print("A+")
#     elif num>=93:
#         print("A")
#     else:
#         print("A-")        
# elif num>=80:
#     if num>=89:
#         print("B+")
#     elif num>=83:
#         print("B")
#     else:
#         print("B-")  
# elif num>=70:
#     if num>=79:
#         print("C+")
#     elif num>=73:
#         print("C")
#     else:
#         print("C-") 
# elif num>=60:
#     if num>69:
#         print("D+")
#     elif num>=63:
#         print("D")
#     else:
#         print("D-")
# else:
#     print("F")               
# print("해당점수 : ",num)




# import random
# 0-100점 랜덤숫자 생성
# 60점 이상 합격
# 50-59점까지 재시험 if score>=50: / if 59>=score>=50:
# 0-49점까지 불합격

# score = random.randint(0,100)
# if score>=60:
#     print("합격")
# # elif 59>=score>=50:     # elif score>=50:
# elif (59>=score) and (score<=50):    
#     print("재시험")
# else:
#     print("불합격")   

# print("랜덤점수 : ",score)         




# import random
# random_no = random.randint(-2,2)
# print("랜덤숫자 : ",random_no)

# # 양수,음수인지 출력하시오.
# # random_no>0
# if random_no>0:
#     print("양수")
# elif random_no == 0:
#     print("0입니다.")    
# else:
#     print("음수")    



# # 조건문을 여러개
# score = 65
# if score>=90:
#     print("A")
# elif score>=80:
#     print("B")
# elif score>=70:
#     print("C")
# elif score>=60:
#     print("D")
# else:
#     print("F")                



# 조건문안에 조건문
# a = 1
# if a>50:
#     if a<100:
#         print("50보다 크고, 100보다 작은수")
#     else:
#         print("50보다 크고,100보다 큰수")    
# else:
#     print("50보다 작은수")        