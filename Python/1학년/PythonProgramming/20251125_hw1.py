'''profile class를 구현하라.
profile에는 id, name, age정보가 있다.

p  = profile(123, ‘Kim’, 35)
p2 = profile()
print(p, p.get_id(), p.get_name(), p.get_age())

 
db class를 구현하라..
db에는 profile list가 멤버 변수로 있고...
append 함수는 list에 profile만 추가되는 멤버 함수 
age(a)는 age가 a인 profile list를 반환하는 멤버 함수이다
name(a)는 name이 a인 profile list를 반환하는 멤버 함수이다
id(a)는 id가 a인 profile list를 반환하는 멤버 함수이다.
'''

class profile:
    def __init__(self, id = 0, name = '', age = 0):
        # 함수명이 id,name,age이여서 self.id 식으로 적으면
        # 예약어랑 겹치므로 callable error 발생. 함수명을 바꿔서 해결
        self.id = id
        self.name = name
        self.age = age
    def get_id(self):
        return self.id
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def __str__(self):
        return f"{self.id} {self.name} {self.age}"

class db:
    def __init__(self):
        self.plist = []
    def append(self, n):
        if isinstance(n, profile):
            self.plist.append(n)
    def age(self, a):
        r = []
        for m in self.plist:
            if m.age == a:
                r.append(m)
        return r
    def name(self, a):
        r = []
        for m in self.plist:
            if m.name == a:
                r.append(m)
        return r
    def id(self, a):
        r = []
        for m in self.plist:
            if m.id == a:
                r.append(m)
        return r

def print_list(n):
    for i in n:
        print(i.id, i.age, i.name)

mydb = db()
p = profile(123, 'Kim', 35)
p2 = profile()
print(p, p.get_id(), p.get_name(), p.get_age())
mydb.append(profile(345, 'Lee', 25))
mydb.append(profile(999, 'Kim', 45))
mydb.append(profile(111, 'Kim', 35))

print('--- age ---')
print_list(mydb.age(35))
print('--- name ---')
print_list(mydb.name("Kim"))
print('--- id ---')
print_list(mydb.id(345))