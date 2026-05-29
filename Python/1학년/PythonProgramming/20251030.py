def change_immutable(x, y):
    x = 999
    y += (999,) # expect tuple var


def change_mutable(x, y):
    x[0] = 999 # expect list var
    y += [999]

i = 8
t = (1,2,3)

print('immutable', i, t)
change_immutable(i, t)

print('changed imuutable', i, t)

mi = [8]
ml = [1,2,3]
ml.append(85) # append: 추가하다
ml.reverse() # reverse: 뒤집다
ml.sort() # sort: 정렬

######
kl = ml # mutable인 list를 그대로 다른 변수에 대입하면 reference(주소까지 참조)한다, 즉 가명을 쓰는 동일인물 같은 것
print(kl)
kl[0] = 1313
print(f"kl, ml = {kl}, {ml}")
kl = ml.copy() # 하지만 .copy()를 하면 kl은 ml의 값만 deepcopy함. ml의 쌍둥이를 하나 더 만드는 것. immutable은 이런식으로 작동
# kl = ml[:] # 이런식으로 slicing을 이용하는게 .copy()보다 더 빠르게 복사함
kl[0] = 1231
print(f".copy() kl, ml = {kl}, {ml}")
######

# ml[2:4] = [33, 55]
# print(mi, ml)
# change_mutable(mi, ml)
# print(mi, ml)