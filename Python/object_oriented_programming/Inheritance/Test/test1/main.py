class BankAccount:
    def __init__(self, owner: str, starting_balance: int) -> None:
        self.name = owner
        self._balance = starting_balance

    def get_balance(self) -> int:
        return self._balance

    def deposit(self, amount: int) -> int:
        if amount > 0 :
            self._balance += amount
            return self._balance
        else :
            return self._balance

    def withdraw(self, amount: int) -> bool:
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            return True
        else :
            return False
