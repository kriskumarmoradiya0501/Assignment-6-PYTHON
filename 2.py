# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 08:37:43 2024

@author: ADMIN
"""

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def show_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")

    def is_passed(self):
        return self.grade >= 40

student = Student("Alice", 20, 45)
student.show_details()
print(student.is_passed())
