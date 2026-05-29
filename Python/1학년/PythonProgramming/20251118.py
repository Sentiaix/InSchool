# d = {'name': 'mike', 'age': 56}
# print(d['name'])
# print(d['age'])
# d['job'] = 'boxer'
# print(d)

# for k in d.keys():
#     print(k, d[k])

# v = list(d.values())
# print(v)
# k = list(d.keys())
# print(k)
# print(k.sort())
# try:
#     print(d['time'])
# except:
#     print("***** KeyError *****")
# print(d.get('time'))

# d2 = d
# d2['job'] = 'singer'
# print(d, d2)

# d3 = d.copy()
# d3['age'] = 99
# print(d, d3)

# dd = {}
# dd[123] = d
# dd[456] = d3

# for k in dd.keys():
#     print(k, dd[k])

# print(dd[123]['name'])
# print(dd[456]['age'])

db = {}
for i in range(0):
    s = input('Enter the informations (id name age job): ').split()
    id = int(s[0])
    name = s[1]
    age = int(s[2])
    job = s[3]
    db[id] = {'name': name, 'age': age, 'job': job}

db = {123: {'name': 'jake', 'age': 19, 'job': 'dog'},
      456: {'name': 'fin', 'age': 15, 'job': 'human'},
      789: {'name': 'foot', 'age': 8, 'job': 'cat'}}

for k in db.keys():
    print(k, db[k])

# 1. id, name, age, job을 전부 list로 변경하고 출력하는 함수 작성
def to_list( fdb ):
    id_list = list(fdb.keys())
    print('id list  ', id_list)
    name_list = []
    age_list = []
    job_list = []
    for dbv in fdb.values():
        name_list.append(dbv['name'])
        age_list.append(dbv['age'])
        job_list.append(dbv['job'])
    print(f"name list {name_list}\nage list  {age_list}\njob list  {job_list}")

print('--------------------------')
to_list(db)

# 2. db를 name:{id:?, age:?, job:?}으로 dict를 재구성하는 함수 설정
def name_as_key(fdb):
    r = {}
    for k in fdb.keys():
        id = k
        name = fdb[k]['name']
        age = fdb[k]['age']
        job = fdb[k]['job']
        r[name] = {'id': id, 'age': age, 'job': job}
    return r
namedb = name_as_key(db)
print('------name as key------')
for k in namedb.keys():
    print(k, namedb[k])