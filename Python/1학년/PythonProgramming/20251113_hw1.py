'''Dictionary를 만드는 코드를 작성해보자.
Key와 Value를 입력한다.
Key 값이 ‘quit’이 아니면, dictionary에 추가 후, 다음 Key와 Value값을 입력 받는다.
Key 값이 ‘quit’이면 dictionary 추가를 끝내고 완성된 dictionary를 print한다.
Key나 Value 값이 float으로 변환 가능하면 float으로 변환해서 dictionary에 추가한다 (예외처리를 사용해보자).'''

# --- 과제 --- #

d = {}

while True:
    k, v= input('Enter the values(KEY,VALUE): ').split(',')
    if v == 'quit':
        break
    else:
        try:
            k = float(k)
        except:
            pass
        try:
            v = float(v)
        except:
            pass
        d[k] = v

print(d)