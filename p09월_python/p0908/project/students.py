class Students:
    slist =[]

    def add(self,s):
        self.slist.append(s)  

    def print(self):
        print("번호","이름","국어","영어","수학","합계","평균",sep="\t")      
        print("-"*60)
        for s in self.slist:
            print(s)

