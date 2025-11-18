# --- 필기 3 --- #
# set 형식

a = {2, 2, 3, 'stuff'}
print(a)
a.add(3)
a.add('three')
print(a)
b = set([1, 2, 3, 'other'])
print(b)
print(a&b, a.intersection(b))
print(a|b, a.union(b))
print(a-b, a.difference(b))
print('three in a', 'three' in a)
print('four in a', 'four' in a)
for i in a:
    print(i)