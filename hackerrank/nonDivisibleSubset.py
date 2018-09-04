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

    All of the given numbers are distinct.

Output Format

Print the size of the largest possible subset ().
'''

from itertools import combinations

def nonDivisibleSubset(k, S):

    retVal = []

    print 'There will be ' + str(2**len(S)) + ' subsets to iterate'

    # TODO - figure out more efficient approach
    # generating all subsets first is probably not necessary
    # could attempt to find all pairs of numbers that sum % k == 0
    # and then return subsets of size (len(S) - 1), check for the two numbers
    # if present - reduce size of subset



    for subset in combinations(S, len(S) - 1):
        validSubset = True
        for (p1,p2) in getBadCombos(S,k):
            print((p1,p2))
            if set((p1,p2)).issubset(set(subset)):
                continue

    return 0




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

def getBadCombos(S,k):

    # get all two number combinations that sum with % k == 0
    retVal =[]
    combosRemain = True
    combos = combinations(S,2)
    while combosRemain:
        try:
            c = next(combos)
            if sum(c) % k == 0:
                retVal.append(c)
        except StopIteration:
            #print('Hit end of iterator')
            combosRemain = False
    return retVal

S = [278, 576, 496, 727, 410, 124, 338, 149, 209, 702, 282, 718, 771, 575, 436]
#S = [278, 576, 496, 727, 410, 124, 338, 149,209]

S = [1,7,2,4]
k = 3
nonDivisibleSubset(k,S)

