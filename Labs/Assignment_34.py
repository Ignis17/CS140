# Author: Joel Turbi
# Assignment: Lab Assignment 34
# Course: CS140

def expanded(text):
    result = ""
    for letter in text:
        result= result + letter +"  "
    return result
def dashed(text):
    result = ""
    for letter in text:
        result = result +letter +" - "
    return result
def reversed(text):
    result=""
    for letter in range(len(text)):
        result = result + text[(len(text) - 1) - letter]
    return result
text = input("Enter a text:\n")
print(expanded(text))
print(dashed(text))
print(reversed(text))

