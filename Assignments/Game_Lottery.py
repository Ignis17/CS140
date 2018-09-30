# Author: Joel Turbi
# Assignment: Lottery Game
# Course: CS140


#Lottery Game
import random
pick3 = random.sample(range(9), 3)
pick5 = random.sample(range(25), 5)
game = int(input("Choose a game of lottery:\n"+"1 - pick 5\n"+"2 - Pick 3\n"))
if game == 1:
    print("Enter five numbers between 1 and 25:\n")
    number_1 = int(input())
    number_2 = int(input())
    number_3 = int(input())
    number_4 = int(input())
    number_5 = int(input())
if pick5 == number_1 and pick5 == number_2 and pick5 == number_3 and pick5 == number_4 and pick5 == number_5:
    print("The winning numbers are:\n", pick5)
    print("You are the winner!")
else:
    print("The winning numbers are:\n", pick5)
    print("Sorry, you are a loser.")
    question = input("Yes or No")
    print("Would you like to try again\n"+question)
    answer = input()
    if question == answer:
        game = int(input("Choose a game of lottery:\n"+"1 - pick 5\n"+"2 - Pick 3\n"))
    else:
        print("Good bye")
        

