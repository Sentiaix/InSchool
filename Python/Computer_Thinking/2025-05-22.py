# b = [3, 0, 1, 8, 7, 2, 5, 4, 6, 9]
# print(b)

# n = len(b)

# for i in range(len(b) -1, 0, -1) :
#     for j in range(0, i) :
#         if b[j] < b[j + 1] :
#             b[j], b[j + 1] = b[j + 1], b[j]

# print(b)

# ## 문자열 ascii 값이 더 큰 순서대로 정렬함.
# ## ex) hippo vs horse >> hippo, horse로 정렬됨( i < o )
# c = ["lion", "cat", "tiger", "iu", "animal", "pig", "man", "horse", "hippo"]
# print(c)

# n = len(c)

# for i in range(n-1) :
#     for j in range(n-1 -i) :
#         if c[j] > c[j + 1] :
#             c[j], c[j + 1] = c[j + 1], c[j]

# print(c)

import random
import time

def BubbleSort3(p):
    for i in range(len(p) - 1, 0, -1):
        # range(start, stop, step)
        # range(기본값 0, stop, 기본값 1)
        for j in range(0, i):
            if p[j] > p[j + 1]:
                p[j], p[j + 1] = p[j + 1], p[j]
    return p

b = random.sample(range(1, 20001), 20000)

print(b)

start = time.time()
BubbleSort3(b)

print(b)
print("time : ", time.time() - start)
