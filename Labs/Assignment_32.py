# Author: Joel Turbi
# Assignment: Lab Assignment 32
# Course: CS140

def display_even(max):
    for i in range(1, max):
       if i%2== 0:
           print(i, end=",")
    print()
a = int(input("Enter a number:\n"))
display_even(a)

