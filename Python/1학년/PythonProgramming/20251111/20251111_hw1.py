'''문제 1.
float을 입력 받을 때까지 입력 요구하는 코드를 except을 사용해서 작성.'''

while True:
    s = input('Enter the value: ')
    try:
        n = float(s)
        break
    except:
        print("Error. Try again")

# print(n) # debug print