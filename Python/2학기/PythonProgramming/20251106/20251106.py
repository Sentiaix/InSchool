import os

cwd = os.getcwd()
print(cwd)
my_cwd = cwd + '/Python, etc/Python/2학기/Pythonprogramming/20251106/'

f = open(cwd + '/Python, etc/Python/2학기/Pythonprogramming/20251106/file.txt', 'w')
f.write('used / or \\\\ \n')
f.write(f"hello float {789.2}\n")
f.close

print("\n----------------read----------------")
f = open(my_cwd + "file.txt", "r")
s = f.read()
print(s)
f.close()

print('----------------readline----------------')
f = open(my_cwd + "file.txt")
s = f.readline()
print(s)
f.close()

print('----------------readline----------------')
f = open(my_cwd + "/file.txt", "r")
for i in f:
    print(i)
f.close()

print('----------------readlines----------------')
f = open(my_cwd + "file.txt")
s = f.readlines()
print(type(s))
for i in s:
    print(i, end='')
f.close()

print('----------------a for append----------------')
f = open(my_cwd + "file.txt", "a")
f.write("append more lines\n")
f.write("a for append")
f.close()
f = open(my_cwd + "file.txt", "r")
s = f.read()
print(s)
f.close()

print('----------------with open, no close----------------')
with open(my_cwd + "file.txt") as f:
    s = f.read()
    print(s)
print("Outside Of Open(...), file closed")