import player



class Enemy:
    def __init__(self, lvl):
        self.ehp = 100 + lvl
        self.edmg = 50
        self.on_fire = False

    def burning(self, firedmg):
        if self.on_fire:
            self.ehp -= firedmg
            print("Enemy took", firedmg, "damage from the fire")
