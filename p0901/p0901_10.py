# 숫자형-정수타입,실수타입, 문자열타입, 불타입
# 리스트,튜플,딕셔너리
# aa = [1,2,3,4,5]  # 리스트             aa[0]
# aa2 = (1,2,3,4,5) # 튜플 - 수정이 안됨. aa2[0]
# aa3 = {"key":"value",}          # 딕셔너리
  
import random
n_shape = ["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]
number = [1,2,3,4,5,6,7,8,9,10,11,12,13]
shape = ["SPADE","HEART","DIAMOND","CLOVER"]

# [ ["SPADE",1],["SPADE",2] ...]
card = [] 
# card 52개의 리스트를 생성하시오.
for s in shape:
    for n in number:
        card.append([s,n])

random.shuffle(card)
print(card)

        


# 아래와 같이 출력하시오.
# for s in shape:
#     for n in number:
#         print("{},{}".format(s,n_shape[n-1]))


# SPADE,1
# SPADE,2 .....
#..
# CLOVER,13