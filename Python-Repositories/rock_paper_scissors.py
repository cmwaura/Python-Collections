### this is the better version of the rock paper scisors game modified on 08/12/2015.

from random import choice

n =["rock", "paper", "scissors"]
print "_"*25
print "these are your choices:"
print "_"*25
for item in n:
    print str(item)
# print "_"*25




def game():

    if comp_choice == "scissors":
        print "rock beats scissors"
    elif comp_choice == "paper":
        print "you lost"
    elif comp_choice == "rock":
        print "this is a tie game"
    else:
        print "there is a bug in the system"
    cont()

def mache():

    if comp_choice == "scissors":
        print "you lost"
    elif comp_choice== "rock":
        print "paper covers rock, congrats"
    elif comp_choice== "paper":
        print "this is a tie game"
    else:
        print "there is a bug in the system"
        main()

def chop():

    if comp_choice == "rock":
        print "rock beats scissors"
    elif comp_choice== "paper":
        print "scissors cuts paper, you won."
    elif comp_choice== "scissors":
        print "this is a tie game"
    else:
        print "there is a bug in the system"
        main()
def cont():
    print "_"*25
    print "would you like to continue?"
    print "type 'yes' or 'no'"
    reply= raw_input("choice ")
    comp_choice = choice(n)
    if reply == "yes":

        main()
    else:
        print "see ya later, alligator"
def main():
    comp_choice = choice(n)

    print comp_choice
    answer = raw_input("please make your decision:  ")
    # print comp_choice
    if answer in n:
        if answer =="rock":

            game()
        elif answer == "paper":

            mache()
        elif answer == "scissors":

            chop()
    else:
        print "you chose an answer not in the list"
        main()


main()


