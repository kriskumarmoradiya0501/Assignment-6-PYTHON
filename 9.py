# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 08:59:05 2024

@author: ADMIN
"""

class Father:
    def __init__(self, father_name):
        self.father_name = father_name

    def father_details(self):
        print(f"Father's Name: {self.father_name}")

class Mother:
    def __init__(self, mother_name):
        self.mother_name = mother_name

    def mother_details(self):
        print(f"Mother's Name: {self.mother_name}")

class Child(Father, Mother):
    def __init__(self, father_name, mother_name, child_name):
        Father.__init__(self, father_name)
        Mother.__init__(self, mother_name)
        self.child_name = child_name

    def child_details(self):
        self.father_details()
        self.mother_details()
        print(f"Child's Name: {self.child_name}")

child = Child("John", "Sarah", "Charlie")
child.child_details()
