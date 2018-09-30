# Author: Joel Turbi
# Assignment: Lab Assignment 26
# Course: CS140

def message(ages):
    if ages < 16:
        print("You can't drive.")
    elif (ages == 16) or (ages == 17):
        print("You can drive but not vote.")
    elif (ages == 18) or (ages <= 24):
        print("You can vote, but not rent a car.")
    else:
        print("You can do pretty much anything.")
age = int(input("What is your age? "))
message(age)
