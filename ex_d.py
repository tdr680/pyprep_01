# -*- coding: utf-8 -*-

#############################################################################################################

# TODO write a function km_to_miles which returns miles given kilometers
# TODO write a function miles_to_km which returns kilometers given miles

# HINT: http://www.metric-conversions.org/length/kilometers-to-miles.htm

#############################################################################################################

def factorial(n):
    # TODO: complete the code to calculate and return factorial of n
    f = 1
    for i in range(1, n+1):
        pass # <- this line to be replaced by your code
    return f

print factorial(5)
# 120

#############################################################################################################

def print_deck(suits, ranks):
    # TODO: go through all suits and all ranks and print all combinations:
    pass # <- this to be replaced by your code

# now create the lists of suits and ranks and call the function
SUITS = ["♧", "♢", "♡", "♤"]
RANKS = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]

print_deck(SUITS, RANKS)
# A♧
# 2♧
# 3♧
# ...

#############################################################################################################

def create_deck(suits, ranks):
    # TODO: similar to print_deck, but now collect all combination and return them as list of tuples:
    return [] # <- this to be replaced by your code

SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]
RANKS = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

deck = create_deck(SUITS, RANKS)

print deck
# [('Clubs', 'Ace'), ('Clubs', '2'), ('Clubs', '3'), ...]     4 * 13 = 52 cards

from random import shuffle

shuffle(deck)

print deck
# [('Clubs', '6'), ('Spades', '3'), ('Hearts', '3'), ...]  still 52 cards, but now in random order

#############################################################################################################

# TODO write a function which returns number of lines in file
def number_of_lines(file):
    return 0 # <- this to be replaced by your code - HINT: open the file end loop (using for loop) through lines

print number_of_lines("lorem_ipsum.txt")
# 8

# TODO write a function which returns number of lines in file
def number_of_words(file):
    return 0 # <- this to be replaced by your code - HINT: try this method of string: "aa a aaa".split()

print number_of_words("lorem_ipsum.txt")
# 87

# TODO write a function which returns number of lines in file
def number_of_characters(file):
    return 0 # <- this to be replaced by your code - HINT: use len("aa a aaa")

print number_of_characters("lorem_ipsum.txt")
# 593

#############################################################################################################
