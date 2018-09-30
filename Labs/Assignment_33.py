# Author: Joel Turbi
# Assignment: Lab Assignment 33
# Course: CS140

def perfect_squares(max):
    for i in range(1, max):
        if i%2== 0:
            print(i**2, end=",")
a = int(input("Enter a number:\n"))
perfect_squares(a)
