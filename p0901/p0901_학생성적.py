stu_list = []

while True:
    print("[ 학생성적프로그램 ]")
    print("1. 학생입력")
    print("2. 학생출력")
    print("3. 학생성적수정")
    print("4. 학생성적삭제")
    print("5. 학생검색")
    print("0. 프로그램종료")
    print("-"*40)
    choice = int(input("원하는 번호를 입력하세요.>> "))
    if choice == 1:
        print("[ 학생성적입력 ]")
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
            print(name," 학생성적이 등록되었습니다.")
            print()

    elif choice == 2:
        print("[ 학생성적출력 ]")
        print("입력된 학생성적 : ",len(stu_list))
        print("번호\t이름\t국어\t영어\t수학\t합계\t평균")
        print("-"*60)
        for s in stu_list:
            print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}".format(*s))

    elif choice == 3:
        print("[ 학생성적수정 ]")

    elif choice == 4:
        print("[ 학생성적삭제 ]")
        
    elif choice == 5:
        print("[ 학생검색 ]")



    else:
        print("[ 프로그램 종료 ]")
        break