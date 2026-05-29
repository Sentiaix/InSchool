'''소문자로 one plus two 같은 str을 입력 받아 계산 값을 출력하라.
사용 가능한 숫자는: zero one two three four five six seven eight nine
사용 가능한 연산자는: plus minus multiply divide
입출력 예시: three minus one
2
입출력 예시: three plus nine
12
입출력 예시: nine divide three
3.0
입출력 예시: three multiply five
15'''

s = input("Enter equation: ").strip() # .strip() << 앞뒤 공백 제거
parts = s.split()  # split()을 이용해 list식으로 packaging처리. 공백 기준으로 쪼개짐. 예) three    plus  five >> ['three', 'plus', 'five']

Snum1, op, Snum2 = parts # unpacking
num1 = num2 = 0

numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
# ops = ['plus', 'minus', 'multiply', 'divide'] # split()을 이용했으므로 ops는 필요 없음

""" split()을 이용하지 않는 방법 근데 정확하지도 않고.. space가 2번 연속 나오는 경우도 고려해야 함
for i in range(len(s)): # 첫 숫자 | 연산자+숫자를 나머지로 버림
    if s[i] == ' ': #공백 나오면
        for _ in range(len(s)): # 공백이 2번 연속 나오는 경우 건너뛰기
            if s[i + 1] == ' ':
                i += 1
                continue
            else:
                break
        Snum1 = s[:i]
        rest = s[i+1:]
        break
for j in range(len(rest)): # 버렸던 나머지를 연산자 | 숫자로 나눔
    if rest[j] == ' ':
        for _ in range(len(rest)): # 공백이 2번 연속 나오는 경우 건너뛰기
            if s[j + 1] == ' ':
                j += 1
                continue
            else:
                break
        op = rest[:j]
        Snum2 = rest[j+1:]
        break
"""

# print(f"First num:{Snum1}, Second num:{Snum2}, Op:{op}") # debbugin print

# numbers.index는 그 숫자의 index를 불러온다. 따라서 zero의 index는 0. 잘 대응하므로 문제 없음
if Snum1 in numbers:
    num1 = numbers.index(Snum1)
if Snum2 in numbers:
    num2 = numbers.index(Snum2)

if op == 'plus':
    res = num1 + num2
elif op == 'minus':
    res = num1 - num2
elif op == 'multiply':
    res = num1 * num2
elif op == 'divide':
    res = num1 / num2
else:
    res = "Syntax Error"

print(res)