from random import *

url = "https://www.naver.com/"
my_url = url.replace("https://www.", "")
my_url = my_url[:my_url.index(".")]

password = my_url[:3] + str(len(my_url)) + str(my_url.count("e")) + "!"

print(" \"{0}\"의 비밀번호는 \"{1}\" 입니다".format(url, password))