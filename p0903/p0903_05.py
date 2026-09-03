my_info = {"id":"aaa","pw":"1111","name":"홍길동","money":10000000}

s_arr = [
    {"prd_name":"컴퓨터","price":1000000},
    {"prd_name":"냉장고","price":2000000},
    {"prd_name":"오디오","price":500000},
    {"prd_name":"세탁기","price":1500000}
    ] # 1-0,2-1,3-2

def p_cal(choice):
    if my_info['money']<s_arr[choice-1]['price']:
        print("보유금액이 부족합니다. 머니충전을 한후 구매하세요.")
        return
    print(f"구매상품 : {s_arr[choice-1]['prd_name']}")
    print(f"가격 : {s_arr[choice-1]['price']:,} 원")
    # 계산하는 부분
    my_info['money'] -= s_arr[choice-1]['price']
    print(f"상품구매후 보유금액 : {my_info['money']:,}원")

while True:  #{"prd_name":"컴퓨터","price":1000000}
    for i,v in enumerate(s_arr): # (0,"컴퓨터"),(1,"냉장고")
        print(f"{i+1}. {v['prd_name']} : {v['price']:,} 원")
   
    choice = int(input("원하는 번호를 입력하세요.>> "))
    if choice == 1:   # 컴퓨터 - 1000000
        p_cal(choice)
    elif choice == 2: # 냉장고 - 2000000
        p_cal(choice)
    elif choice == 3: # 오디오 - 500000
        p_cal(choice)
    elif choice == 4: # 세탁기 - 1500000
        p_cal(choice)

        


