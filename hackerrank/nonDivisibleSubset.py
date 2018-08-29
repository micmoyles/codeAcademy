#!/usr/bin/python

def nonDivisibleSubset(k, S):
    pass


def getPermutations(k, S):
    '''
    :param k: integer
    :param S: array
    :return: array of combinations s1,s2 where s1+s2 % k == 0
    '''
    retVal= []
    for i in xrange(len(S)):
        for j in xrange(i+1,len(S)):
            print str(S[i]) + ' + ' + str(S[j])
            if (S[i] + S[j]) % k == 0:
                retVal.append([S[i],S[j]])
    print retVal

def getSubSets(s):

    startingPoint = 0

    # largest subset
    max = len(s) - 1

    # first add all single elements
    retVal = [[x] for x in s]

    # next step to add all subsets with 2<=size<len(s)
    while startingPoint < max:
        for i in xrange(1,len(s)+1):
            substr = s[startingPoint:i]
            if substr:
                retVal.append(substr)
        startingPoint+=1

    retVal.append([s[max]])
    return retVal

S = [1,5,9,8]
k = 5
print getSubSets(S)
