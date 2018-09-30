# Author: Joel Turbi
# Assignment: Lab Assignment 17B
# Course: CS140

price = int(input("What is the price?"))
if (price<50):
    print("Must buy!")
if (price>=50 and price<=59):
    print("On sale. Good price.")
if (price>=60 and price<=75):
    print("Regular price.")
if (price>75):
    print("Expensive.")
