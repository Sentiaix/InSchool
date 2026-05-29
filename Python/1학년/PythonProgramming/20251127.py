# 13주차 목요일. <Class의 상속>
import random

class character:
    def __init__(self, name = 'Fin', hp = 10):
        self._hp = hp
        self._name = name
    def sethp(self, hp):
        self._hp = hp
    def hp(self):
        return self._hp
    def setname(self, name):
        self._name = name
    def __str__(self): # 이건 python 지정 함수
        return f"{self._name} hp: {self._hp}"
    
class warrior(character): # character에서 상속받은 class
    def __init__(self):
        super().__init__('Faker', 200) # 초기화 함수
        self._attk = 50
        self._def = 25
    def attack(self, enemy):
        enemy._hp -= self._attk
        if enemy._hp < 0:
            enemy._hp = 0
        print(f"{self._name} attacks {enemy._name}. enemy's hp is {enemy._hp}")
    def __str__(self): # 함수 재정의
        return super().__str__() + f" attk: {self._attk} def: {self._def}"

class warrior_mage(warrior):
    def __init__(self):
        super().__init__()
        self._attk = 100
        self._def = 10
    def attack(self, enemy): # 0~2: 빗나감, 3~7: 맞음, 8~10: 치명상
        evnt_attk = random.randrange(0,11)
        if evnt_attk <= 2: # miss
            print('Miss!')
        elif evnt_attk <= 7: # hit
            print('Hit!')
            enemy._hp -= self._attk
        elif evnt_attk <= 10: # critical hit
            print('Critical Hit!')
            enemy._hp -= self._attk * 2 # 2배의 피해
        if enemy._hp < 0:
            enemy._hp = 0
        print(f"{self._name} attacks {enemy._name}. enemy's hp is {enemy._hp}")
    def heal(self, amount): # 자기 스스로를 amount만큼 치유함
        print(f"Your hp was {self._hp}.", end='')
        self._hp += amount
        print(f' Now is {self._hp}.')
# -- 추가 한 기능 -- #
# attack에 확률에 따라 빗나감, 적중, 치명상을 설정함.
# 자가 치료 함수를 설정함.

magician = warrior_mage()
hero = warrior()
hero.setname('jake')
print(hero)
npc = character('Fin', 25)
npc.sethp(50)
print(npc)
# npc._hp = 50
# npc.hp = 50 # 이건 class의 member변수를 새로 만들어서 새로 대입하는거임. 위 npc._hp = 50으로 작동하는 기존 함수에 변수를 만드는거와 다름.
hero.attack(npc)
print(npc)
print('---- ---- ----')
npc.sethp(500)
magician.attack(npc)
print(magician)
magician.heal(30)