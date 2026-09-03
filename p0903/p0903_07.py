# from func import cal1,cal2,cal3
from func import *
cal1()
cal2()
cal3()

import datetime
import random
import sys

print(sys.builtin_module_names)

import math
dir(math)
print(math.log(10))
print(math.sin(10))
print(math.floor(10.921)) # 버림
print(math.ceil(10.111))  # 올림
print(round(10.567,1))  # 반올림 (값,소수점자리)



# now = datetime.datetime.now()
# print(now)


# import func
# func.cal1()
# func.cal2()
# func.cal3()



# def func1(a,b,*num):
#     sum = a + b
#     for n in num:
#         sum += n
#     return sum

# print(func1(1,2,3))
# print(func1(1,10))
# print(func1(10,20,30,40,50))




# def func1(*num):
#     sum = 0
#     for n in num:
#         sum += n
#     return sum

# print(func1(1,2,3))
# print(func1(1,2))
# print(func1(10,20,30,40,50))






# def func1(a,b,c):
#     print(a)
#     return a+10

# c = 30 
# result = func1(10,2,c)
# print(result)





# def func1():
#     global a  # 전역변수에 선언되어 있는 링크를 가져옴
#     a = 10 #지역변수
#     b = 5
#     c = 1
#     print("func1 a : ",a)
# #----------------------------
# a = 20 #전역변수
# func1()
# print("전역변수 : ",a)    




# def func1():
#     a = 10 # 함수a
#     print("func1 a : ",a)

# def func2():
#     print("func2 a : ",a)

# a = 20 # 함수밖 a
# # 실행
# func1()  # 10
# func2()


