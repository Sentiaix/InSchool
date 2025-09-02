a = int(input())

# 오름차순 별
for i in range(1, a + 1):
    print("*" * i)

# 내림차순 별
for i in range(a, 0, -1):
    print("*" * (i-1))