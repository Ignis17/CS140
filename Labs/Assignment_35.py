# Author: Joel Turbi
# Assignment: Lab Assignment 35
# Course: CS140

def encoded(text):
    result= ""
    location=0
    vowels= ['a','e','i','o','u']
    num_vowels= ['1','2','3','4','5']
    for x in text:
        if x in vowels:
            location= vowels.index(x)
            x = num_vowels[location]
        result+=x 
    print(result)
user_text = input('Enter a text:\n')
encoded(user_text)
