'''4개의 정수를 입력받아... list나 배열 datatype은 사용 금지이다.
1. 홀수와 짝수를 따로 나누어서 출력하라.
2. 홀수는 큰수부터 정렬해서 출력, 짝수는 작은수부터 정렬해서 출력 하라

 
입출력 예시 1:
enter 4 numbers: 8
enter 4 numbers: 3
enter 4 numbers: 4
enter 4 numbers: 5
홀수 3 5
짝수 8 4
정렬 홀수 5 3
정렬 짝수 4 8
 
입출력 예시 2:
enter 4 numbers: 1
enter 4 numbers: 3
enter 4 numbers: 7
enter 4 numbers: 5
홀수 1 3 7 5
짝수 
정렬 홀수 7 5 3 1
정렬 짝수 '''

n1 = int(input("enter 4 numbers: "))
n2 = int(input("enter 4 numbers: "))
n3 = int(input("enter 4 numbers: "))
n4 = int(input("enter 4 numbers: "))

# 이거 없으면 변수호출없다고 에러뜸
o1 = o2 = o3 = o4 = None
p1 = p2 = p3 = p4 = None
 
odds = "홀수 "
pairs = "짝수 "

# 짝수 홀수 구분
if n1 % 2: #홀수면 2로 나눌때 1(True), 짝수면 나머지 0(False) 이용
    odds += str(n1) + " "
    o1 = n1
else:
    pairs += str(n1) + " "
    p1 = n1

if n2 % 2:
    odds += str(n2) + " "
    o2 = n2
else:
    pairs += str(n2) + " "
    p2 = n2

if n3 % 2:
    odds += str(n3) + " "
    o3 = n3
else:
    pairs += str(n3) + " "
    p3 = n3

if n4 % 2:
    odds += str(n4) + " "
    o4 = n4
else:
    pairs += str(n4) + " "
    p4 = n4


print(odds)
print(pairs)

# 순차정렬
print("정렬 홀수", end=" ")
for _ in range(4):
    m = None
    # in + range() 말고 in (변수1, 변수2...) 로 사용하면 for함수가 순서대로 변수를 꺼내서 사용함
    for x in (o1, o2, o3, o4): # 여기 돌리면 가장 큰 값을 m에 넣음
        if x is not None: # x값이 존재하는 경우만 판독
            if m is None or x > m : # m값이 없는 case도 추가해 오류 방지
                m = x
    if m is not None: # 만약 m값이 존재한다면 성공적으로 m(ax)값을 골라낸 것임
        print(m, end=" ")
        # o1, ..., o4중에서 최댓값으로 발탁된 값은 None으로 교체함. (if oN == m >> oN = None)
        if o1 == m: o1 = None
        elif o2 == m: o2 = None
        elif o3 == m: o3 = None
        elif o4 == m: o4 = None
print()

print("정렬 짝수", end=" ")
for _ in range(4):
    m = None
    for x in (p1, p2, p3, p4):
        if x is not None:
            if m is None or x < m : # Odd 파트랑 다르게 여긴 최솟값 찾기
                m = x
    if m is not None:
        print(m, end=" ")
        # p1, p2, p3, p4중에서 최솟값으로 발탁된 pN은 None으로 바꿔버려서 제거함
        if p1 == m: p1 = None
        elif p2 == m: p2 = None
        elif p3 == m: p3 = None
        elif p4 == m: p4 = None
print()