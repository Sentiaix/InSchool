class bmw:
    def __init__(self, speed, fuel):
        self.spd = speed
        self.fuel = fuel
    def speed(self):
        return self.spd
    def gas(self, amount = 0): # 가속
        self.spd += amount
    def cbreak(self, amount): # 감속
        self.spd -= amount * (self.spd * 0.1) # 현재 속도의 10% * n초만큼 감속.
        self.spd = int(self.spd)
        if self.spd <= 0:
            self.spd = 0