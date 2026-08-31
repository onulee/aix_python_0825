name = []
kor = []
eng = []
math = []
total = []
avg = []
for i in range(3):
    name.append(input("이름입력 :")) 
    k_input = int(input("국어점수입력 : "))  
    kor.append(k_input)
    e_input = int(input("영어점수입력 : "))
    eng.append(e_input)
    m_input = int(input("수학점수입력 : "))
    math.append(m_input)
    total.append(k_input+e_input+m_input)
    avg.append((k_input+e_input+m_input)/3)

print("[ 학생성적 ]")
print("번호\t이름\t국어\t영어\t수학\t합계\t평균\t")
print("-"*60)
for i in range(len(name)):
    print(f"{i+1}\t{name[i]}\t{kor[i]}\t{eng[i]}\t{math[i]}\
\t{total[i]}\t{avg[i]:.2f}")

# [학생성적]
# 홍길동 70
# 유관순 100
# 이순신 90




# list_a = ["바나나","딸기","사과","배","복숭아"]
# j = 1
# for i in list_a:
#     print(j,":",i) # 1:바나나,2:딸기,3:사과
#     j = j+1

# # enumerate : index번호,리스트값 2개 전달
# for i,value in enumerate(list_a):  
#     print(i+1,":",value)

# for i in range(len(list_a)):
#     print(i+1,":",list_a[i])



# for i in range(1,4):
#     print(i)   # 1,2,3


 


# list_a = ["바나나","딸기","사과"]
# for i in range(3):
#     list_a.append(input("과일입력 : "))

# for i in list_a:
#     print(i) 



# 구구단을 출력하시오.
# 숫자입력: 5, 5단부터 출력하시오.
# # 5단만 출력
# a = int(input("시작되는 단 입력 : "))
# b = int(input("끝부분 : "))
# for i in range(a,a+1):
#     for j in range(1,b+1):
#         print(f"{i}x{j}={i*j}")





# sum = 0
# # 입력한 첫번째 숫자부터 두번째 입력한 숫자까지 합을 구하시오.
# # 2,5

# a = int(input("1.숫자입력 : "))
# b = int(input("2.숫자입력 : "))
# c = 0
# if a>b:  # a가 클때만 값을 서로 변경
#     a,b = b,a
#     # c = a
#     # a = b
#     # b = c 
# for i in range(a,b+1):
#     sum = sum + i
# print("합 : ",sum)


# # 3개의 입력한 숫자의 합을 구하시오.
# # 1. 입력 int(input("숫자입력 : "))
# # 2. for문 3번  for i in range(3):
# # 3. sum   sum = sum + input1

# sum = 0
# alist = []
# for i in range(3):
#     input1 = int(input("숫자입력 : "))
#     alist.append(input1)
#     sum = sum + input1

# print("합계 : ",sum)
# print("입력값 : ",alist)




# # 1-100까지 합을 출력하시오.
# sum = 0
# for i in range(1,101):
#     if i%7==0:
#         print(i)
#         sum = sum + i
# print("합 : ",sum)   

# 홀수 합을 구하시오.
# 7의 배수만 합을 구하시오.





# sum = 0
# no = 0
# sum2 = 0
# for i in range(1,101):  # 1-10:55 / 1-100:5050
#     sum = sum + i
#     if sum>100:
#         no = i
#         sum2 = sum
#         break

# print("합계가 100을 넘을때 i의 값 : ",no)
# print("그때 합계 : ",sum2)
# print("이전단계 : ",no-1)
# print("이전단계 합 : ",sum2-no)
# # sum 이 100 넘을때 i값을 출력하시오.



sum = 0
result = 1
for i in range(1,11):
    sum = sum + i
    result = result * i

# sum 이 100 넘을때 i값을 출력하시오.


# print("합계 : ",sum)
# print("곱 : {:,}".format(result))
# # 합계 : 55
# # 1-10까지 곱 : 



# # 구구단을 아래로 출력하시오.
# for i in range(2,10):
#     print(f"[{i}단]",end="\t")
# print()     
# for i in range(1,10):
#     for j in range(2,10):
#         print("{}x{}={}".format(j,i,i*j),end='\t') 
#     print() 

