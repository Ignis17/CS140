# Author: Joel Turbi
# Assignment: Lab Assignment 36
# Course: CS140

def seasons_fun(user_input):
    if user_input in seasons:
       months = seasons[user_input]
    for user_input in months:
        print(user_input, end= " -- ")
    print()
seasons = {"Spring":["March", "April", "June"], "Summer":["June", "July", "August", "September"], "Fall":["September", "October", "November", "December"], "Winter":["December", "January", "February", "March"]}
user_input = input("Enter a season:\n")
seasons_fun(user_input)
              
