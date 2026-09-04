# 파일 읽어오기
stu = []
f = open("C:/aaa/test2.txt","r",encoding="utf-8")
while True:
    line = f.readline() # /n 줄바꿈때문에 에러가 남.
    if line=="": break
    line = line.strip()

    print(line,end="")
    arr = line.split(",")

    for i,a in enumerate(arr):
        if 5>=i>=2:
            arr[i] = int(a)
        elif i==6:
            arr[i] = float(a)    
    # stu 리스트에 저장
    # print(arr)
    stu.append({'no':arr[0],'name':arr[1],'kor':arr[2],'eng':arr[3],'math':arr[4],'total':arr[5],'avg':arr[6]})
      
    
f.close()
print(stu)

