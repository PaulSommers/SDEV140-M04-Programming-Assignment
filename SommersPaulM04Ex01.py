"""
Author: Paul Sommers
Date written: 11/13/2024
Assignment: Module 04 Programming Assignment 1
Short Desc: This program prompts the user to enter a number greater than 1 and displays all prime numbers less than or equal to the number.
            It creates a list of all the numbers between 2 and the number the user entered, and then it loops trough this list checking
            each number to see if its prime or not (and outputting it if it is).
"""

# Prompt the user to enter a number greater than 1
number = int(input("Enter an integer greater than 1: "))

# Initialize an empty list to store numbers
numberList = []

# Populate the list with integers from 2 up to the entered number
for numbers in range(2, number + 1):
    numberList.append(numbers)

# Loop through the list to check if each number is prime
for num in numberList:
    isPrime = True  # Set flag for prime break-case
    for divisor in range(2, num):  # Check divisors from 2 to the number - 1
        if num % divisor == 0:  # If divisible, it's not a prime number
            isPrime = False
            break
    if isPrime:
        print(num)  # Print the number if it's prime