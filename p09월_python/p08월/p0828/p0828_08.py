# 날짜함수,랜덤함수
import datetime
import random

a = [1,2,3,4,5]
print(a)
a[2]=30
a[3]=500
print(a)
a.pop(2)
print(a)
a.append(200)
print(a)




# # 1-45까지 랜덤5개를 가져와서
# # 입력한 숫자가 있으면 당첨,없으면 꽝
# # 1개만 우선
# # 5개

# lotto = random.sample(range(1,46),5)
# print(lotto)
# iarr = []
# # 반복문
# for i in range(5):
#     iarr.append(int(input("숫자입력 : ")))

# # 비교해서 있으면 당첨,없으면 꽝
# for i in range(5):
#     if iarr[i] in lotto: print("당첨")
#     else: print("꽝")






# # 랜덤 5개
# # randint-랜덤1개, sample-랜덤여러개(중복불가),
# # shuffle-전체섞음, choices-랜덤여러개(중복가능)
# a = random.randint(1,45) #랜덤1개
# arr = random.sample(range(1,46),5) #1-45까지 중복없이 5개를 가져옴.
# print(arr)
# arr2 = random.sample([1,2,3],2)
# print(arr2)
# arr3 = [1,2,3,4,5]  # 리스트 전체를 랜덤으로 섞어줌.
# random.shuffle(arr3)
# print(arr3)
# arr4 = [1,2,3,4,5]
# arr5 = random.choices(arr4,k=5) # 리스트 해당개수만큼 가져옴.중복가능
# print(arr5)

# 리스트생성방법
# alist1 = [0,0,0,0,0]
# alist2 = [0]*5
# alist3 = list(range(1,6))
# print(alist1)
# print(alist2)
# print(alist3)






# # 
# now = datetime.datetime.now()
# #year,month,day,hour,minute,second
# print(now)
# print(now.year)
# print(now.month)

# # random
# r_num = random.randint(1,12)
# # 3,4,5 봄, 6,7,8 여름, 9,10,11 가을 12,1,2 겨울이라고 출력하시오.
# if 3<=r_num<=5:
#     print("봄")
# elif 6<=r_num<=8:
#     print("여름")    
# elif 9<=r_num and r_num<=11:
#     print("가을")
# else:
#     print("겨울")   


# # now.month  
# # 01월,02월   
