def ch_list(a): # a == b
    a[0] += 888

def ch_immut(a):
    a += 888

b = [1,2,3]
print(b)
ch_list(b)
print(b)

c = 2
print('immutable', c)
ch_immut(c)
print('immutable', c)

# 함수 len()
# len() 함수는 길이를 (unsigned) int 형태로 반환하며, string, list, tuple 등에 사용가능하다
a = [1,2,3]
len(a)
s = 'string'
len(s)
t = (1,2,3,4)
len(t)

a.append(15) # list 뒤에 특정 값을 추가한다
a.clear() # list 비우기

a = [1,2,222,3,126]
b = a.copy() # 원래 list는 다른 변수에 대입하면 reference를 copy한다. 하지만 값만 복사하고자 하면 .copy()를 사용하자
print(a, b)
b[0] += 123
print(a, b)

a.count(3) # () 속 대상의 갯수를 세어서 반환한다
a.extend([17,18,19]) # append는 한 개씩 추가한다면, .extend는 list로 묶어 한 번에 값을 넣는다
print(a)

a.index(2) # () 속 대상의 위치를 세어거 반환한다. (슬라이싱 넣어서 가능)
print(a)
a.pop() # append와 반대로 뒤에서부터 값을 꺼내온다.
print(a)
a.pop(1) # 특정 index에서도 꺼내올 수 있다
print(a)

a.remove(222) # () 속 값을 제거한다. 대상이 여러개라면 index가 낮은 순서부터 제거한다.(앞에서부터)
print(a)
a.reverse() # 순서를 뒤집는다.
print(a)
a.sort() # 오름차순으로 정렬한다.
print(a)

c = [1,2,3]
d = [1,2,3,4]
print(c + d) # [1, 2, 3, 1, 2, 3, 4]
print(c * 3) # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# tuple
t = (1, 2, 3)
print(t + (3,5)) # (1, 2, 3, 3, 5) # 값이 수정 안될 뿐 확장은 된다.
print(t * 3) # (1, 2, 3, 1, 2, 3, 1, 2, 3)