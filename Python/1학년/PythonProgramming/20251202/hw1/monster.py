class slime:
    def __init__(self):
        self.hp = 10
        self.attk = 1
        self.df = 1
    def split(self): # 무한 복제 가능성 있음
        return slime(), slime()

class orc:
    def __init__(self):
        self.hp = 30
        self.attk = 10
        self.df = 10
    def bigswing(self, enemy, attacker):
        enemy.hp -= attacker.attk
        print("Orc uses Big Swing!")
        # 아래 출력 시 enemy가 memeory 위치로 나옴.
        # print(f"attacked {enemy}. {enemy}'s hp is {enemy.hp} now.")
        print(f"attacked {type(enemy).__name__}. {type(enemy).__name__}'s hp is {enemy.hp} now.")