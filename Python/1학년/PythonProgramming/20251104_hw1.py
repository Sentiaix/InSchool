import random

rand_int = [random.randint(1, 100) for _ in range(20)]
print("raw list:", rand_int)

# 홀수만 뽑기
def only_odd(a):
    odd_list = []

    for i in range(len(a)):
        if a[i] % 2 == 1 :
            odd_list.append(a[i])

    odd_list.sort()

    return odd_list


# 소수만 뽑기
def only_prime(a):
    prim_list = []
    prime_number = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

    for i in range(len(a)):
        if a[i] in prime_number:
            prim_list.append(a[i])

    prim_list.sort()
    
    return prim_list

# 짝수만 앞에, 홀수만 뒤에
def pair_odd(a):
    pair_list = []
    odd_list = []

    for i in range(len(a)):
        if a[i] % 2 : # 나눴는데 나머지 있으면 1, 홀수
            odd_list.append(a[i])
        else :
            pair_list.append(a[i])

    pair_list.sort()
    odd_list.sort()
    
    return pair_list + odd_list

print("odd nums:", only_odd(rand_int))
print("primes  :", only_prime(rand_int))
print("pair-odd:", pair_odd(rand_int))