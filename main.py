# Add bank class here

class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}

    def create_account(self, account_holder, initial_balance=0):
        account_number = len(self.accounts) + 1
        account = BankAccount(account_number, account_holder, initial_balance)
        self.accounts[account_number] = account
        return account_number

    def get_account_balance(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number].get_balance()
        else:
            return "Account not found."

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number].deposit(amount)
            return f"Deposited ${amount} into account {account_number}."
        else:
            return "Account not found."

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            success = self.accounts[account_number].withdraw(amount)
            if success:
                return f"Withdrew ${amount} from account {account_number}."
            else:
                return "Insufficient funds."
        else:
            return "Account not found."


class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        else:
            return False


# Example Usage
if __name__ == "__main__":
    my_bank = Bank("MyBank")

    # Create accounts
    account1 = my_bank.create_account("Alice", 1000)
    account2 = my_bank.create_account("Bob", 500)

    # Perform transactions
    print(my_bank.deposit(account1, 200))
    print(my_bank.withdraw(account2, 100))

    # Check account balances
    print(f"Account {account1} balance: ${my_bank.get_account_balance(account1)}")
    print(f"Account {account2} balance: ${my_bank.get_account_balance(account2)}")
