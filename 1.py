# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 08:36:56 2024

@author: ADMIN
"""

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print(f"Title: {self.title}, Author: {self.author}, Price: {self.price}")

book1 = Book("Python Basics", "John Doe", 500)
book2 = Book("Data Science", "Jane Doe", 600)

book1.display()
book2.display()
