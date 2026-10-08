class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = 0
        self.set_balance(balance)

    # Setter for account number
    def set_account_number(self, account_number):
        self.__account_number = account_number

    # Setter for balance
    def set_balance(self, balance):
        if balance < 0:
            print("The balance must be not be a negative number.")
        else:
            self.__balance = balance

    # Getter for account number
    def get_account_number(self):
        return self.__account_number

    # Getter for balance
    def get_balance(self):
        return self.__balance


# Object of class BankAccount
a1 = BankAccount(12345, 1000)

print("Account 1")
print("Account Number:", a1.get_account_number())
print("Balance:", a1.get_balance())

print()
print("Update balance to -100")
a1.set_balance(-100)

print("Account Number:", a1.get_account_number())
print("Balance:", a1.get_balance())
