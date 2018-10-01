#!/usr/bin/python

'''
https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting
profiling was the key in figuring out the timeouts
 python -m cProfile  fraudulant.py

'''
from bubbleSort import myBubbleSort
import math
import bisect

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

def insertInOrder(a,l):
    '''

    :param a: sorted array
    :param l: element to insert
    :return: sorted array a including l
    This is too slow for the purposes of the hackerrank challenge. See comments below.
    '''

    if l >= a[len(a)-1]:
        a.append(l)
        return a

    elif l <= a[0]:
        a.insert(0,l)
        return a

    middleIndex =  int(math.floor( len(a) / 2.0))

    if l < a[ middleIndex ]:
        startingIndex = 0
    else:
        startingIndex = middleIndex

    for i in xrange(startingIndex,len(a)):

        if l <= a[i]:
            a.insert(i,l)
            return a

        elif l > a[i] and l < a[i+1]:
            a.insert(i+1,l)
            return a

def activityNotifications(expenditure, d):
    '''
    expenditure: an array of integers representing daily expenditures
    d: an integer, the lookback days for median spending
    '''

    alerts = 0
    l = d
    curExp = expenditure[l - d:l]
    curExp = sorted(curExp)

    while l < len(expenditure):

        today = expenditure[l]
        median = getMedian(curExp)
        if today >= 2 * median:
            alerts+=1

        '''
        When it comes to inserting and removing from the list, the simple remove() method and method insertInOrder() 
        from above are too expensive and together count for about 98% of the run time.
        Using the appropriate methods from the bisect module reduces the run time from 100s to 2s for size 200000
        '''
        #curExp.remove(expenditure[l-d])
        indexToRemove = bisect.bisect_left(curExp,expenditure[l-d])
        curExp.pop(indexToRemove)

        # insert next element into the already sorted list
        #curExp = insertInOrder(curExp,expenditure[l])
        bisect.insort(curExp,expenditure[l])
        l+=1
    return alerts

p = [5,8,9,6,4,7,7,55,7,8,7,4,34,7,44,8,11,2,66,9,45,64,32,32,32]
e = [2, 3, 4, 2, 3, 6, 8, 4, 5]
f = [10, 20 , 30 ,40, 50]

fh = open('input01.txt')
fd = fh.read().split('\n')
data = map(int, fd[1].split())
fh.close()
print len(data)

activityNotifications(data,10000)
#activityNotifications(p,10)
#print insertInOrder(sorted(p),12,7)




