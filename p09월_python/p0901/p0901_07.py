a,b,c,d,e,f = 0,0,0,0,0,0
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(a+b+c+d+e+f)

a_arr = [10,20,30,40,50,60,70,80,90,100]
sum = 0
for a in a_arr:
    print(a)
    sum += a
print(sum)
# print(a_arr[2:5]) 
# print(a_arr[::-1])  
# 
# 리스트 추가 : append:뒤에, insert:위치, extend:리스트+리스트 
# 리스트 수정 : a_arr[위치] = 1000
# 리스트 삭제 : pop(위치):위치가 없으면 제일뒤에, del 위치

a_list = [1,2,3]
a_list.append(4)
print(a_list)
a_list.pop()
print(a_list)
a_list.pop(0) # 위치
print(a_list)


# 퀴즈
n_arr = [100,91,230,1,2,5,70,500]
# 100이상의 숫자만 출력하시오.
# 100:3자리숫자
# 91:2자리숫자
# 230:3자리숫자
# 1:1자리숫자
a_arr = []
for n in n_arr:  # n타입:정수형타입 -> 문자타입
    no = len(str(n))
    a = "{}:{}자리숫자".format(n,no)
    a_arr.append(a)
    print(a)
print(a_arr)    



# for n in n_arr:
#     if n>=100:
#         a_arr.append(n)
#         print(n)

# print(a_arr)


# a = 100
# b = "100"
# print(len(b))
# print(len(a))