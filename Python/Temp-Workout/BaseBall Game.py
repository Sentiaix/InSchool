# Baseball Game enhanced Version
# 넣고싶은거: 1. 4개 숫자(기회 50번) 2. 타이머 (원하는대로 작동하지 않음)
# 3. 소리 출력기능 추가하기 4. 하도 못하면 한글자씩 알려주기(앞부터)

import random # random number를 pulling 하기 위해 사용
import winsound as sd # beepsound를 출력하기 위함

def beepsound(fr, du): # 높은 beep : 2500 / 낮은 beep : 1000
    sd.Beep(fr, du) # winsound.Beep(frequency, duration)

secretLen = 5 # 무작위 숫자의 길이는 3 >> 5임

secretList = random.sample(range(10), secretLen)
        # 0-9 중 3 >> 5개 랜덤 선택
secret = '' # secret이라는 빈 문자열 변수 생성
for i in range(secretLen):
    secret += str(secretList[i])
    # int값인 secretList의 [0],[1],...[secretLen - 1]값을 str형으로 각각 변환해 추가함

# print(secret) #테스트용

#for {var} in range(start num, end num + 1, increase num):
for chance in range(50, 0, -1): # 10 >> 50번의 기회

    ## 추론 숫자가 올바르게 입력됐는지 검사
    while True:
        guess = input(f"You have {chance} chance(s). Guess my three-digit number: ")
        if chance <= 40: # 기회가 40, 25, 10, 3회 남았을 때마다 한 글자씩 순차적으로 공개
            print("Hint!: ", end='')
            print(f"{secretList[0]}", end='')
            if chance <= 25:
                print(f"{secretList[1]}", end='')
                if chance <= 10:
                    print(f"{secretList[2]}", end='')
                    if chance <= 3:
                        print(f"{secretList[3]}", end='')
        print("\n")

        if len(guess) ==  secretLen and guess.isdigit():
            break
        else:
            print(f"Please type {secretLen} integer value!\n")

# print(guess) #테스트용

    ## 추론 숫자 분석
    strike = 0 #스트라이크 초기화
    ball = 0 #볼 초기화

    for i in range(secretLen):
        if secret[i] == guess[i]:
            strike += 1
        elif secret[i] in guess:
            ball += 1
    # print(secret, strike, ball) #테스트용

    ##분석 결과 출력
    if strike == secretLen:
        print("You guessed my number!!")
        break

    if strike > 0:
        if ball > 0:
            print(f"{strike} strike(s) and {ball} ball(s)\n")
            beepsound(2500, 250)
            beepsound(1000, 250)
        else: # ball이 0이면
            print(f"{strike} strike(s)\n")
            beepsound(2500, 500)
    else: # strike가 0이면
        if ball > 0:
            print(f"{ball} ball(s)\n")
            beepsound(1000, 500)
        else: # strike ball 모두 0이면
            print("Out\n")
            beepsound(1000, 1500)
else: ### For문에 대한 else.
    print('You failed to guess my number..')
    beepsound(2500, 250)
    beepsound(1000, 250)
    beepsound(500, 500)
    print(f"Answer is : >> {secret} <<\n")