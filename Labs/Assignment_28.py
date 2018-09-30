# Author: Joel Turbi
# Assignment: Lab Assignment 28
# Course: CS140

def watch(age):
    if age < 13:
        print("You can not watch the movie! It's PG13. Sorry.")
    elif (age == 13) or (age <= 17):
        print("You can watch the movie only if accompanied by an adult.")
    elif (age == 18) or (age > 18):
        print("Enjoy the movie!")

ages = int(input("What is your age?  "))
watch(ages)
