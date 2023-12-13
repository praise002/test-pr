class Account:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0
        
    def __str__(self):
        return f'{self.owner}\'s account balance is {self.baance}'
    
    def deposit(self, amount):
        if amount > 0:
            self.balance == amount
        
    def withdraw(self, amount):
        if (amount > 0) and (amount <= self.balance):
            self.balance -= amount
            return True
        else:
            return False
        
    def transfer(self, amount, recipient):
        if amount < 0:
            # amount is negative, return False
            return False
        # Attempt to withdraw the amount from the sender's account
        elif self.withdraw(amount) == True:
            # If withdrawal was successful, deposit the amount into the recipient's account
            recipient.deposit(amount)
            return True
        # Withdrawal failed maybe it exceeds the account balance, return False
        # elif self.withdraw(amount) == False:
        #     return False
        else:
            return False
            
            

if __name__ == '__main__':
    my_account = Account('Mehdi')
    # print(my_account.owner)
    # print(my_account.balance)
    # print(my_account)
    # print(my_account.deposit(100))
    # print(my_account)
    
    # print(my_account.deposit(-100))
    # print(my_account)
    
    # print(my_account)  
    # my_account.deposit(100)
    # print(my_account)  

    # print(my_account.withdraw(20)) 
    # print(my_account)  

    # # WE IGNORE NEGATIVE INPUTS
    # print(my_account.withdraw(-20)) 
    # print(my_account)  

    # # We do not make withdrawals if they exceed the balance.
    # print(my_account.withdraw(200)) 
    # print(my_account) 
    
    print(my_account)
    print(my_account.deposit(100))
    print(my_account)
    print(my_account.withdraw(40))
    print(my_account.withdraw(60))
    print(my_account)
    
    print(my_account.transfer(40, 'Danmi'))
    print(my_account)
    
# python -m unittest -k test_account_objects_withdraw_possible_amount test.py
# python -m unittest -k test_account_objects_withdraw_possible_amount -v test.py

lst = []
lst.remove()
