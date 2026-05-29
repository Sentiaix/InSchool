print("a" + "b")
print("a", "b")

# 방법 1
print("나는 %d살입니다." % 20) #정수
print("나는 %s을 좋아해요" % "Python") #문장 (범용성 가장 좋음)
print("Apple 은 %c로 시작해요." % "A") #한 글자


# 방법 2
print("나는 {}살 입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간")) #format에서 파란이 0번, 빨강이 1번
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간")) # {0}은 0번 format을 호출.

# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요".format(age= 20, color= "빨간"))

# 방법 4
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요")

# 탈출문자 ##

print("백문이 불여일견\n지피지기 백전불태")

# 저는 "나도코딩"입니다.
print("저는 \"나도코딩\" 입니다.")
 
# \\ : 문장 내에서 \로 바뀜
print("C:\\Users\KSN\Desktop\\PythonWorkspace>")

# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine")

# \b : backspace (한 글자 지우기)
print("Redd\bApple")

# \t : tab(키보드)
print("Red\tApple")