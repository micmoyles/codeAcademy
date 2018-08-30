#!/usr/bin/python

def nonDivisibleSubset(k, S):
    retVal = []
    # getall subsets
    subSets = getSubSets(S)
    assert len(subSets) == 2**len(S) - 2, 'Unexpected number of subsets returned'

    # for each subset, add all combinations of two elements
    # if any two are evenly divisble by k then that subset fails
    print subSets
    for subSet in subSets:
        if len(subSet) == 1:
            print 'Removing'
            print subSet
            subSets.remove(subSet)
        else:
            print subSet
            print '--------------'
            if checkPermutations(k,subSet):
                retVal.append(subSet)
    return retVal


def checkPermutations(k, S):
    '''
    :param k: integer
    :param S: array
    :return: True if no two elements sum with % k == 0
    '''
    check = True
    S = list(S)
    for i in xrange(len(S)):
        for j in xrange(len(S)):
            if j == i: continue
            print str(S[i]) + ' + ' + str(S[j])
            if (S[i] + S[j]) % k == 0:
                return False

    return True

def getSubSets(s):

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

        for r in [x for x in retVal if len(x) == size - 1 ]:
            #print 'Looking at '
            #print r
            # ie get two element arrays when we are creating 3 element arrays
            for i in xrange(len(s)):
                #print 'Element ' + str(s[i])
                if s[i] not in r:
                    f = r
                    #print 'Adding ' + str(s[i]) + ' to '
                    #print r,f
                    #print retVal

                    #print retVal
                    newElement = f | set([s[i]])
                    if newElement not in retVal:
                        retVal.append( newElement )
                    #print retVal

        size += 1

    return retVal

S = [1,7,2,4]
k = 3
print nonDivisibleSubset(k,S)

