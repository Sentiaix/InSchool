'''mix 함수를 완성하라. 
mix함수는 string 2개를 입력 받아 2 string의 문자를 번갈아 가며 합한다. 
0번 문자는 s1[0], 1번 문자는 s2[0], 2번 문자는 s1[1], 3번 문자는 s2[1] … 식으로 합해지고, 
입력 string의 길이가 다르면, 더 긴 string의 나머지 부분을 그대로 합한다.
입출력 예시를 확인해서 반복문으로 구현하라. 
아래는 사용 코드와 mix함수의 일부분이 구현되어 있다. 
 
def mix( s1 , s2):
    #여기에 코드 작성해서 mix 함수 완료
    
s1 = input('enter 1st string: ')
s2 = input('enter 2nd string: ')
mixed_str = mix(s1, s2)
print(mixed_str)
 
입출력 예시 1:
enter 1st string: 123
enter 2nd string: ABCDEFG
1A2B3CDEFG
 
입출력 예시 2: 
enter 1st string: 0123456789
enter 2nd string: 0123456789
00112233445566778899
 
입출력 예시 3: 
enter 1st string: ABCDEFGHIJKLMNOPQRSTUVWXYZ
enter 2nd string: 12345
A1B2C3D4E5FGHIJKLMNOPQRSTUVWXYZ'''

def mix (s1, s2):
    result_str = '' # return할 문자열
    idx_1 = 0
    idx_2 = 0
    for i in range( len(s1) + len(s2) ):
        if idx_1 < len(s1): # i가 짝수인 경우 s1거부터
            result_str += s1[idx_1]
            idx_1 += 1
        if idx_2 < len(s2): # i가 홀수인 경우 s2부터
            result_str += s2[idx_2]
            idx_2 += 1
    return result_str

s1 = input('enter 1st string: ')
s2 = input('enter 2nd string: ')
mixed_str = mix(s1, s2)
print(mixed_str)