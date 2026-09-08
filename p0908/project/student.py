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