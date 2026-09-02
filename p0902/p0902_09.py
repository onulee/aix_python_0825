import random
from gugudan import gugudan_func

def main_print():
    print("1.구구단 출력프로그램")
    print("2.1-10까지 숫자맞추기 프로그램")
    print("3.두수를 입력받아 +,-,*,/ 결과값 출력프로그램")
    choice = int(input("원하는 번호입력 : "))
    return choice

def number_func():
    ran_num = random.randint(1,10)
    while True:
        in_num = int(input("1-10사이의 숫자입력 : "))
        if in_num == ran_num:
            print("정답입니다.")
            break
        elif in_num>ran_num:
            print("작은수 입력해주세요.")
        else:
            print("큰수를 입력해주세요.")
    print("랜덤숫자 : ",ran_num)



def cal_func():
    num1 = int(input("숫자입력 : "))
    num2 = int(input("숫자입력 : "))
    print("더하기 : ",num1+num2)
    print("빼기 : ",num1-num2)
    print("곱하기 : ",num1*num2)
    print("나누기 : ",num1/num2)

while True:
    # 메인출력
    choice = main_print()
    if choice==1:
        gugudan_func()
    elif choice == 2:
        number_func()       
    else:
        cal_func()
