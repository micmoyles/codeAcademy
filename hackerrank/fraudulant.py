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

def insertInOrder(a,l):

    print 'Inserting ' + str(l) + ' into '+ str(a)
    if l >= a[len(a)-1]:
        a.append(l)
        print 'Inserted at very end'
        return a

    elif l <= a[0]:
        a.insert(0,l)
        print 'Inserted at very front'
        return a

    print 'Starting loops'
    middleIndex =  int(math.floor( len(a) / 2.0))

    if l < a[ middleIndex ]:
        startingIndex = 0
    else:
        print 'Will work with second half from index %d' % middleIndex
        startingIndex = middleIndex

    print 'Starting Index: %d' % startingIndex
    for i in xrange(startingIndex,len(a)):

        if l <= a[i]:
            a.insert(i,l)
            print 'Inserting %d into element %d of array' % (l,i)
            print str(a)
            return a
        elif l > a[i] and l < a[i+1]:
            print 'Inserting %d between %d and %d' % (l,a[i],a[i+1])
            a.insert(i+1,l)

            print str(a)
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

        today = expenditure[l]
        print 'Today: ' + str(today) + ' Median: ' + str(getMedian(curExp)) + ' curExp: ' + str(curExp)
        median = getMedian(curExp)
        if today >= 2 * median:
            alerts+=1
            print 'Alert Issued'
        else:
            print 'No alert issued'

        #curExp.pop(0) #<- This is incorrect as it is removing the smallest element when it should be removing
        # the element from d days ago.
        print 'Removing %d ' % expenditure[l-d]
        curExp.remove(expenditure[l-d])
        # insert next element into the already sorted list
        curExp = insertInOrder(curExp,expenditure[l])
        #print curExp
        l+=1

p = [5,8,9,6,4,7,7,55,7,8,7,4,34,7,44,8,11,2,66,9,45,64,32,32,32]
e = [2, 3, 4, 2, 3, 6, 8, 4, 5]
f = [10, 20 , 30 ,40, 50]
activityNotifications(p,10)
#print insertInOrder(sorted(p),12,7)




