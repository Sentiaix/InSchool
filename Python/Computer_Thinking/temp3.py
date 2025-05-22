# def plus(v1,v2): #python3 def needs colon
#     result = 0
#     result = v1 + v2
#     return result

# hap = plus(100, 200)
# print(f"{hap}")

# a = 20

# def test():
#     a = 10
#     print(f"test()에서 a의 값 {a}")

# def test2():
#     print(f"test2()에서 a의 값 {a}")

# test()
# test2()

def factorial(v1):
    start_val = v1
    if(v1 == 1):
        return 1
    return v1 * factorial(v1 - 1)

print(f"factorial is {factorial(int(input("get number: ")))}")