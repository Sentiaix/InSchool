class profile:
    def __init__(self, id, name, age, nation):
        # 여기서 memeber 변수를 저장.
        self.id = 0
        self.name = 'hong'
        self.age  = 18
        self.nation = 'Korea'
    def print(self):
        print(self.id, self.name, self.age, self.nation)
    def __str__(self):
        return f"for print {self.id} {self.name} {self.age} {self.nation}"
    
class db:
    def __init__(self):
        self.plist = []
    def append(self, n):
        if str(type(n)).find('profile') >= 0:            
            self.plist.append(n)
    def age(self, a):
        r = []
        for m in self.plist:
            if m.age == a:
                r.append(m)
        return r

mydb = db()
print(mydb.plist)
p = profile(123, 'kim', 25, 'Chosun')
print(p)
mydb.plist.append(p)
mydb.append(p)
mydb.append(profile(456, 'lee', 23, 'Korea'))
mydb.append('string')
mydb.age(25)

mydb.plist = 'list now is string'
print('list length', len(mydb.plist))
# p.id = 456
# p.name = 'gil dong'
# p.nation = 'japan'

# p.print()