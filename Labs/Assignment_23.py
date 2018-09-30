# Author: Joel Turbi
# Assignment: Lab Assignment 23
# Course: CS140

import random
print("Here comes the dice:")
Roll_1 = random.randint(1,6)
Roll_2 = random.randint(1,6)
total = Roll_1 + Roll_2
print("Roll #1:", Roll_1)
print("Roll #2:", Roll_2)
print("The total is:", total)
while Roll_1 != Roll_2:
    Roll_1 = random.randint(1,6)
    Roll_2 = random.randint(1,6)
    total = Roll_1 + Roll_2
    print("Roll #1:", Roll_1)
    print("Roll #2:", Roll_2)
    print("The total is:", total)
    
