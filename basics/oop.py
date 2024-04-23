# class PascalCase
# def __init__(self, attributes)

class BankAccount:
    def __init__(self, account_number, holder, balance):
        self.account_number = account_number
        self.holder = holder
        self.balance = balance

    def show_balance(self):
        print(self.holder + " holds " + str(self.balance) + " in the account.")
 
    def add_deposit(self, deposit):
        if deposit > 0:
            self.balance += deposit


paul_account = BankAccount("777-666-555", "Paul Donahue", 2300)
teresa_account = BankAccount("777-666-0021", "Teresa Parker", 300456)

paul_account.show_balance()
teresa_account.show_balance()

paul_account.add_deposit(4000000)
paul_account.show_balance()

print(paul_account.holder)
