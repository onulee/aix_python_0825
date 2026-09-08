class Students:
    slist = []

    def add(self,s):
        self.slist.append(s)

    def print(self):
        print()
        print(" "*25,end="")
        print("[ 학생성적출력 ]")
        print("-"*70)
        print("번호","이름","국어","영어","수학","합계","평균","등수",sep="\t")      
        print("-"*70)
        for s in self.slist:
            print(s)

