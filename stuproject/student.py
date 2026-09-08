class Student:
    # 생성자 
    def __init__(self,*args):
        if len(args) == 5:    # 학생성적입력에서 객체 넣기
            self.no = args[0]   #no
            self.name = args[1] #name
            self.kor = args[2]  #kor
            self.eng = args[3]  #eng
            self.math = args[4] #math
            self.total = self.kor+self.eng+self.math
            self.avg = self.total/3
            self.rank = 0
        elif len(args) == 8:   # stu.txt파일에서 객체 넣기
            self.no = args[0]   #no
            self.name = args[1] #name
            self.kor = args[2]  #kor
            self.eng = args[3]  #eng
            self.math = args[4] #math
            self.total = args[5]
            self.avg = args[6]
            self.rank = args[7]  

    # 문자열함수
    def __str__(self):
        return f"{self.no}\t{self.name}\t{self.kor}\t{self.eng}\t{self.math}\t{self.total}\t{self.avg:.2f}\t{self.rank}"    

    # 합계
    def s_total(self):
        self.total = self.kor+self.eng+self.math

    def s_avg(self):
        self.avg = self.total/3 

    def s_str(self):
        return f"{self.no},{self.name},{self.kor},{self.eng},{self.math},{self.total},{self.avg:.2f},{self.rank}"           

