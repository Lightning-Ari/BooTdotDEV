def main():
    new_brawlers = Brawler("Aragorn", 4, 4)
    new_brawlers = Brawler("Gimli", 2, 7)
    new_brawlers = Brawler("Legolas", 7, 7)
    new_brawlers = Brawler("Frodo", 3, 2)

    fight(Brawler.name = "Aragorn", Brawler.name =  "Gimli")


# don't touch below this line


class Brawler:
    def __init__(self, name, speed, strength):
        self.name = name
        self.speed = speed
        self.strength = strength
        self.power = speed * strength


def fight(attacker, defender):
    print(f"{attacker.name}: {attacker.power} power")
    print(f"{defender.name}: {defender.power} power")
    if attacker.power > defender.power:
        print(f"{attacker.name} wins!")
    elif attacker.power < defender.power:
        print(f"{defender.name} wins!")
    else:
        print("It's a tie!")
    print("---------------------------------")


main()
