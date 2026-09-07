# import func 
# import func as fn
from func import hap,hap2,hap3

# 1. 매개변수X, return X - hap()
hap()
print("hap()완료")

# 2. 매개변수 O, return X - hap2()
num1 = int(input("숫자입력1 : "))
num2 = int(input("숫자입력2 : ")) 
hap2(num1,num2)
print("hap2()완료")

# 3. 매개변수 O, return O - hap3()
num1 = int(input("숫자입력1 : "))
num2 = int(input("숫자입력2 : ")) 
sum = hap3(num1,num2)
print(sum)
print("hap3()완료")




