# 로또맞추기
# 학생성적프로그램
# 학생성적입력 - 변수,리스트-리스트,리스트-딕셔너리
# stu_list = [
#     [1,"홍길동",100,100,100,300,100.0],
#     [2,"유관순",100,100,100,300,100.0],
#     [3,"이순신",100,100,100,300,100.0],
# ]
stu_list = []
# stu_list.append([1,"홍길동",100,100,100,300,100.0])
while True:
    no = len(stu_list)+1 #
    # no = input("번호입력 : ")
    print("자동번호 : ",no)
    name = input("이름입력(종료하려면 0) : ")
    if name=="0": break
    kor = int(input("국어입력 : "))
    eng = int(input("영어입력 : "))
    math = int(input("수학입력 : "))
    total = kor+eng+math
    avg = total/3
    stu_list.append([no,name,kor,eng,math,total,avg])

print("입력된 학생성적 : ",len(stu_list))
print("번호\t이름\t국어\t영어\t수학\t합계\t평균")
print("-"*60)
for s in stu_list:
    print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}".format(*s))
    
    










# [1,2,3,4,5,6,7,8,9] 1차원리스트
# 리스트 - 직접입력,[0]*9,list(range(1,10))
# num_arr = list(range(1,10))
# print(num_arr)
# all_arr = []
# for i in range(0,9,3): # 0,3,6
#     print(i,end=" ") # 0,3,6
#     all_arr.append(num_arr[i:i+3])
#     # all_arr.append(num_arr[0:0+3])  #0-3 / 0,1,2
#     # all_arr.append(num_arr[3:3+3])  #3-6 / 3,4,5
#     # all_arr.append(num_arr[6:6+3])  #6-9 / 6,7,8
# print(all_arr)
