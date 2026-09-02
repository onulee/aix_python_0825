import datetime
now = datetime.datetime.now()
print(now)
print(now.year)
print(now.month)
print("{:02d}월".format(now.month))
print("{:02d}초".format(now.second))
# 2026년8월27일 11시57분20초
print(now)
f_date = now.strftime("%Y년%m월%d일 %H시%M분%S초")
print(f_date)

print("{}년{}월{}일 {}시{}분{}초".format(\
    now.year,now.month,now.day,now.hour,\
    now.minute,now.second))

# 월 출력하는데, 1,2,3....9월 01월,02월03월,10월,11월,12월



# # format
# # 123 -> 5자리 빈공백 0으로 채워서 출력하시오.
# print("{:015,d}".format(123456789))
# print("{:02d}".format(12))