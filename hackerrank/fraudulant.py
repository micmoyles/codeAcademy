#!/usr/bin/python

'''
https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting
'''
from bubbleSort import myBubbleSort
import math

def getMedian(l, needToSort = False):
    if needToSort:
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

def insertInOrder(a,l, currentMedian = None):
    print 'Inserting ' + str(l) + ' into '+str(a)
    if l >= a[len(a)-1]:
        a.append(l)
        print 'Leaving at 1'
        return a
    elif l <= a[0]:
        a.insert(0,l)
        print 'Leaving at 2'
        return a
    print 'Starting loops'

    if currentMedian is None or l <= currentMedian:
        startingIndex = 0
    else:
        startingIndex = int(math.floor( len(l) / 2.0 ))

    for i in xrange(startingIndex,len(a)):

        if l == a[i]:
            a.insert(i,l)
            print 'Leaving at 3'
            return a
        elif l > a[i] and l < a[i+1]:
            a.insert(i+1,l)
            print 'Leaving at 4'
            return a

def activityNotifications(expenditure, d):
    '''
    expenditure: an array of integers representing daily expenditures
    d: an integer, the lookback days for median spending
    '''
    print expenditure

    alerts = 0
    l = d
    curExp = expenditure[l - d:l]
    curExp = sorted(curExp)

    while l < len(expenditure):
    #for l in xrange(d,len(expenditure)):
        # in array [a b c d e f] we want to choose e and get the median of [a b c d]
        #curExp = expenditure[l-d:l]

        today = expenditure[l]
        print today, curExp, getMedian(curExp)
        if today >= 2 * getMedian(curExp):
            alerts+=1
            print 'Alert Issued'

        # remove first element
        #print 'Butchering'
        #print curExp
        curExp.pop(0)
        #print curExp
        # insert next element into the already sorted list
        curExp = insertInOrder(curExp,expenditure[l])
        #print curExp
        l+=1

p = [5,8,9,6,4,7,7,55,7,8]
e = [2, 3, 4, 2, 3, 6, 8, 4, 5]
f = [10, 20 , 30 ,40, 50]
#activityNotifications(e,5)
print insertInOrder(sorted(p),0)




