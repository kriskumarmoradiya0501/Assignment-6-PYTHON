# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 08:38:31 2024

@author: ADMIN
"""

class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Price: {self.price}")

    def is_price_above(self, value):
        return self.price > value

laptop = Laptop("Dell", "XPS 15", 1200)
laptop.display()
print(laptop.is_price_above(1000))
