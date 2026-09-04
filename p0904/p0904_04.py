# 파일 읽어오기
f = open("C:/aaa/test1.txt","r",encoding="utf-8")
while True:
    line = f.readline()
    if not line: break
    print(line,end="")
f.close()
