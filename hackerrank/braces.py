#!/usr/bin/python

def braces(values):

    retVal = []
    res = ''

    for val in values:
        print val, len(val)
#        if len(val) % 2 != 0:
        if not checkLength(val):
            # if the length is odd then we must contain at least one unclosed brace
            res = 'NO'
            print 'Odd length'
        elif not checkCounts(val):
        #elif (val.count('{') != val.count('}')) or (val.count('[') != val.count(']')) or (
        #                val.count('(') != val.count(')')):
            # counts do not match so we can return no immediately
            print 'Counts do not match'
            res = 'NO'

        else:

            print 'Checking open braces'
            # catch open braces in nested braces
            for l in xrange(len(val)):
                substr = ''
                v = val[l]
                print 'starting with ' + v
                if v == '{': closer = '}'
                if v == '(': closer = ')'
                if v == '[': closer = ']'

                for i in xrange(l,len(val)):
                    if val[i] == closer:
                        # generate substring to check
                        substr = val[l:i+1]
                        print 'Found Substring : ' + substr
                        if not checkLength(substr):
                            res = 'NO'
                            print 'Substring length fails'
                            break
                        elif not checkCounts(substr):
                            res = 'NO'
                            print 'Substring count check fails'
                            break


        retVal.append(res)
    return retVal

def checkCounts(s):

    if (s.count('{') != s.count('}')) or (s.count('[') != s.count(']')) or (
            s.count('(') != s.count(')')):
        return False
    else:
        return True

def checkLength(s):
    if len(s) % 2 == 0:
        return True
    else:
        return False



b = braces(['{[}]()'])
print b
