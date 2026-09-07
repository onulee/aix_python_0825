# import p_stu_m as pm
from p_stu_m import *

   


readStu() # 파일불러오기
while True:
    # 0.메인화면함수
    choice = main_screen()
    if choice == 1:
        stu_input()    # 1.학생성적입력함수
    elif choice == 2:
        stu_output()   # 2.학생성적출력함수
    elif choice == 3:
        pass
    elif choice == 9:
        writeStu()
    else:
        print("프로그램 종료")
        break
