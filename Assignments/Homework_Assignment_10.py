# Author: Joel Turbi
# Assignment: Homework Assignment 10
# Course: CS140

import random
def getwords(text):
    text = text.split()
    for i in range(20):
        result=random.randint(0, len(text)-1)
        print (text[result], end = " ")
# Main Program
words_list = getwords("In what was once North America, the Capitol of Panem maintains its hold on its 12 districts by forcing them each to select a boy and a girl, called Tributes, to compete in a nationally televised event called the Hunger Games. Every citizen must watch as the youths fight to the death until only one remains. District 12 Tribute Katniss Everdeen (Jennifer Lawrence) has little to rely on, other than her hunting skills and sharp instincts, in an arena where she must weigh survival against love.")

