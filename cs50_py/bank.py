class Account:
    def __init__(self):
        self._balance = 0
    def __str__(self):
        return f"Balance: {self._balance}"
    @property
    def balance(self):
        return self._balance
    
    def deposit(self, n):
        self._balance += n

    def withdraw(self, n):
        self._balance -=n


def main():
    account = Account()
    print(account)

    account.deposit(100)
    account.withdraw(50)

    print(account)
if __name__ == "__main__":
    main()
