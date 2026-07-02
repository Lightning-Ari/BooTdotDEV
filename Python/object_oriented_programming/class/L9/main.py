class Archer:
    def __init__(self, name: str, health: int, num_arrows: int) -> None:
        self.name = name
        self.health = health
        self.num_arrows = num_arrows

    def take_hit(self) -> None:
        try :
            self.health -= 1
        except NameError:
            if self.health < 1:
                raise RuntimeError(f"{self.name} is dead")      

    def shoot(self, target: "Archer") -> None:
        if self.health < 1 :
            raise RuntimeError(f"{self.name} is dead")
        elif self.num_arrows < 1:
            raise RuntimeError(f"{self.name} can't shoot")
        else: 
            self.num_arrows -= 1
            print(f"{self.name} shoots {target} ")
            target.take_hit()
                
            

    # don't touch below this line

    def get_status(self) -> tuple[str, int, int]:
        return self.name, self.health, self.num_arrows

    def print_status(self) -> None:
        print(f"{self.name} has {self.health} health and {self.num_arrows} arrows")
