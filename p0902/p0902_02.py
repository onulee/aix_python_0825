from func import *

main_print()

### 1.앞뒤공백제거 - strip()
a = "      abc       "
print(a.strip()) #공백제거 -> a반영은 안됨.

### 2.중간공백제거 - replace()
b = "     a      b"
print(b.strip())
print(b.replace(" ",""))

### 3.분리 : split - 리스트타입으로 전달됨.
c = "딸기,수박,바나나,사과"
print(c)
print(c.split(","))

d = "1,홍길동,100,100,100,300,100.0"
dlist = d.split(",")
dlist[2] = 90
dlist[3] = int(dlist[3])
dlist[4] = int(dlist[4])
dlist[5] = dlist[2]+dlist[3]+dlist[4]
dlist[6] = dlist[5]/3

dlist2 = [str(i) for i in dlist]
print(dlist)

# 4. 특정문자로 결합 - join  "1"+1
# 문자열리스트만 변경가능 join결합
# 문자열로 변환됨.
d_str = ",".join(dlist2)
print(d_str)

# 5. count : 문자열안에 해당문자가 몇개 있는지 확인
# 6. find : 문자열안에 해당문자 위치 반환, 없으면 -1
# 7. index : find와 동일, 없으면 에러








# # join
# aa = "/"
# bb = aa.join(["바나나","딸기","사과"])
# print(bb)
# print(type(bb))




# ss = "   파이썬"       #파이썬 - strip
# ss2 = "<<<<파<<이<썬"  #파이썬 -replace
# print(ss.strip())
# print(ss2.replace("<",""))


# aa = input("이름을 입력하세요.>> ").strip()

# aa = [1,2,   3, 4 ,5]




# ss = "파이썬 공부!! 열심히 합시다. 파이썬"
# print(ss.count("공부"))
# print(ss.count("파이썬"))
# print(ss.find("공부"))  #4
# print(ss.find("자바"))  #없을때 : -1
# print(ss.index("자바")) # index는 없을때 에러




# aa = "a/b/c/d/f/g"
# aa_list = aa.split("/")
# print(aa_list)

# bb = "100,10,5,4,1"
# # 모든수의 합을 구하시오.
# bb_list = bb.split(",")
# bb_list = [int(i) for i in bb_list]
# sum = 0
# for b in bb_list:
#     sum += b
# print(bb_list)
# print("합계 : ",sum)

# bb_list2 = [int(i) for i in bb_list]
# print(bb_list2)




# aa = "가나다라가가가나나다라라라라라라라"
# ##
# # {가:10,나:5,다:11...}
# aa_dict = {}
# for a in aa:
#     if a not in aa_dict:
#         aa_dict[a] = 1
#     else:
#         aa_dict[a] += 1


# print(aa_dict)



# a = [1,2,3,4,5]
# b = [10,20,30,40,50]
# c = []

# c = list(zip(a,b))
# d = dict(zip(a,b))
# print(c)
# print(d)

# for i,j in zip(a,b):
#     c.append([i,j])
# print(c)    

# for i in range(len(a)):
#     c.append([a[i],b[i]])
# print(c)    




# 리스트 생성방법
# a1 = [1,2,3,4,5]
# a2 = [0]*5
# a3 = list(range(1,6))
# a4 = [i*i+2 for i in range(1,6) if i%2==0] #리스트내포
# print(a4)


# # a = ["바나나","딸기","사과","딸기","딸기","사과"]
# aa = [1,2,3,1,1,1,2,3,1,1,1,2,2,3]
# # print(aa.count("딸기"))
# # {"바나나":1,"딸기":3,"사과":2}
# aa_dic = {}
# for a in aa:
#     if a not in aa_dic:
#         aa_dic[a] = 1
#     else:
#         aa_dic[a] = aa_dic[a]+1
#         print("있습니다.")    

# print(aa_dic)

# 딕셔너리
# a_dic = {"바나나":1,"딸기":3,"사과":2} 
# print(a_dic["바나나"])  #출력
# a_dic["배"] = 5         #추가
# print(a_dic) 
# del a_dic["바나나"]      #삭제
# print(a_dic) 
# a_dic["사과"] = 100      #수정
# print(a_dic) 

# a = 10
# a2 = 0
# a2 = a
# print(a2)
# a = 100
# print(a2)


# alist = [1,2,3]
# alist2 = []
# alist2 = alist      # 얕은복사
# # alist2 = [*alist] # 깊은복사
# print(alist2)  # 1,2,3


# alist[0] = 100
# print(alist2)
