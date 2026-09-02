# 1. 번호,이름,국어,영어,수학
# 2. 합계,평균
# 3. 성적출력하도록 구성하시오.

# 입력 -> 변수저장 -> DB저장
s = [0,0,0,0,0,0,0] #리스트타입 - append,insert / pop,del,remove
s[0] = input("번호 입력 : ")
s[1] = input("이름 입력 : ")
s[2] = int(input("국어점수 입력 : "))  #int
s[3] = int(input("영어점수 입력 : "))  #int
s[4] = int(input("수학점수 입력 : "))  #int
s[5] = s[2]+s[3]+s[4]
s[6] = s[5]/3  # 나눗셈 -> float

print("[학생성적프로그램]")
print("번호\t이름\t국어\t영어\t수학\t합계\t평균")
print("-"*60)  #문자*반복
print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]:.2f}")
# print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}".\
#       format(no,name,kor,eng,math,total,avg))


