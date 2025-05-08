a = int(input())

for i in range(1, a + 1):
    print("*" * i)

for i in range(a-1, 0, -1):
    print("*" * i)

while True:
    dan = int(input("단을 입력하세요: "))
    gop = int(input("곱을 입력하세요: "))

    if(dan<0 or gop<0):
        print("**************************음수는 안됩니다********************")
        continue

    print(f"{dan} X {gop} = {dan*gop}")

    if dan == 0 and gop == 0:
        print(f"{dan},{gop}을 입력하셨으므로 종료합니다.")
        break

