'''산수 계산 str을 입력 받아 +, -, *, /계산 값을 출력 하라.
 
입출력 예시 1:
Enter equation: 89-56
33.0
 
입출력 예시 2:
Enter equation: 5*7
35.0
 
입출력 예시 3:
Enter equation: 4*-3
-12.0
 
입출력 예시 4:
Enter equation: -4.5--63
58.5'''

# input값에는 공백이 존재하거나 연산자가 존재하지 않는 경우는 없음.
Eq = input("Enter equation: ")

# 연산자 후보
ops = ['+', '-', '*', '/']

# 맨 앞 부호는 건너뛰고, 그 뒤부터 첫 연산자 찾기
op_idx = -1
op = '' # oprator는 문자열 형식임
for i in range(1, len(Eq)): # 어차피 맨 앞은 부호이거나 숫자임. 따라서 idx는 1부터 시작
    if Eq[i] in ops:
        op_idx = i
        op = Eq[i]
        break

# print(f"Operator: {op}, Index: {op_idx}") # debug print

# 숫자 부분 자르기
n1 = float(Eq[:op_idx])
n2 = float(Eq[op_idx+1:]) # Eq[op_idx]로 쓰면 연산자까지 들어감. 따라서 +1 필요

# 계산
if op == '+':
    res = n1 + n2
elif op == '-':
    res = n1 - n2
elif op == '*':
    res = n1 * n2
elif op == '/':
    res = n1 / n2

print(res)