import os

cwd = os.getcwd()
cwd += '/Python, etc/Python/2학기/Pythonprogramming/20251106/'

f = open(cwd + "numbers.txt", "w")
f.write("""45
124
563
472
412
5
-58""")
f.close()

sum = 0 # 합

f = open(cwd + "numbers.txt", "r")
# s = f.read()
# print(s) # debug print
s = f.readlines()
for i in range(len(s)):
    sum += int(s[0])
print(sum)
f.close()