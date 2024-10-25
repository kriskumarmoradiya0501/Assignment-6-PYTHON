# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 08:38:21 2024

@author: ADMIN
"""

class MovieTicket:
    def __init__(self, movie_name, seat_no, price):
        self.movie_name = movie_name
        self.seat_no = seat_no
        self.price = price

    def display(self):
        print(f"Movie: {self.movie_name}, Seat No: {self.seat_no}, Price: {self.price}")

    def is_affordable(self, budget):
        return self.price <= budget

ticket = MovieTicket("Inception", "A10", 300)
ticket.display()
print(ticket.is_affordable(250))
