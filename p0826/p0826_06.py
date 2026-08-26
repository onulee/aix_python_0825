# 관계연산자 ==,!=,>,<,>=,<=
# True, False bool타입으로 반환


# 프로그램 종료
# 대문자 x 또는 X 를 입력하면 종료
str1 = input("프로그램을 종료하려면 x 또는 X를 입력하세요.>>")
if(str1=="x") or (str1=="X"):
    print("프로그램이 종료되었습니다.")
else:
    print("프로그램을 계속실행합니다.")
        



# 아이디,패스워드를 입력받아 맞는지 확인
# 아이디 : aaa, 패스워드 : 1111
# id = input("아이디를 입력하세요.>> ")
# pw = input("패스워드를 입력하세요.>> ")
# if (id=="aaa") and (pw=="1111"):
#     print("로그인이 되었습니다. 메인페이지로 이동합니다")
# else:
#     print("아이디 또는 패스워드가 일치하지 않습니다.")    

# a = 10
# b = 5
# print(a==b) # False
# print(a!=b) # True
# print(a>b)  # True
# print(a<b)  # False



# 산술연산자 : +,-,*,/,//,%,**

# money = 12340
# # 12340 -> 500원 동전 몇개? 340원 100동전 몇개? 40원 10동전 몇개?
# # 12340원 500원 동전: ?, 100원 동전 : ?, 10원 : ?

# result = money//500
# num = money%500
# print(result,num)
# result2 = num//100
# num2 = num%100
# result3 = num2//10
# print(result,result2,result3)


# # 1270원 
# # >> 500원 2개, 100원 2,10원 7개




# # 500원 동전 몇개가 필요할까요?
# # result = money//500
# # print("500동전 필요개수 : ",result)
# # result2 = money//100
# # print("100동전 필요개수 : ",result2)