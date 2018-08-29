#!/usr/bin/python

def getSubStrings(s):
    startingPoint = 0
    max = len(s) - 1
    retVal = []
    while startingPoint < max:
        for i in xrange(1,len(s)+1):
            substr = s[startingPoint:i]
            if substr:
                retVal.append(substr)
        startingPoint+=1
    retVal.append(s[max])
    return set(retVal)

def reverseString(s):
    reversedString = ''
    sList = list(s)
    sList.reverse()
    for letter in sList:
        reversedString+=letter
    print reversedString

getSubStrings('Teresa')
reverseString('Michael')