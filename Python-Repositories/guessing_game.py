__author__ = 'crispus'
from random import choice
x = range(1,100)
print x
y = choice(x)
# print y

brackets=[]

def guess_the_number():

    while True:
        answer = input("would you like to guess what number the computer chose? " )
        brackets.append(answer)
        if answer == y:
            print "you got it and it only took you " + str(len(brackets)) + " tries "
            print "your guesses were",brackets
            break
        elif answer > y:
            print "try lower"
        else:
            print "try higher"



guess_the_number()


