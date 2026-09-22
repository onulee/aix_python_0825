title = ["번호",'이름','국어','영어','수학','합계','평균']
k_title = ["no",'name','kor','eng','math','total','avg']
stu = []
sno = 1 #학생성적인원변수 - db
# 파일불러오기 
# -------------------------------------------
f = open("C:/aaa/test2.txt","r",encoding="utf-8")
while True:
    line = f.readline() # /n 줄바꿈때문에 에러가 남.
    if line=="": break
    line = line.strip()
    arr = line.split(",")
    for i,a in enumerate(arr):
        if 5>=i>=2:
            arr[i] = int(a)
        elif i==6:
            arr[i] = float(a)    
    # stu 리스트에 저장
    stu.append({'no':arr[0],'name':arr[1],'kor':arr[2],'eng':arr[3],'math':arr[4],'total':arr[5],'avg':arr[6]})
f.close()
#-------------------------------------------




# 함수선언 ------------------------------------
def s_mainPrint():
    # 메인화면부분
    print("[ 학생성적프로그램 ]")
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("3. 학생성적수정")
    print("-"*60)
    choice = int(input("원하는 번호를 입력하세요.>> "))
    print()
    return choice



# 학생성적입력함수선언
def s_input(): 
    global sno
    while True: #입력을 멈추고 싶을때까지 입력받음
        no = sno  # 번호자동부여 / 
        print("[ 학생성적입력 ]")
        name = input(f"{no}번째 이름입력 (0.이전화면이동) : ")
        if name == "0": break
        kor = int(input("국어점수입력 : "))
        eng = int(input("영어점수입력 : "))
        math = int(input("수학점수입력 : "))
        total = kor+eng+math
        avg = total/3

        # 리스트저장 - 파일저장 - db저장
        stu.append({'no':no,'name':name,'kor':kor,\
                    'eng':eng,'math':math,'total':total,\
                        'avg':avg})
        print(f"{name} 학생성적이 저장되었습니다.")
        print()
        # score = [0]*3
        # for i in range(3):
        #     score[i] = int(input(f"{title[i+2]} 점수입력 : "))
        sno += 1
        s_output() 

def s_output(): # 학생성적출력부분 함수
    print()
    print("[ 학생성적출력 ]")
    print("-"*60)
    print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))  
    print("-"*60)
    if len(stu)==0:
        print("*** 학생데이터가 없습니다. ***")
    else:    
        for s in stu:
            print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}")
    print()

def s_update(): # 학생성적수정
    print()
    print("[ 학생성적수정 ]")
    name = input("찾을려는 학생이름을 입력하세요.>> ") 
    temp = 0
    for i,s in enumerate(stu):
        if s['name']==name:
            print(f"{name} 학생을 찾았습니다.")
            temp = 1
            break 

    if temp == 0:
        print(f"{name} 학생이 없습니다.")
    elif temp == 1:
        print("[ 과목수정선택 ]")
        print("1. 국어   2. 영어   3. 수학")
        choice = int(input("원하는 번호입력 : "))
        
        print(f"현재{title[choice+1]}점수 : {s[k_title[choice+1]]}")
        s[k_title[choice+1]] = int(input(f"변경하려는 {title[choice+1]}점수 : "))
        s['total'] = s['kor']+s['eng']+s['math']
        s['avg'] = s['total']/3
        print(f"{s[k_title[choice+1]]}점으로 {title[choice+1]}점수가 변경되었습니다.")
        

        
#----------------------------------------------------
# 실제프로그램 시작부분
#----------------------------------------------------
while True:
    choice = s_mainPrint()  # 메인화면부분 함수호출
    if choice == 1:   # 학생성적입력부분
       s_input()  
    elif choice == 2: # 학생성적출력부분 
       s_output()
    elif choice == 3: # 학생성적수정부분
       s_update() 

        

