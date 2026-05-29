class slime:
    def __init__(self):
        self.hp = 10
        self.attk = 1
        self.df = 1
    def split(self):
        return slime(), slime()

class orc:
    def __init__(self):
        self.hp = 50
        self.attk = 10
        self.df = 10
    def bigswing(self, enemy1, enemy2):
        enemy1.hp -= self.attk
        enemy2.hp -= self.attk
        print(f"{type(enemy1).__name__}, {type(enemy2).__name__} got {self.attk} damages!")
        if enemy1.hp <= 0:
            print(f"{type(enemy1).__name__} is dead!")
        if enemy2.hp <= 0:
            print(f"{type(enemy2).__name__} is dead!")

# npc = slime()
# oc = orc()
# oc.bigswing(npc)