# Baseball Game enhanced Version
# 넣고싶은거: 1. (O) 4개 숫자(기회 20번) 2. 타이머 (원하는대로 작동하지 않음)
# 3. 소리 출력기능 추가하기 4. 하도 못하면 한글자씩 알려주기(앞부터)

import random # random number를 pulling 하기 위해 사용
import winsound as sd # beepsound를 출력하기 위함

def high_beep(): # 높은 beep
    fr = 10000    # range : 37 ~ 32767
    du = 1000     # 1000 ms ==1second
    sd.Beep(fr, du) # winsound.Beep(frequency, duration)

def low_beep(): # 낮은 beep
    fr_l = 2000
    du_l = 1000
    sd.Beep(fr_l, du_l)

def low_long_beep(): # 낮고 느린 beep
    fr_ll = 2000
    du_ll = 3000
    sd.Beep(fr_ll, du_ll)

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
        guess = input(f"You have {chance} chance(s). Guess my three-digit number: ", end='')
        if chance <= 40: # 기회가 40부터 10씩 줄어들때마다 한글자씩 추가로 공개
            print("Hint!: ")
            print(f"{secretList[0]}", end='')
            if chance <= 30:
                print(f"{secretList[1]}", end='')
                if chance <= 20:
                    print(f"{secretList[2]}", end='')
                    if chance <= 10:
                        print(f"{secretList[3]}", end='')
        print("\n")

        if len(guess) ==  secretLen and guess.isdigit():
            break

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
            low_beep()
        else: # ball이 0이면
            print(f"{strike} strike(s)\n")
            high_beep()
    else: # strike가 0이면
        if ball > 0:
            print(f"{ball} ball(s)\n")
            low_beep()
        else: # strike ball 모두 0이면
            print("Out\n")
            low_long_beep()
else: ### For문에 대한 else.
    print('You failed to guess my number..')
    print(f"{secret}")