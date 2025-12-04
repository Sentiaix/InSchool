class hunter:
    def __init__(self, weapon):
        self.hp = 10
        self.attk = weapon
        self.df = 10
    def attacks(self, enemy):
        enemy.hp -= self.attk
        print(f"{type(enemy).__name__} got {self.attk} damages!")
        if enemy.hp <= 0:
            print(f"{type(enemy).__name__} is dead!")

class knight(hunter):
    def __init__(self, weapon):
        super().__init__(self)
        self.hp = 20
        self.attk = weapon
        self.df = 10
    
# k = knight(5)
# npc = hunter(3)
# k.attacks(npc)