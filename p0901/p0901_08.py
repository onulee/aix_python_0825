stu_list = [
    [1,"홍길동",100,90,80,270,90.0],
    [2,"유관순",90,80,70,240,80.0],
    [3,"이순신",80,70,60,210,70.0],
]

while True:
    flag = 0  #초기화
    name = input("검색이름입력 : ")
    for i,stu in enumerate(stu_list):
        if name in stu:
            stu_index = stu.index(name)
            print("해당하는 이름이 있습니다.")
            flag = 1
            break

    if flag == 0:
        print("해당하는 이름이 없습니다.")    


# name_arr = ["홍길동","유관순","이순신","강감찬","김구"]
# name = input("검색할 이름을 입력하세요.>> ")
# # print(name_arr.index(name))
# print(name_arr.find(name)) # 문자 find,rfind

# while True:
#     name = input("검색할 이름을 입력하세요.>> ")
#     if name in name_arr:
#         no = name_arr.index(name)
#         print(no,":",name," 학생이 검색되었습니다.")
#         change = input("변경할 이름을 입력하세요.>> ")
#         name_arr[no] = change
#         print(name_arr)
#     else:
#         print(name, "학생은 없습니다.")



# stu_list = [
#     [1,"홍길동",100,90,80,270,90.0],
#     [2,"유관순",90,80,70,240,80.0],
#     [3,"이순신",80,70,60,210,70.0],
# ]

# 유관순 - 국어:100, 영어:50
#  [2,"유관순",90,80,70,240,80.0]
# stu_list[1][2] = 100
# stu_list[1][3] = 50
# stu_list[1][5] = stu_list[1][2]+stu_list[1][3]+stu_list[1][4]
# stu_list[1][6] = stu_list[1][5]/3
# print(stu_list)

# stu_list[0][1] = "홍길자"
# print(stu_list)
# print(stu_list[0][2],stu_list[0][3],stu_list[0][4])


# aa = []
# bb = []
# value = 0
# for i in range(0,100):
#     aa.append(value)
#     value += 2
# print(aa) 

# cc = list(range(0,200,2))
# print(cc)

# # 리스트내포
# dd = [i for i in range(0,200,2)]
# print(dd)

# # for i in range(0,100):
# #     bb.append(aa[99-i])
# # print(bb) 
# # 
# # 
# aa =[10,20,30]
# bb = [1,2,3]
# print(aa*3) 
# print(aa+bb)  #aa,bb가 값이 변경이 안됨.  extend

# aa.extend(bb) # aa의 값이 변경됨.
# print(aa)

# a = 1
# b = 2
# print(a+b) # 3

# aa.append(1)  # aa값이 변경 
# # append,insert,extend,pop,del

# aa = [1,2,3,4,5,6,7]
# print(aa[::-1])
# print(aa[::-2])

# aa = [1,2,3]
# aa[1:2] = [20,30]
# print(aa)
