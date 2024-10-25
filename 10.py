# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 08:59:24 2024

@author: ADMIN
"""

class Employee:
    def show_details(self):
        print("Employee Details")

class Developer(Employee):
    def show_details(self):
        print("Developer Details")

class Manager(Employee):
    def show_details(self):
        print("Manager Details")

dev = Developer()
man = Manager()

dev.show_details()
man.show_details()
