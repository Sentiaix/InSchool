
animal = "고양이"
name = "호섭"
age = 2
hobby = "말하기"


age = int(input("당신의 고양이는 몇살인가요? "))
is_adult = age >= 3

print("우리집 " + animal +"의 이름이 " + name + "입니다")
#print("" + name + "이는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요.")
print("", name, "이는 ", age, "살이며, ", hobby, "을 아주 좋아해요.")
# print("" + name + "이는 어른일까요? " + str(is_adult) + "")
print(name+ "이는 어른일까요? " + str(is_adult) + "")
# print(name, "이는 어른일까요? " + str(is_adult) + "")