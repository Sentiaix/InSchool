# --- 필기 2 --- #
# dict part2

s = input('string: ')

d = {}

for c in s:
    if c in d:
        d[c] += 1 # n번째 알파벳에 값 추가
    else:
        d[c] = 1 # 요소 추가
print(d)

# key ' '을 SPACE로, \t을 TAB으로, \n을 NEWLINE으로 바꾸기
d2 = {}
for k in d.keys():
    if k == ' ':
        d2['SPACE'] = d[k]
    elif k == '\t':
        d2['TAB'] = d[k]
    elif k == '\n':
        d2['NEWLINE'] = d[k]
    else:
        d2[k] = d[k]
print(d2)