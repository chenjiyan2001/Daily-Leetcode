# 1. O(1) t:248ms(75%) O(n) m:41.5M(13%) 模拟
class Bank:

    def __init__(self, balance: List[int]):
        self.bank = balance
        self.n = len(balance)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if 1 <= account1 <= self.n and 1 <= account2 <= self.n:
            if self.bank[account1 - 1] >= money:
                self.bank[account1 - 1] -= money
                self.bank[account2 - 1] += money
                return True
        return False

    def deposit(self, account: int, money: int) -> bool:
        if account < 1 or account > self.n:
            return False
        self.bank[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if account < 1 or account > self.n or self.bank[account - 1] < money:
            return False
        self.bank[account - 1] -= money
        return True