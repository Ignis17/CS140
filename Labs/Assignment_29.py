# Author: Joel Turbi
# Assignment: Lab Assignment 29
# Course: CS140

print("Knock! Knock!")
dummy = input()
print("Ho-ho.")
dummy = input()
print("You know, your Santa impression could use a little work.\n")
answer=input("Would you like to read it again?")
print()
while(answer == "yes") or (answer == "YES") or (answer == "Yes"):
    print("Knock! Knock!")
    dummy = input()
    print("Ho-ho.")
    dummy = input()
    print("You know, your Santa impression could use a little work.")
    print()
    answer=input("Would you like to read it again?") 
print("Good bye!")
