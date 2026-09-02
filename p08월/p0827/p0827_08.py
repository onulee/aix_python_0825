# 1.1-100까지 랜덤숫자 3개를 리스트에 추가
# 2.1개 숫자를 입력받아 
# 있으면 당첨, 없으면 꽝
# 랜덤숫자 리스트 출력
# 입력숫자 출력
import random
# num1 = random.randint(1,100)
# num2 = random.randint(1,100)
# num3 = random.randint(1,100)
# 중복이 있을수 있음.
# arr = [num1,num2,num3]
# arr.sort() # 순차정렬
# random.sample(range(1,101),3)
# 중복없이 1-100사이 숫자 추출
arr2 = random.sample(range(1,101),3)
input1 = int(input("숫자입력 : "))
if input1 in arr2:
    print("당첨")
else:
    print("꽝")
print("랜덤숫자 :",arr2)
print("입력숫자 :",input1)        
