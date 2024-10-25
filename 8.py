# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 08:38:41 2024

@author: ADMIN
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def show_student(self):
        self.display()
        print(f"Grade: {self.grade}")

student = Student("Bob", 18, "A")
student.show_student()
