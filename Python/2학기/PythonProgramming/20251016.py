s = input("String: ")
# immutable type: (변경불가능 타입)
    # int, float, str
#   mutable type: (변경 가능 타입)
    # list

def len(x):
    return "redefined len()"

print("len(s)", len(s))
print("-----------------------------------------")


def change(a): # 값 자체가 매개변수로 들어간 것 처럼 작동
    a = 999

def change2(a): # []로 메모리 주소에 접근
    a[0] = 999

a = 888
change(a)
print("ummutable", type(a), a)
a = [888]
print("mutable", type(a), a)
change2(a)
print("mutable", type(a), a)


def info(s):
    legnth = len(s)
    return legnth, s[0], s[1]

a = info(s)
x, y, z= info(s)

print(type(a), a[0], a[1])
print(x, y, z)