"""class Angel:
    def attack(self):
        return "rage 10"

class BerserkAngel(Angel):
    def attack(self):
        return "Berserk " + super().attack().replace("10", "15")

unit = BerserkAngel()
print(unit.attack())
"""

class Human:
    def __init__(self, name: str, speed: int) -> None:
        self.name = name
        self.speed = speed
    
    def get_name(self) -> str:
        return self.name
    
    def get_speed(self) -> int:
        return self.speed
    
class SportMan(Human):
    def __init__(self, name: str, speed: int) -> None:
        super().__init__(name, speed)

    def get_speed(self) -> int:
        return super().get_speed() + 5
    

any_human = Human("Dip", 5)
arindam = SportMan("Arindam", 5)

print(f"{arindam.get_name()} is name and speed is {arindam.get_speed()}")
