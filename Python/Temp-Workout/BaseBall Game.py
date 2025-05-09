# Baseball Game enhanced Version
# 넣고싶은거: 1. (O) 4개 숫자(기회 20번) 2. 타이머 (원하는대로 작동하지 않음)

import random # random number를 pulling 하기 위해 사용
secretLen = 4 # 무작위 숫자의 길이는 3 >> 4임

secretList = random.sample(range(10), secretLen)
        # 0-9 중 3 >> 4개 랜덤 선택
secret = '' # secret이라는 빈 문자열 변수 생성
for i in range(secretLen):
    secret += str(secretList[i])
    # int값인 secretList의 [0],[1],...[secretLen - 1]값을 str형으로 각각 변환해 추가함

# print(secret) #테스트용

#for {var} in range(start num, end num + 1, increase num):
for chance in range(20, 0, -1): # 10 >> 20번의 기회

    ## 추론 숫자가 올바르게 입력됐는지 검사
    while True:
        guess = input(f"You have {chance} chance(s). Guess my three-digit number: ")
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
        else: # ball이 0이면
            print(f"{strike} strike(s)\n")
    else: # strike가 0이면
        if ball > 0:
            print(f"{ball} ball(s)\n")
        else: # strike ball 모두 0이면
            print("Out\n")
else: ### For문에 대한 else.
    print('You failed to guess my number..')