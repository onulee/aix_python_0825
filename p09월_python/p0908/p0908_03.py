class Student:
    # 생성자
    def __init__(self,no,name,kor,eng,math):
        self.__no = no
        self.__name = name
        self.__kor = kor  #캡슐화:클래스내부에서만 값을 수정
        self.__eng = eng
        self.__math = math
        self.__total = kor+eng+math
        self.__avg = (kor+eng+math)/3

    def __str__(self):
        return f"{self.__no}\t{self.__name}\t{self.__kor}\t{self.__eng}\t{self.__math}\t{self.__total}\t{self.__avg:.2f}"

    def get_kor(self):
        return self.__kor

    def set_kor(self,kor): # 캡슐화를 하면, 잘못된 값이 입력될때 에러처리
        if kor<0:
            print("잘못된 값이 들어옴.")
            return
        self.__kor = kor

    
    # 클래스 내 함수 매개변수 첫번째 self
    def cal_total(self):
        self.__total = self.__kor+self.__eng+self.__math

    def cal_avg(self):
        self.__avg = self.__total/3

    def print(self):
        print(self.__no,self.__name,self.__kor,self.__eng,self.__math,self.__total,f"{self.__avg:.2f}",sep="\t")           

stuList = []
# 객체선언
s = Student(1,"홍길동",100,100,99)   
print("-"*50)
print(s) 
print("-"*50)
s.__kor = 70    # 클래스 변수값 수정이 안됨(캡슐화)
s.__math = 40   # 클래스 변수값 수정이 안됨(캡슐화)
s.set_kor(-50)  # setter,getter를 사용해서 수정,확인을 해야 함.
s.cal_total()
s.cal_avg()
s.print()
print(s)


