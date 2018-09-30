# Author: Joel Turbi
# Assignment: Lab Assignment 27
# Course: CS140

def checkout(item_num, price):
    subtotal = (item_num * price)
    taxes = (0.6 * subtotal) 
    total = (subtotal + taxes)
    print("Your total is: \n", "$", total)   
item_num = int(input("What is the amount of items you carry today?"))
price = float(input("What is the price of these items? "))
checkout(item_num, price)
