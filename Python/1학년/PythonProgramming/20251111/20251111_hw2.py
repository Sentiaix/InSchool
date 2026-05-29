'''문제2
존재하는 파일 경로가 입력될 때까지 입력 요구하는 코드 작성해서 파일 open후 파일 내용 출력.
'''

import os
cwd = os.getcwd()
cwd = cwd + '/Python, etc/Python/2학기/PythonProgramming/20251111'

# Enter this
# vvvvvvvvv
# C:\Users\samsung\.vscode\Code\Python, etc\Python\2학기\PythonProgramming\20251111\hello.txt
while True:
    s = input('Enter the file path: ')
    try:
        f = open(s, 'r')
        content = f.read()
        print(content)
        f.close()
        break
    except FileNotFoundError:
        print("File not found. Try again.")