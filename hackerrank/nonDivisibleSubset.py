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

    # this currently does not return a unique list or subsets

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

S = [1,5,9,8,7]
k = 5
ans = getSubSets(S)
print len(ans)
