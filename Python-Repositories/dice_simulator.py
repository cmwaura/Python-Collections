__author__ = 'crispus'
# This is a program which will roll a die for the user and generate a random choice based/
# on the number of dice the user will ask for.

from random import choice, sample
# The die that the user will roll.
dice1=[1,2,3,4,5,6]

#  This will give the user a chance to roll the dice again. It will keep on rolling until the user decides/
# that otherwise and then it will quit.
def decision():

    cont = raw_input("would you like to go for another round? y/n ")
    print cont
    # If the user chooses Y= yes then the dice rolls again asking for the number of times it will roll.
    if cont == "y":
        num_of_dice()

    # If the user says n="No" then the program quits
    if cont=="n":
        print "thanks for playing."
        quit()
    # If the user chooses another choice the program asks him to choose the right specifications
    else:
        print "please choose between y/n"
        decision()

# Asking the user to choose the number of dice he would allocate to the program between 1 and 4./
# It will then roll the dice, print the results and redirect you to repeat if needed.
def num_of_dice():

    die_no= input("please choose the number of die you would like to use [1-4] ")
    # return int(die_no)
    if die_no > 0 and die_no <= 4:
        sim = [choice(dice1) for items in xrange(die_no)]
        print sim
        decision()
        #
    else:
        print "please check the specifications[1-4] and roll again"
        print "*"*58
        print "-"*58
        num_of_dice()





num_of_dice()
