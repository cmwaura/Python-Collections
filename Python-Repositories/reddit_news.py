__author__ = 'crispus'
from colorama import *
import praw
import subprocess as sp

'''aim of these script is to take all of my favorite subreddits and
present them on my python idle. Here I will begin by letting the user
pick a decision among a list and then display the results that the user
is waiting for'''

name = ["funny", "news", "worldnews", "Fitness", "All"]
# header = "welcome to subreddit."
print("-"*100)
print("WELCOME TO PY.REDDIT ")
print("-"*100)
print("please make a decision between ")
print("1. R/Funny")
print("2. R/news")
print("3. R/Worldnews")
print("4. R/Fitness")
print("5. R/All")
print("-"*100)
print("-"*100)
question = input(str("Please choose one: "))
# calling a subprocess to clear the command line screen.
tmp = sp.call('cls', shell=True)

class RedditPraw:
    global name

    def __init__(self):
        pass

    def run(self, namer):

        r = praw.Reddit(user_agent= 'news_reader')
        submissions = r.get_subreddit(str(namer)).get_top_from_day(limit=30)
        submission_form = "{}) {} : {} <{}>"
        count = 1
        text = "top 30 posts from your favorite subreddit"
        print(Back.WHITE+ Fore.BLACK +  text)
        print('-' * 30)
        for sub in submissions:
            print(submission_form.format(count, sub.ups, sub.title, sub.url))
            count += 1

    def truncation(self):
        reddit = RedditPraw()
        print(reddit.run(str(name[int(question)])))


def main():
    global question
    try:

        if question == "1":
            question = int(question)
            question -= 1
            RedditPraw().truncation()
        elif question == "2":
            question = int(question)
            question -= 1
            RedditPraw().truncation()
        elif question == "3":
            question = int(question)
            question -= 1
            RedditPraw().truncation()
        elif question == "4":
            question = int(question)
            question -= 1
            RedditPraw().truncation()
        elif question == "5":
            question = int(question)
            question -= 1
            RedditPraw().truncation()
        else:
            pass
    except:
        pass
if __name__ == '__main__':
    main()



