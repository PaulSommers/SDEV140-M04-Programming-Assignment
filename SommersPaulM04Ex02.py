"""
Author: Paul Sommers
Date written: 11/13/2024
Assignment: Module 04 Programming Assignment 2
Short Desc: This program takes a dictionary of items and their prices, and displays the top three most expensive items.
"""

# Create dictionary of items and their prices
shop = {'Apple': 0.50, 'Banana': 0.20, 'Mango': 0.99, 'Coconut': 2.99, 'Pineapple': 3.99}

# Sort the dictionary by price in descending order and get the top 3 items
sortedShop = sorted(shop.items(), key=lambda x: x[1], reverse=True)[:3]

# Display the top three items and their prices
for item, price in sortedShop:
    print(item, price)