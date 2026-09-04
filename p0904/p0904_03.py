# # # 예외처리 try - except

choice = int(input("원하는 번호입력 : "))
if choice == 1:
    print("학생성적입력부분")
elif choice == 2:
    print("출력")
elif choice == 3:
    print("수정")
elif choice == 4:
    raise NotImplementedError   # 프로그램구현안된부분 확인         




# print(1)
# try:
#     print(2)
#     print(3)
#     print(10/0) #에러가남.
#     print(4)
# except Exception as e:
#     print(e)
#     print(type(e))    
#     print(5)
#     print(6)
# print(7)





# # pront(1)  #구문오류

# # 런타임에러
# arr = [1,2,3,4,5]
# while True:
#     choice = int(input("0-4까지 숫자입력 : "))
#     if choice.isdigit():
#         choice = int(choice)
#     else:
#         print("숫자만 입력이 가능합니다. 다시 입력하세요.")
#         continue    
#     print("선택값 : ",arr[choice])
    # try:
    #     choice = int(input("0-4까지 숫자입력 : "))
    #     print("선택값 : ",arr[choice])
    # except Exception as e:
    #     print("에러가 났습니다.")
    #     print(e)