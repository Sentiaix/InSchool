'''
강의 노트 + 강의 문제
 
문제 1. 입력 매개 변수를 합하는 함수를 아래 사용 코드를 보고 구현 하시오.
print('합', mysum(1,2,3,4))
print('합', mysum(45, 3))
print('합', mysum(num1=6, num2=25, num3= 2))
 
문제2. 재규 호출과 Global 변수를 사용해서 영문자, 숫자, 스페이스만 가져오는 함수 구현 하시오. 아래 사용 코드와 입출력 참고해서 구현.
str = input('Enter: ')
outstr = ''
text_num(str)
print(outstr)
 
입출력 예시:
Enter: Somthing happend? 478 times !!!?
Somthing happend 478 times
'''

# 문제 1.
def your_sum(*args, **kwargs): # *_ < n개의 매개변수를 알아서 받고 tuple로 묶음, **_ << num1=6 같은 자료형을 'num1' : 6 이런식으로 묶어줌
    total = 0
    for num in args:
        total += num
    for num in kwargs.values():
        total += num
    return total

print('합', your_sum(1,2,3,4))
print('합', your_sum(45, 3))
print('합', your_sum(num1=6, num2=25, num3= 2))

# 문제 2.
str_input = input('Enter: ')
outstr = ''
def text_num(s):
    global outstr
    if s == '':
        return
    if s[0].isalpha() or s[0].isdigit() or s[0].isspace(): # 알파벳, 스페이스바, 숫자 중 하나 인 경우
        outstr += s[0] # outstr에 저장
    text_num(s[1:]) # 다음 글자부터 확인하도록 슬라이싱

text_num(str_input)
print(outstr)