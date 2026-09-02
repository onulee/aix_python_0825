# 1. 번호,이름,국어,영어,수학
# 2. 합계,평균
# 3. 성적출력하도록 구성하시오.

# 입력 -> 변수저장 -> DB저장
s = [] #리스트타입 - append,insert / pop,del,remove
no = input("번호 입력 : ")      #str
name = input("이름 입력 : ")
kor = int(input("국어점수 입력 : "))  #int
eng = int(input("영어점수 입력 : "))  #int
math = int(input("수학점수 입력 : "))  #int
total = kor+eng+math
avg = total/3  # 나눗셈 -> float

print("[학생성적프로그램]")
print("번호\t이름\t국어\t영어\t수학\t합계\t평균")
print("-"*60)  #문자*반복
print(f"{no}\t{name}\t{kor}\t{eng}\t{math}\t{total}\t{avg:.2f}")
# print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}".\
#       format(no,name,kor,eng,math,total,avg))


