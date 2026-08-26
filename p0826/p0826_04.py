# 잔액 : 1000 고정
# 송금금액 : 100 입력
# 총금액을 출력하시오.

# 출력되도록 하시오.
# 잔액 : 1000
# 송금금액 : 100
# 총금액 : 1100

total1 = 1000
send = int(input("송금금액을 입력하세요."))
total2 = total1+send

print("잔액 : ",total1)
print("송금금액 : ",send)
print("총금액 : ",total2)
print("잔액 : {}, 송금금액 : {}, 총금액 : {}".format(total1,send,total2))
