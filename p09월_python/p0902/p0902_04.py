
# 함수사용이유 : 긴 구문의 반복적인 명령어를 줄일수 있음
# 코드를 간결하게 하기 위해서 함수 사용
def stu_print():
    for s in stu:
        print("{},{},{},{},{}".format(*s))

stu = [
    [1,"홍길동",100,100,100],
    [2,"유관순",100,100,100],
    [3,"이순신",100,100,100],
]

while True:
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("3. 학생성적검색")
    choice = int(input("원하는 번호를 입력하세요.>> "))
    if choice == 1:
        name = input("이름을 입력하세요.")
        # 학생전체출력
        stu_print()
        
    elif choice == 2:
        # 학생출력하는 구문
        print("번호\t이름\t국어\t영어\t수학")
        # 학생전체출력
        # 학생전체출력
        stu_print()
        # for s in stu:
        #     print("{},{},{},{},{}".format(*s))
    else:        
        name = input("이름을 입력하세요.")
        # 학생전체출력
        # 학생전체출력
        stu_print()
        # for s in stu:
        #     print("{},{},{},{},{}".format(*s))





# def cal():
#     num1 = int(input("숫자입력 : "))
#     num2 = int(input("숫자입력 : "))
#     print(num1+num2)
#     print(num1-num2)
#     print(num1*num2)
#     print(num1/num2)

# cal()
# cal()
# cal()



# def fun():
#     print("함수를 호출합니다.")

# fun() 
# fun() 
# fun()  
