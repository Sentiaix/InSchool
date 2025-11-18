# valid_case = { "one" : 1, 
#                "two" : 2,
#                "three" : 3 }
# # s = input()
# # print(valid_case[s])
# print(len(valid_case))
# print(valid_case)
# valid_case.update({'one': 1, 'two': 2, 'three': 3, 'four': 4})
# valid_case['five'] = 5
# print(valid_case)
# for n in valid_case.values():
#     print(n)

# for k, v in valid_case.items():
#     print(k, v)
# if 'one' in valid_case:
#     print(valid_case['one'])
# del(valid_case['three'])
# print(valid_case)

# --- 실습 --- # 위까지는 그냥 필기임

# --- 필기 1 --- #

s = input('enter the string: ')
print(s.split())
print('--- dictonary ---')
d = {2: 'two', 3: 'three', 'two': 2.0}
print(len(d), d)
print(d[2], d['two'])
# print(d[0]) # KeyError
print(d.get(0)) # Return: None
d[0] = 'infinite' # add to dict
print(d)
d.update({2: 'twenty', 'five': 5})
print(d)
# print(d.keys())
# print(d.values())
# print(d.items())
for k in d.keys():
    print(k)
for v in d.values():
    print(v)
for k, v in d.items():
    print(k,v)

if s in d:
    print(s, 'is key')
else:
    print(s, 'is not key')
if s in d.values():
    print(s, 'is value')
else:
    print(s, 'is not value')
del(d['five'])
print(d)
d.clear()
print(d)