import unittest
from unittest.mock import MagicMock
class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount('test', 1234.5)

    def test_create_bank_account(self):
        self.assertEqual(BankAccount('abc123', 1200.0).balance, 1200.0) #корректно созданный объект

        with self.assertRaises(ValueError) as context1:
            x = BankAccount('abc123', '1200.0')
        self.assertEqual('Баланс должен быть числом с плавающей точкой', str(context1.exception))

        with self.assertRaises(ValueError) as context2:
            x = BankAccount('abc123', -1200.0)
        self.assertEqual('Баланс отрицательный', str(context2.exception))

    def test_deposit(self):
        before_deposit = self.account.getBalance()
        self.account.deposit(50.0)
        self.assertEqual(before_deposit + 50.0, self.account.getBalance())

        with self.assertRaises(ValueError) as context1:
            self.account.deposit(0)
        self.assertEqual('Сумма должна быть больше нуля', str(context1.exception))

        with self.assertRaises(ValueError) as context2:
            self.account.deposit(-9)
        self.assertEqual('Сумма должна быть больше нуля', str(context2.exception))
    
    def test_withdraw(self):
        before_withdraw = self.account.getBalance()
        self.account.withdraw(123.4)
        self.assertEqual(before_withdraw, self.account.getBalance() + 123.4)

        with self.assertRaises(ValueError) as context1:
            self.account.withdraw(5555.5)
        self.assertEqual('Недостаточно средств', str(context1.exception))

        with self.assertRaises(ValueError) as context2:
            self.account.withdraw(0)
        self.assertEqual('Сумма должна быть больше нуля', str(context2.exception))
    
    def test_get_balance(self):
        self.assertEqual(self.account.balance, self.account.getBalance())
    

def minus_money(x):
    if x <= 0:
        raise ValueError('Сумма должна быть больше нуля')
class BankAccount:
    def __init__(self, accountNumber: str, balance: float=0.0):
        if type(balance) != float:
            raise ValueError('Баланс должен быть числом с плавающей точкой')
        if balance < 0:
            raise ValueError('Баланс отрицательный')
        self.accountNumber = accountNumber
        self.balance = float(balance)
    def deposit(self, amount: float):
        minus_money(amount)
        self.balance += amount
    def withdraw(self, amount: float):
        minus_money(amount)
        if amount > self.balance:
            raise ValueError('Недостаточно средств')
        self.balance -= amount
    def getBalance(self):
        return self.balance

        
unittest.main()
