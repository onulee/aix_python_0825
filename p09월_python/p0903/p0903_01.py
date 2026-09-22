# C,자바 : 컴파일러 언어 - 모든소스를 기계어로 번역후 프로그램진행
# 파이썬 : 스크립트 언어 - 한줄씩 기계어로 번역후 프로그램진행
# 함수사용이유 : 코드재사용, 코드 간결
def d_print():
    for i in range(1,11):
        print(i)

def hello_print():
    print("안녕하세요.")
    print("안녕하세요.")
    print("안녕하세요.")
    print("안녕하세요.")
    print("안녕하세요.")

def cal(n1,n2):   #shift+alt+방향키, alt+방향키
    r1 = n1+n2
    r2 = n1-n2
    r3 = n1*n2
    r4 = n1/n2
    return r1,r2,r3,r4 

n1 = int(input("숫자입력 : "))
n2 = int(input("숫자입력 : "))
r1,r2,r3,r4 = cal(n1,n2)
print(r1,r2,r3,r4)

