# 전개연산자
arr = [1,2,3,4,5]
arr2 = []
arr3 = []
arr2 = arr    # 얕은복사 - 2개의 리스트 상관관계 생김.
arr3 = [*arr] # [1,2,3,4,5]  깊은복사 - 2개의 리스트 상관관계가 없음
print(arr)
print(arr2)
print(arr3)
print("-"*50)
# 2번째
arr2[0] = 5000
print(arr)
print(arr2)
print(arr3)




# arr3 = [*arr]
# arr3 = [1,2,3,4,5]

# arr[2] = 1000
# print(arr)
# print(arr2)

# # print(arr)
# # print(*arr)
# # arr2 = []
# # a = 1
# # a2 = 0 

# # a2 = a
# # print(a2) # 1
# # a = 100
# # print(a2) # 1