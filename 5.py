# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 08:38:13 2024

@author: ADMIN
"""

class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def display(self):
        print(f"Name: {self.name}, Position: {self.position}, Salary: {self.salary}")

    def increment_salary(self, percentage):
        self.salary += self.salary * (percentage / 100)

employee = Employee("Jane", "Manager", 50000)
employee.display()
employee.increment_salary(10)
employee.display()
