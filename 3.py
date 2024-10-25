# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 08:37:50 2024

@author: ADMIN
"""

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")

car = Car("Toyota", "Corolla", 2020)
car.display()
car.year = 2022
car.display()
