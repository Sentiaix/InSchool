'''str을 입력받아 숫자 비교 연산자 >, <, >=, <=, ==, != 결과를 출력하라...

 
입출력 예시 1:
Enter inequality: 12>12.0
False
 
입출력 예시 2:
Enter inequality: 12.0>=12
True
 
입출력 예시 3:
Enter inequality: -41<12
True
 
입출력 예시 4:
Enter inequality:  5!=+5
False'''

s = input("Enter inequality: ")
# print(s)
 
ops = ['>', '=', '<', '!']
op = ''
num1 = num2 = 0
 
for i in range (1, len(s)): # 0번째는 어차피 숫자임.
    if s[i] in ops:
        if s[i+1] == '=':
            op = s[i:i+2]
            num1 = float(s[:i])
            num2 = float(s[i + 2:])
        else :
            op = s[i]
            num1 = float(s[:i]) # i번째 수 직전까지 float로 저장
            num2 = float(s[i + 1:]) # i+1번째 수 부터 끝까지 float로 저장
        break
 
print(i, num1, num2, op) # debuggin print

 
if op == '>=':
    print(num1 >= num2)
elif op == '>':
    print(num1 > num2)
elif op == '=':
    print(num1 == num2)
elif op == '<':
    print(num1 < num2)
elif op == '<=':
    print(num1 <= num2)
elif op == '!=':
    print(num1 != num2)
else :    print("Syntax Error")
