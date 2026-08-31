import random

# 로또 랜덤부분
lotto = random.sample(range(1,46),6)
# print("확인로또>> : ",lotto)
# 입력6개
myNum = []
i = 0
while i<6:
    no = int(input("숫자입력 : "))
    if no not in myNum:
        myNum.append(no)
        i = i+1
    else:
        print("번호가 있습니다.")  

# 맞는지 확인
count = 0
answer = []
for i in myNum:
    if i in lotto:
        count = count+1
        answer.append(i)

print("로또번호 : ",lotto)
print("입력한번호 : ",myNum)
print("정답번호 : ",answer)
print("정답개수 : ",count)



# # 6개 입력부분
# myNum = []  # 6개 입력 
# i = 0
# while i<6:
#     no = int(input("숫자입력 : "))
#     if no not in myNum:
#         myNum.append(no)
#         i = i+1
#     else:
#         print("번호가 있습니다.")    

# # 정답확인 부분
# answer = []
# count = 0
# for i in myNum:
#     if i in lotto:
#         count = count + 1
#         answer.append(i)


# # 6개를 입력받아 있는지 확인하시오.
# print("로또번호 : ",lotto)
# print("입력숫자 : ",myNum)
# print("정답확인 : ",answer)
# print("정답개수 : ",count)








# import random
# # 1개 랜덤
# a = random.randint(1,45)
# print(a)
# # 리스트를 섞어줌.
# alist = list(range(1,46))
# print(alist)
# random.shuffle(alist)
# print(alist)
# # 랜덤으로 개수만큼 추출 - 중복이 안됨.
# ranArr = random.sample(range(1,46),6)
# print(ranArr)

# # 랜덤으로 개수만큼 추출 - 중복가능
# ranArr2 = random.choices(range(1,46),k=6)
# print(ranArr2)


# myNum = []  # 6개 넣어야 하는데 
# i = 0
# while i<6:
#     no = int(input("숫자입력 : "))
#     if no not in myNum:
#         myNum.append(no)
#         i = i+1
#     else:
#         print("번호가 있습니다.")        

# print("입력숫자 : ",myNum)





    
# for i in range(6):
#     no = int(input("숫자입력 : "))
#     if no not in myNum:
#         myNum.append(no)
#     else:
#         print("번호가 있습니다.")