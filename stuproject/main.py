from stuFunc import *

readStu() # 파일불러오기
while True:
    # 0.메인화면함수
    choice = main_screen()
    if choice == 1:
        stu_input()    # 1.학생성적입력함수
    elif choice == 2:
        stu_output()   # 2.학생성적출력함수
    elif choice == 3:
        stu_update()
    elif choice == 8:
        print("[ 등수처리 ]")
    elif choice == 9:
        writeStu()
    else:
        print("프로그램 종료")
        break