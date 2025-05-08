print(1+2) #3
print(5-2) #3
print(2*3) #6
print(8/2) #4

#제곱
print(3**3) #27

#나머지
print(5%3) #2
print(10%3) #1
#몫
print(5//2) #2
print(10//3) #3

print( 5 > 11 ) #False
print( 3>= 3 ) #True
print( 3 < 10 ) #true
print( 5 <= 5 ) #true

print(3 == 3) #True
print( 4 == 2) #False
print(3 + 4 == 7) #True
print( 1 != 3) #True
print(not (1 == 3)) #True
print(not (1 != 3)) #False

#and gate, or gate
print((3 > 0) and (3<5)) #True
print((3 > 0) & (3 < 5)) #True &=and

print((3 > 0 ) or (3 > 5)) #True
print((3 > 0 ) | (3 > 5)) #True |(shift+\) = or

print(5 > 4 > 3) #True
print(5 > 4 > 7) #False

#간단한 수식
print(2 + 3 * 4) # 14
print((2 + 3 ) * 4) # 24
number = 2 + 3 * 4 # 14
print(number) # 14
number = number + 2 # 16
print(number)  #16
number += 2 # 18, 열 43번과 같은 형식
print(number)
number *= 2 # 18 * 2 = 36
print(number)
number /= 2 # 36 / 2 = 18
print(number)
number -= 2 # 18 - 2 = 16
print(number)
number %= 5 # 1 (나머지) 16 % 5
print(number)
number //= 3 # 0 (몫) 1 // 3
print(number)