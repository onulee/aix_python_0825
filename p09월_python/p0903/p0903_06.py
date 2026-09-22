s_arr = [
    {"prd_name":"컴퓨터","price":1000000},
    {"prd_name":"냉장고","price":2000000},
    {"prd_name":"오디오","price":500000},
    {"prd_name":"세탁기","price":1500000}
    ] # 1-0,2-1,3-2

print("1.컴퓨터-1000000")
print("2.냉장고")
print("3.오디오")
print("4.세탁기")
choice = int(input("원하는 번호입력 : "))
if choice == 1:
    print("컴퓨터")
elif choice == 2:
    print("냉장고")
elif choice == 3:
    print("오디오")
elif choice == 4:
    print("세탁기")


