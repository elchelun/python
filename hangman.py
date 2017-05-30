#!/usr/bin/python

import sys
import re
import os
import random
import time

os.system('clear')

print "Welcome to Chelo's HangMan\n\n"
print "Please select what you want to play with: "
print "1) Movies"
print "2) Countries"
print "3) Mexican Food"
#option = raw_input("\nSelect 1-2-3: ")

os.system('clear')

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

def print_word(p, w):
    for i in range(len(p)):
        w.append("_ ")
        print w[i],
    print "\n\n"

options= ["movies", "countries", "mex_food"]
movies = ['deadpool', 'spiderman', 'superman', 'batman']
letters = []
word = []
count = 0

def search(p,w,l):
    for i in range(len(p)):
        if l == p[i]:
            w[i] = l
    return p,w,l

#Next line is for texting only
option = '1'

if option == "1":
    init_hang_print()
    picked = random.choice(movies)
    print_word(picked, word)
    if picked:
        while count < 7:
            found = False
            letter = raw_input("Enter a leter or 1 to guess the " + options[0] + ": ")
            if letter != "1":
                for i in range(len(picked)):
                    if letter == picked[i]:
                        word[i] = letter
                        found = True
                if found:
                    hang_print(count)
                    print_word(picked, word)
                else:
                    count += 1
                    hang_print(count)
                    print_word(picked, word)
            else:
                guess = raw_input("Enter your best guess: ")
                time.sleep(0.5)
                if guess == picked:
                    print "\nGood guess, you WIN\n"
                    quit()
                else:
                    print "\nSorry you LOST"
                    print "\nThe " + options[0] + "was " + picked
                    print "\nBetter luck next time :)\n"
                    quit()
