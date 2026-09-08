class Student:
    total = 0
    avg = 0

    # 생성자
    def __init__(self,no,name,kor,eng,math):
        # self.__no = no # 캡슐화 : 클래스 내부에서만 값을 수정가능
        # 캡슐화시 값을 수정할수 있도록, setter,getter를 만들어줌.
        self.no = no
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = kor+eng+math
        self.avg = self.total/3
        # self.rank = 0

    def __str__(self):
        return f"{self.no}\t{self.name}\t{self.kor}\t{self.eng}\t{self.math}\t{self.total}\t{self.avg:.2f}"    

    def cal_total(self):
        self.total = self.kor+self.eng+self.math

    def cal_avg(self):
        self.avg = self.total/3    

# 객체선언을 하면
# s1 = Student()   # s -> 3개변수가 생성됨. 
# no=1
# name = "홍길동"
# total = 50 
# 객체선언시 바로 값 입력
s1 = Student(1,"홍길동",90,90,100)
s2 = Student(2,"유관순",100,100,99)

# 출력 : 참조변수명.변수명
print(s1.name)
# 수정 : 참조변수명.변수명 = 수정값
s1.name="홍길자"
print(s1.name)
# 추가 : 참조변수명.변수명 : 없는 변수 입력시 추가
s1.rank = 1
print(s1.rank)

stuList = []
# 전체출력
print(s1)
print(s2)
stuList.append(s1)
stuList.append(s2)
# stu.add(s1)

# 수정
s1.kor = 10
s1.total = s1.kor+s1.eng+s1.math
s1.cal_total()
s2.cal_total()
s1.avg = s1.total/3
s1.cal_avg()
print(s1)