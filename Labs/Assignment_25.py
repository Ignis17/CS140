# Author: Joel Turbi
# Assignment: Lab Assignment 25
# Course: CS140

def chorus(number):
    for number in range(10, 0, -1):
        if (number ==1):
          print(number, '''bear in the bed and the little one said, "You know what? I'm lonely."''')
        else:
            print(number, '''bears in the bed and the little once said, "I'm crowded roll over."''')
            print("So, they all rolled over and one fell out.")
            print()
chorus(10)
