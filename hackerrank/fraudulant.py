#!/usr/bin/python

'''
https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting
'''
from bubbleSort import myBubbleSort
import math

def getMedian(l):
    l = myBubbleSort(l)
    # if length of l is even we take the average of the middle two numbers
    if len(l) % 2 == 0:
        middle1 = len(l) / 2
        middle2 = middle1 - 1
        median = (l[middle1] + l[middle2]) / 2.0
    else:
        middle = int(math.floor( len(l) / 2.0 ))
        median = l[middle]
    return median

def activityNotifications(expenditure, d):
    '''
    expenditure: an array of integers representing daily expenditures
    d: an integer, the lookback days for median spending
    '''
    print expenditure
    for l in xrange(d,len(expenditure)):
        # in array [a b c d e f] we want to choose e and get the median of [a b c d]
        curExp = expenditure[0:l]

        today = expenditure[l]
        print today, curExp, getMedian(curExp)
        if today >= getMedian(curExp): print 'Alert Issued'

p = [5,8,9,6,4,7,7,55,7,8]
e = [2, 3, 4, 2, 3, 6, 8, 4, 5]
activityNotifications(e,5)


