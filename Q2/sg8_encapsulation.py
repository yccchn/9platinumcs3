class BankAccount:  # Creates the BankAccount class
    def __init__(self, account_number, balance):  # Sets the account details
        self.__account_number = account_number  # Saves the account number
        self.__balance = 0  # Starts the balance at 0
        self.set_balance(balance)  # Sets the starting balance

    # Setter for account number
    def set_account_number(self, account_number):  # Updates the account number
        self.__account_number = account_number  # Saves the new account number

    # Setter for balance
    def set_balance(self, balance):  # Updates the balance
        if balance < 0:  # Checks if the balance is negative
            print("The balance must be not be a negative number.")  # Prints an error message
        else:  # If the balance is not negative
            self.__balance = balance  # Saves the new balance

    # Getter for account number
    def get_account_number(self):  # Gets the account number
        return self.__account_number  # Returns the account number

    # Getter for balance
    def get_balance(self):  # Gets the balance
        return self.__balance  # Returns the balance


# Object of class BankAccount
a1 = BankAccount(12345, 1000)  # Creates a bank account

print("Account 1")  # Prints the account name
print("Account Number:", a1.get_account_number())  # Prints the account number
print("Balance:", a1.get_balance())  # Prints the balance

print()  # Prints a blank line
print("Update balance to -100")  # Shows the update
a1.set_balance(-100)  # Tries to set a negative balance

print("Account Number:", a1.get_account_number())  # Prints the account number
print("Balance:", a1.get_balance())  # Prints the balance again
