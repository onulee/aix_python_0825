# 1-100까지 랜덤숫자를 1개 생성해서
# 무한반복해서 숫자를 맞추는 프로그램을 구현하시오.
# 입력한 숫자가 크면 크다
# 입력한 숫자가 작으면 작다라고 출력하고
# 맞추면 정답이라고 출력
# 입력한 숫자가 모두 출력되도록 하시오.

import random
ran_num = random.randint(1,100) #타입:int
arr_num = []
while True:
    input_num = int(input("숫자를 입력하세요.>> ")) #타입:str->int
    arr_num.append(input_num) #입력한 숫자 리스트에 추가
    if input_num == ran_num:
        print("정답")
        break
    elif input_num>ran_num:
        print("입력한 숫자가 더 큽니다.")
    else:
        print("입력한 숫자가 더 작습니다.")        

print("랜덤숫자 : ",ran_num)
print("입력한 모든 숫자 : ",arr_num)
