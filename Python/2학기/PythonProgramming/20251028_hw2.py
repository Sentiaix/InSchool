'''영문 소문자, 대문자, 스페이스만 string을 입력 받아, 단어를 뒤에서부터 출력하는 reverse_words함수를 구현하라.
아래 활용 코드와 입출력 예시를 참고하여 반복문으로 구현하라.
s = input('Enter alphabets and space only: '
reverse_words(s)
 
입출력 예시 1:
Enter alphabets and space only: how do you do sir
sir do you do how
 
입출력 예시 2:
Enter alphabets and space only: foot foot wondering the world wondering
wondering world the wondering foot foot'''

def reverse_words (s):
    s = s.strip()
    lwords = s.split()
    # print(lwords) #debug print

    for i in range( len(lwords) // 2):
        temp = lwords[-i - 1]
        lwords[-i - 1] = lwords[i]
        lwords[i] = temp
    
    result = ''

    for i in range(len(lwords)):
        result += lwords[i] + ' '
    
    return result


s = input('Enter alphabets and space only: ')
rstr = reverse_words(s)
print(rstr)