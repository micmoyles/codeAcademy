#!/usr/bin/python

'''
Given a set of distinct integers, print the size of a maximal subset of where the sum of any numbers in is not evenly divisible by .

For example, the array and . One of the arrays that can be created is . Another is . After testing all permutations, the maximum length solution array has elements.

Function Description

Complete the nonDivisibleSubset function in the editor below. It should return an integer representing the length of the longest subset of meeting the criteria.

nonDivisibleSubset has the following parameter(s):

    S: an array of integers
    k: an integer

Input Format

The first line contains space-separated integers, and , the number of values in and the non factor.
The second line contains space-separated integers describing , the unique values of the set.

Constraints

    1 <= n <= 10**5
    1 <= k <= 100
    1 <= S[i] <= 10**9
    All of the given numbers are distinct.

Output Format

Print the size of the largest possible subset ().
'''

import sys
from itertools import combinations

def nonDivisibleSubset(k, S):

    '''
    Check constraints
    '''
    if len(S) >= 10 ** 5:
        print('Length too long.')
        sys.exit(1)
    if k >= 100 or k < 1:
        print('Invalid value for k.')
        sys.exit(1)
    if list(filter( lambda s: s >= 10 ** 9,S)):
        print('An element of S is too large')
        sys.exit(1)
    delta = 1

    print 'There would be ' + str(2**len(S)) + ' subsets to iterate'

    '''
    The approach is to:
    1) Find all combinations that we do not want in our subset
    2) Use a generator to call subsets starting with the largest (len(S) - 1)
    3) If a subset matches our condition then exit and return the length of the subset
    4) If not, call another subset
    5) When the generator ends, we decrease the size of the subset and create a new generator
    '''

    pairs = getBadCombos(S,k)

    print(pairs)

    while delta < len(S):
        print('Operating with subset size max - ' + str(delta))
        for subset in combinations(S, len(S) - delta):
            res = [x for x in pairs if x.issubset(subset)]
            if not res:
                print('Subset ' + str(subset) + ' does not contain any two numbers with a sum divisble by ' + str(k))
                return len(subset)

        '''
        if we reach this point then no subsets matching our conditions were found so we reduce the size of the subsets
        we are testing and recall the generator
        '''

        delta += 1

    return 0

def getBadCombos(S,k):

    # get all two number combinations that sum with % k == 0

    retVal =[]
    combosRemain = True
    combos = combinations(S,2)
    while combosRemain:
        try:
            c = next(combos)
            if sum(c) % k == 0:
                retVal.append(set(c))
        except StopIteration:
            combosRemain = False
    return retVal



def checkPermutations(k, S):
    '''
    :param k: integer
    :param S: array
    :return: True if no two elements sum with % k == 0
    '''
    S = list(S)

    for i in xrange(len(S)):
        for j in xrange(len(S)):

            if j == i:
                continue
            if (S[i] + S[j]) % k == 0:
                return False

    return True

def getSubSets(s, exactSize = None):

    # largest subset
    max = len(s)
    size = 2 # size starts at 2 because we do not need to loop over 1 element subsets

    # first add all single elements
    retVal = [{x} for x in s]

    # next step to add all subsets with 2<=size<len(s)
    # get all two element subsets
    # take each two element subset and add one element to get the three element subsets
    # repeat

    while size < max:
        R = [x for x in retVal if len(x) == size - 1 ]
        for r in R:
            # ie get two element arrays when we are creating 3 element arrays
            for i in xrange(len(s)):
                #print 'Element ' + str(s[i])
                if s[i] not in r:

                    f = r

                    newElement = f | set([s[i]])
                    if newElement not in retVal:
                        retVal.append( newElement )

        size += 1

    return retVal



S = [278, 576, 496, 727, 410, 124, 338, 149, 209, 702, 282, 718, 771, 575, 436]
#S = [278, 576, 496, 727, 410, 124, 338, 149,209]

#S = [1,7,2,4]
k = 17
S = [19,10,12,10,24,25,22]
k = 4
ans = nonDivisibleSubset(k,S)
print ans

