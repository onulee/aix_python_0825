# 학생성적
stu = []
c_no = 1   #학생번호로 사용

def main_print():
    # 메인화면 출력부분
    print("[ 학생성적프로그램 ]")
    print("-"*60)
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("-"*60)

def stu_input():  #학생성적입력함수
    c_no = 1   #학생번호로 사용
    print()
    while True:
        print("[ 학생성적입력 ]")
        no = c_no
        name = input("학생이름입력 (0.이전페이지 이동) : ")
        if name=="0": break
        kor = int(input("국어점수입력 : "))
        eng = int(input("영어점수입력 : "))
        math = int(input("수학점수입력 : "))
        total = kor+eng+math
        avg = total/3
        stu.append(
            {"no":no,"name":name,"kor":kor,"eng":eng\
            ,"math":math,"total":total,"avg":avg}
        )
        print(name,"학생 성적이 저장되었습니다.")
        c_no += 1   # 다음번호 1증가
    print()

while True:
    main_print() #함수호출
    choice = int(input("원하는 번호를 입력하세요."))
    # 학생성적입력부분
    if choice == 1:
        stu_input()
    # 학생성적출력부분
    elif choice == 2:
        print()
        print("[ 학생성적출력 ]")
        print("-"*60)
        print("번호\t이름\t국어\t영어\t수학\t합계\t평균")
        print("-"*60)
        for s in stu:
            print(f"{s['no']}\t{s['name']}\t{s['kor']}\
\t{s['eng']}\t{s['math']}\t{s['total']}\
\t{s['avg']:.2f}") 
        print()       


