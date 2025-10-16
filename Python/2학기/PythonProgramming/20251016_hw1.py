# 1+2+3+...+x 값을 반환하는 재귀함수 만들기

x = int(input("Enter the integer: "))

def sum(x):
    if x <= 1:
        return x
    else :
        return x + sum(x - 1)

print(f"sum(x): {sum(x)}")

# input이 3이면, "3+2+1"을 출력하는 plus 라는 이름의 재귀함수 만들기 (global 변수 사용)

#global 없어도 문제 풀이 가능

def plus(x):
    if x <= 1:
        return str(x)
    else :
        return str(x) + "+" + plus(x - 1)

print(f"plus(x): {plus(x)}")