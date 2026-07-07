class Angel:
    def attack(self):
        return "rage 10"

class BerserkAngel(Angel):
    def attack(self):
        return "Berserk " + super().attack().replace("10", "15")

unit = BerserkAngel()
print(unit.attack())