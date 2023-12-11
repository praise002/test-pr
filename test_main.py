import unittest
from main import Bank

class TestBankAndBankAccount(unittest.TestCase):
    def setUp(self):
        self.my_bank = Bank("MyBank")
        self.account1 = self.my_bank.create_account("Alice", 1000)
        self.account2 = self.my_bank.create_account("Bob", 500)

    def test_create_account(self):
        self.assertEqual(self.my_bank.get_account_balance(self.account1), 1000)
        self.assertEqual(self.my_bank.get_account_balance(self.account2), 500)

    def test_deposit(self):
        self.my_bank.deposit(self.account1, 200)
        self.assertEqual(self.my_bank.get_account_balance(self.account1), 1200)

    def test_withdraw(self):
        self.my_bank.withdraw(self.account2, 100)
        self.assertEqual(self.my_bank.get_account_balance(self.account2), 400)

    def test_withdraw_insufficient_funds(self):
        result = self.my_bank.withdraw(self.account2, 600)
        self.assertEqual(result, "Insufficient funds.")
        self.assertEqual(self.my_bank.get_account_balance(self.account2), 500)

    def test_get_account_balance_account_not_found(self):
        result = self.my_bank.get_account_balance(999)
        self.assertEqual(result, "Account not found.")

if __name__ == '__main__':
    unittest.main()
