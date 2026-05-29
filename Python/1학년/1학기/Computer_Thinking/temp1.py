"""
a = int(input("정수 a를 입력해주세요: "))
b = int(input("정수 b를 입력해주세요: "))
 
print(a+b, a-b, a*b, a/b, a//b, a%b, a**b) # a//b는 소수부 떼고 계산

print(a&b)

num = int(input("정수를 입력하시오: "))
if num % 2 == 0 : 
    print("짝수입니다")
else :
    print("홀수입니다")

if a and b and num :
    print("a와 b와 num은 모두 참이다")
else :
    print("a 또는 b 또는 num 중 하나는 거짓이다")
"""

a = 0
print((a>100) and (a<1000))

for i in range(100): #range (시작값, 끝값+1, 증가값)
    print(i)


for i in range(2, -1, -1):
    print("%d: test for lang" % i)

for i in range(3):
    print("%d " % i, end=" ")
    #end="" 는 프린트가 끝나고 다음 문자를 ~로 출력하라 라는 구문


