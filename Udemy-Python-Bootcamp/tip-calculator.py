# Day 2:
# Description:
# We're going to build a tip calculator.
# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay:
# (150.00 / 5) * 1.12 = 33.6
# Data Types
# Type Error, Checking and Conversion
# Mathematical Operation

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
tip_per_head=tip/100*bill+bill
print(f"Each person should pay: {tip_per_head:.2f}")

#OUTPUT:
# Welcome to the tip calculator!
# What was the total bill? $100
# What percentage tip would you like to give? 10 12 15 10
# How many people to split the bill? 5
# Each person should pay: 110.00
