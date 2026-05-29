# profile class를 구현하라.
# profile에는 id, name, age, nationality정보가 있다.

# db class를 구현하라.
# db에는 profile list가 멤버 변수로 있고
# age(a)는 age가 a인 profile list를 반환하는 멤버 함수

class profile:
    def __init__(self, id, name, age, nationality):
        self.id = id
        self.name = name
        self.age = age
        self.nationality = nationality

class db:
    def __init__(self):
        self.mlist = []
    def age(self, a):
        rlist = []
        for p in self.mlist:
            if p.age == a:
                rlist.append(p)
        return rlist

        

agents = db() # C언어에 비유하면 db는 agents를 호출하는 구조체 변수명
# profile은 db속 mlist에 추가하기 위한 나만의 자료형.
agents.mlist.append(profile('007', 'Bond', 35, 'England'))
rage = agents.age(35) # age가 35인 profile list 반환
for i in rage:
    print(i.id, i.name, i.age, i.nationality)
for i in agents.mlist:
    print(i)