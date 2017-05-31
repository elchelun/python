#!/usr/bin/python

import sys
import re
import os
import random
import time

#os.system('clear')

def init_hang_print():
    print "\t   ________"
    print "\t   |      |"
    print "\t   |        "
    print "\t   |        "
    print "\t   |        "
    print "\t   |        "
    print "\t -----      "
    print "\n\n"

def hang_print(x):
    os.system('clear')
    if x == 0:
        print "\t   ________"
        print "\t   |      |"
        print "\t   |        "
        print "\t   |        "
        print "\t   |        "
        print "\t   |        "
        print "\t -----      "
        print "\n\n"
    elif x == 1:
        print "\t   ________"
        print "\t   |      |"
        print "\t   |      O  "
        print "\t   |        "
        print "\t   |        "
        print "\t   |        "
        print "\t -----      "
        print "\n\n"
    elif x == 2:
        print "\t   ________"
        print "\t   |      |"
        print "\t   |      O  "
        print "\t   |      |  "
        print "\t   |      |  "
        print "\t   |        "
        print "\t -----      "
        print "\n\n"
    elif x == 3:
        print "\t   ________"
        print "\t   |      |"
        print "\t   |      O  "
        print "\t   |     /|  "
        print "\t   |      |  "
        print "\t   |        "
        print "\t -----      "
        print "\n\n"
    elif x == 4:
        print "\t   ________"
        print "\t   |      |"
        print "\t   |      O  "
        print "\t   |     /|\  "
        print "\t   |      |  "
        print "\t   |        "
        print "\t -----      "
        print "\n\n"
    elif x == 5:
        print "\t   ________"
        print "\t   |      |"
        print "\t   |      O  "
        print "\t   |     /|\  "
        print "\t   |      |  "
        print "\t   |     /   "
        print "\t -----      "
        print "\n\n"
    elif x == 6:
        print "\t   ________"
        print "\t   |      |"
        print "\t   |      O  "
        print "\t   |     /|\  "
        print "\t   |      |  "
        print "\t   |     / \  "
        print "\t -----      "
        print "\n\n"
        print "GAME OVER"

def init_print_word(p, w):
    for i in range(len(p)):
        if p[i] != " ":
            w.append("_ ")
        else:
            w.append(" ")
        print w[i],
    print "\n\n"

def print_word(p, w):
    for i in range(len(p)):
#        if p[i] != " ":
#            w.append("_ ")
#        else:
#            w.append(" | ")
        print w[i],
    print "\n\n"


def file2list(files, lines):
    with open(files) as file:
        for line in file:
            line = line.strip() #or someother preprocessing
            lines.append(line)
    return lines

options= ["", "movies", "country", "mexican food"]
movies = []
countries = []
mex_food = []
letters = []
bad_letter = []
word = []
count = 0

#Script start here
os.system('clear')
print "Welcome to Chelo's HangMan\n\n"
print "Please select what you want to play with: "
print "1) Movies"
print "2) Countries"
print "3) Mexican Food"
option = raw_input("\nSelect 1-2-3: ")

os.system('clear')

if option == "1":
    file2list('./movies', movies)
    init_hang_print()
    picked = random.choice(movies)
    init_print_word(picked, word)
elif option == "2":
    file2list('./countries', countries)
    init_hang_print()
    picked = random.choice(countries)
    init_print_word(picked, word)
elif option == "3":
    file2list('./mex_food', mex_food)
    init_hang_print()
    picked = random.choice(mex_food)
    init_print_word(picked, word)

if picked:
    while count < 6:
        found = False
        letter = raw_input("Enter a leter or 1 to guess the " + options[int(option)] + ": ")
        if letter != "1":
            for i in range(len(picked)):
                if letter == picked[i]:
                    word[i] = letter
                    found = True
            if found:
                hang_print(count)
                print_word(picked, word)
                print bad_letter, "\n\n"
            else:
                count += 1
                hang_print(count)
                print_word(picked, word)
                bad_letter.append(letter)
                print bad_letter, "\n\n"
            winner = "".join(word)
            if winner == picked:
                print "\nGood job, you WIN!!!\n\n"
                quit()
        else:
            guess = raw_input("Enter your best guess: ")
            time.sleep(0.5)
            if guess == picked:
                print "\nGood guess, you WIN!!!\n\n"
                quit()
            else:
                print "\nSorry you LOST"
                print "\nThe " + options[int(option)] + " was " + picked
                print "\nBetter luck next time :)\n"
                quit()
print "\nSorry you LOST"
print "\nThe " + options[int(option)] + " was " + picked
print "\nBetter luck next time :)\n"
quit()

