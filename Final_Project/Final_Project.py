'''
Group Members: Luis Casado, Joel Turbi
Professor: Dr. Zavala
Class: CS 140
Assignment: Final Project
Due Date: Tuesday 20th, 2016
CS-140 Final Project
'''

import random

def getwords(text):
    stopletters = [".", ",", ";", ":", "'s", '"', "!", "?", "(", ")", '“', '”']
    text = text.lower()
    for letter in stopletters:
        text = text.replace(letter, "")
    words = text.split()
    return words


def compute_bigrams(input_list):
    bigram_list = {}
    for i in range(len(input_list)-1):
        if input_list[i] in bigram_list:
            bigram_list[input_list[i]] = bigram_list[input_list[i]]+[input_list[i+1]]
        else:
            bigram_list[input_list[i]] = [input_list[i+1]]
    return bigram_list

# Change the filename when you run the program for a different file
filename = "sample1.txt"
file = open(filename, "r")
text = file.read()
words_list = getwords(text)

# Bigrams is the dictionary you will use for implementing the 2-grams approach
bigrams = compute_bigrams(words_list)
# print(bigrams)

# ADD YOUR CODE BELOW THIS POINT
def paragraph(bigrams):
    n = random.randint(0, len(words_list)-1)
    key = words_list[n]
    print(key, end=" ")
    for x in range(40):
        words = bigrams[key]
        ran_word = random.randint(0, (len(words)-1))
        key = words[ran_word]
        print(key, end=" ")
    print("\n")

for x in range(0, 5):
    paragraph(bigrams)


'''
Team Members: Joel Turbi & Luis Casado
* Who did What?
- Joel:
* Assembled together the sample files.
- Luis & Joel:
* Worked on the main program together.
- Luis:
* Put together the results and final report.
'''
