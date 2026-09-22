# 학생2명의 성적을 입력받아 출력하시오.
# 번호,이름,국어,영어,수학 점수를 입력받아
# 번호,이름,국어,영어,수학,합계,평균을 출력하시오.

# 1. 성적입력
# 2. 성적처리 수식
# 3. 성적출력

# 1. 성적입력
no = input("번호입력 : ")
name = input("이름입력 : ")
kor = int(input("국어점수 입력 : "))  # 한줄복사 shift+alt+방향키
eng = int(input("영어점수 입력 : "))
math = int(input("수학점수 입력 : "))
# 2.성적처리 수식
total = kor+eng+math
avg = total/3
# 3.성적출력
print("번호\t이름\t국어\t영어\t수학\t합계\t평균")
print("{}\t{}\t{}\t{}\t{}\t{}\t{}".\
      format(no,name,kor,eng,math,total,avg))