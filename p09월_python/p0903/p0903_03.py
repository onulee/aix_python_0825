def cal1():
    for i in range(2,10):
            for j in range(1,10):
                print(f"{i}x{j}={i*j}") 

def cal2(num1,num2):
     print(num1+num2)
     print(num1-num2)

def cal3():
     sum = 0
     for i in range(1,11):
          sum += i
     print("합계 : ",sum)     

print("1.구구단 출력")
print("2.두수를 입력받아, +,- 값을 출력")
print("3. 1-10까지 합을 출력")
choice = int(input("원하는 번호를 입력하세요.>> "))

if choice == 1:
    cal1()
elif choice == 2:
    num1 = int(input("숫자입력 : "))
    num2 = int(input("숫자입력 : "))
    cal2(num1,num2)
else:
    cal3()


