alist = list(range(1,21))
nlist = []
for a in alist:
    if a%3==0: nlist.append(a)
print(nlist)

a = [n for n in range(1,21) if n%3==0]
print(a)

# name_dic = {
#     "aaa":'토마토',"ddd":"바나나","eee":"딸기","bbb":"배"
# }

# # [b,c,a,k,l,d,z,y]

# name_sort1 = []
# # name_sort1 = sorted(name_dic.items(),key=lambda x:x[1])
# name_sort1 = sorted(name_dic.items(),key=lambda x:x[0],reverse=True)

# print(name_sort1)




# # 리스트 자동생성방법 4가지
# alist = [i for i in range(1,11)] #리스트내포:컴프리헨션
# print(alist)
# alist2 = list(range(1,11))
# print(alist2)
# alist3 = [0]*10
# print(alist3)
# alist4 = [1,2,3,4,5,6,7,8,9,10]
# print(alist4)

# engs = {
#     "car":"자동차",
#     "color":"색상",
#     "pig":"돼지",
#     "love":"사랑",
#     "phone":"전화기"
# }

# print(engs.keys())
# print(engs.values())
# print(engs.items())

# for k,v in engs.items():
#     print(k,"는(은) 한국어로 무엇일까요?")
#     answer = input("정답 : ")
#     if answer == v:
#         print("[ 정답입니다.^^ ]")
#     else:
#         print("[ 오답입니다.ㅜㅜ]")









# 
# stu = {"no":1,"name":"홍길동","total":100}
# for i,v in stu.items():
#     print(i,":",v)


# print(stu.keys())  # key
# print(stu.values()) # value
# print(stu.items())  # key,value
# s_list = list(stu.values()) # 딕셔너리리스트 -> list()타입변환
# print(s_list)



# stu = {"no":1,"name":"홍길동","kor":100,"eng":100,"math":100,"music":100}
# stu_arr = [1,"홍길동",100,100,100,100]

# print(stu)
# # 딕셔너리 추가 : 없는키 입력
# stu["total"] = 400
# stu["avg"] = stu["total"]/4
# print(stu)

# # 딕셔너리 수정 : 있는키에 값을 넣으면 수정됨.
# stu["kor"] = 50
# print(stu)

# # 딕셔너리 출력 : 키 출력
# print(stu["kor"])

# # 딕셔너리 삭제 : del(키)
# del(stu["eng"])
# print(stu)

# stu_list = [
#     {"no":1,"name":"홍길동","kor":100,"eng":100,"math":100,"total":400,"avg":100.0},
#     {"no":2,"name":"유관순","kor":100,"eng":100,"math":100,"total":400,"avg":100.0},
#     {"no":3,"name":"이순신","kor":100,"eng":100,"math":100,"total":400,"avg":100.0},
# ]
# stu_list[0]['name'] = "홍길자" # 있는키 입력:수정
# print(stu_list[0]['name'])   # 출력
# print(stu_list[0]['kor'])
# stu_list[0]['rank'] = 1  # 없는키입력:추가
# del(stu_list[0]['no'])   # 삭제
# print(stu_list)

# # print(stu_list[0]['no'])
# print(stu_list[0].get('no'))