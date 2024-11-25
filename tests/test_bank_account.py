import unittest
from bank_account.bank_account import BankAccount


class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount(100)

    def test_deposit(self):
        self.account.deposit(50)
        self.assertEqual(self.account.balance, 150)

    def test_neagtive_initial(self):
        with self.assertRaises(ValueError):
            self.account = BankAccount(-10)

    def test_deposit_except(self):
        # error
        with self.assertRaises(ValueError):
            self.account.deposit(0)

    def test_withdraw(self):
        self.account.withdraw(25)
        self.assertEqual(self.account.balance, 75)

    def test_withdraw_except1(self):
        # error 1
        with self.assertRaises(ValueError): 
            self.account.withdraw(0)

    def test_withdraw_except2(self):
        # error 2 Insufficient
        with self.assertRaises(ValueError):
            self.account.withdraw(125)


    def test_transfer(self):
        target = BankAccount(0)
        self.account.transfer_to(target, 100)
        self.assertEqual(self.account.balance, 0)
        self.assertEqual(target.balance, 100)

    
    def test_transfer_except(self):
        target = 0
        with self.assertRaises(ValueError):
            self.account.transfer_to(target, 100)



if __name__ == "__main__":
    unittest.main()
