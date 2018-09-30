# Author: Joel Turbi
# Assignment: Lab Assignment 21
# Course: CS140

def greeting(day):
    if day == "Monday":
        print("Have a wonderful week")
    else:
        if (day == "Friday") or (day == "Saturday"):
            print("have a wonderful weekend")
        else:
            print("Hang in there!")

day = input("What day is it? ")
greeting(day)

