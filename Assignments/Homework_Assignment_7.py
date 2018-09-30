# Author: Joel Turbi
# Assignment: Homework Assignment #7
# Course: CS140

#Lottery Game - Pick 3
import random
pick3 = random.sample(range(1, 4),3)
print("**** Welcome to PICK3 lottery game ****\n")
print("Please pick three numbers between 1 and 9:")
numbersEntry1 = number_1 = int(input())
numbersEntry2 = number_2 = int(input())
numbersEntry3 = number_3 = int(input())
while numbersEntry1 and numbersEntry2 and numbersEntry3 != pick3:
    print("The winning numbers are:", pick3)
    print("Sorry you do not win this time.")
    numbersEntry = input("Do You want to play again (Yes/No)? ")
    if (numbersEntry == 'Yes') or (numbersEntry== 'yes') or (numbersEntry == 'YES'):
        
        print("Please pick three numbers between 1 and 9:")
        pick3 = random.sample(range(1, 4),3)
        numbersEntry = number_1 = int(input())
        numbersEntry = number_2 = int(input())
        numbersEntry = number_3 = int(input())
    else:
        if (numbersEntry == 'No')or (numbersEntry== 'no') or (numbersEntry == 'NO'):
            print("Goodbye")
            quit()
print("The winning numbers are:", pick3)
print("CONGRATULATIONS! YOU ARE A WINNER!\n", "YOU CAN CASH YOUR PRIZE AT MEDGAR EVERS COLLEGE!")
print("Goodbye")
