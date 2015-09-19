__author__ = 'crispus'
# practice for basic statistics.
from collections import Counter
def mean():
    l= len(numbers)
    numbersum=0
    for number in numbers:
        numbersum = numbersum + number
        numberaverage= float(numbersum/l)
    return numbersum, numberaverage
def mod():
    data = Counter(numbers)
    print data.most_common()
    print data.most_common(1)#returns the highest repeated number
    # return data
def median():
    sortnum = sorted(numbers)
    middle = len(sortnum)
    #divided the length of the numbers by 2
    med= middle/2
    #if there is no median number, divides the two middle numbers to get
    #the median. Otherwise, returns the median number.
    if not med%2:
        return (sortnum[med-1]+sortnum[med])/2.0

    return sortnum[med]




data = raw_input("Enter your numbers, separated by a space \n  ")
numbers = map(int, data.split())
# print numbers
print mean()
print mod()
print median()