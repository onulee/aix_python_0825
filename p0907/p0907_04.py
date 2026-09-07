m_str = '"서울특별시  (1100000000)","9,330,658","4,482,949","          2.08","4,504,432","4,826,226","          0.93"'
test = m_str.split('","')
for i,t in enumerate(test):
    t = t.replace('"','')
    t = t.replace(',','')
    t = t.replace('\xa0','')
    t = t.replace('\u200b','')
    t = t.replace('\ufeff','')
    t = t.strip()
    if t.isdigit():
        t = float(t)
        test[i] = t
    print(type(t))
print(test)
#------------------
# 서울 전체인구에서 남성비율은 몇%인가? 출력하시오.
print("서울총인구 남성비율 : {:.2f} %".format(test[4]/test[1]*100))
print("서울총인구 여성비율 : {:.2f} %".format(test[5]/test[1]*100))