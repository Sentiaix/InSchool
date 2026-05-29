class hunter:
    def __init__(self, weapon):
        self.hp = 10
        self.attk = weapon
        self.df = 5
    def attacks(self, obj):
        obj.hp -= self.attk
        print(f"attacked {type(obj).__name__}. {type(obj).__name__}'s hp is {obj.hp} now.")

class knight:
    def __init__(self, weapon):
        self.hp = 20
        self.attk = weapon
        self.df = 10
    def attacks(self, obj):
        obj.hp -= self.attk
        print(f"attacked {type(obj).__name__}. {type(obj).__name__}'s hp is {obj.hp} now.")