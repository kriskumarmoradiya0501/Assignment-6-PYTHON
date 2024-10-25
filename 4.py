# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 08:38:03 2024

@author: ADMIN
"""

class BankAccount:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient balance")

    def display(self):
        print(f"Account Number: {self.account_number}, Name: {self.name}, Balance: {self.balance}")

account = BankAccount(12345, "John", 1000)
account.deposit(500)
account.withdraw(300)
account.display()
