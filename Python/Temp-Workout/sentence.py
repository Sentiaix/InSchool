sentence = '나는 소년입니다.'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence3)


# 슬라이싱

jumin = "990120-1234567" 

print("성별 :" +jumin[7])
print("연 : " +jumin[0:2]) #[a:b] a부터 b직전까지.
print("월 : " +jumin[3:5])
print("일 : " +jumin[4:6])
print("생년월일 : " +jumin[:6]) # = print("생년월일 : " +jumin[0:6])
print("뒤 7자리 : " +jumin[7:])
print("뒤 7자리 역순 : " +jumin[-7:])

#문자열 처리함수

python = "Python is Amazing"

print(python.lower())
print(python.upper())
print(python[0].isupper()) #python 변수의 첫 글자가 대문자인가?
print(len(python))
print(python.replace("Python", "Java"))

index = python.index("n")
print(index)
index = python.index("n", index + 1) #두 번째 n 확인
print(index)

print(python.find("n")) #n 순차적으로 찾기

print(python.find("Java"))
#print(python.index("Java")) > 오류 발생

print(python.count("n"))