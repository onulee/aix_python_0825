import random
a_arr = list(range(1,26))
random.shuffle(a_arr)
while True:
    print(" "*15,end="")
    print("[ 빙고게임 ]")
    print("-"*50)
    for i,v in enumerate(a_arr):
        if (i+1)%5!=0:
            print(v,end="\t")
        else:
            print(v)    
    print("-"*50)
    num = int(input("원하는 번호를 입력하세요.>> "))
    if num in a_arr:
        idx = a_arr.index(num)
        a_arr[idx] = "X"



# aa = list(range(1,13))
# print(aa)

# a_arr = []
# for i in range(0,12,4):
#     a_arr.append(aa[i:i+4])
# print(a_arr)

# #-----------------------
# import random
# aa = list(range(1,26))
# random.shuffle(aa)
# for i,v in enumerate(aa):
#     if (i+1)%5!=0:
#         print(v,end="\t")
#     else:
#         print(v)

# [
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12]
# ]



# a_arr = [1,5,10,20,90,100,7,2]
# a_arr2 = [*a_arr]
# a_arr3 = a_arr.copy()  #깊은복사
# a_arr2.sort()
# a_arr2.sort(reverse=True)
# a_arr2.reverse()
# a_arr[0] = 100
# print(a_arr)
# print(a_arr2)
# print(a_arr3)
