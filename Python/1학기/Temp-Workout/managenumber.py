print(abs(-3)) # 3 (abs=absoulte=절댓값)
print(pow(4, 2)) # 4^2 = 4*4 = 16
print(max(5, 12))  # 12
print(min(5, 12)) # 5
print(round(3.14)) # 3 반올림
print(round(4.9)) # 5 반올림

from math import *
print(floor(4.99)) # 내림. 4
print(ceil(3.14)) # 올림. 4
print(sqrt(16)) # 루트. 4

### 랜덤 함수 ###

from random import *

print(random()) # 0.0 ~ 1.0 미만의 임의의 함수 값
print(random() * 10) # 0.0 ~ 10.0 미만의 임의의 함수 값
print(int(random() * 10)) # 0 ~ 10 미만의 임의의 함수 값
print(int(random() * 10)) # 0 ~ 10 미만의 임의의 함수 값
print(int(random() * 10)) # 0 ~ 10 미만의 임의의 함수 값
print(int(random() * 10) + 1 ) # 1 ~ 10 이하의 임의의 함수 값

print(int(random() * 45 ) + 1) # 1 ~ 45 이하의 임의의 함수 값

print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값

print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값
# randit(a, b) a와 b 포함한 임의의 값