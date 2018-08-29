#!/usr/bin/python
import sys
message ='abaabb4bccccf'


# Complete the compressedString function below.
def compressedString(message):
    retval = ''
    curLetter = ''
    print message
    if len(message) > 10**5:
        sys.exit(1)
    for l in xrange(len(message)):
        count = 1
        if message[l] == curLetter:
            continue
        curLetter = message[l]
        if not curLetter.isalpha():
            print 'invalid char'
            sys.exit(1)

        for i in xrange(l+1,len(message)):
            # start from next letter
            if curLetter==message[i]:
                count+=1
            else:
                break



        print curLetter, count
        if count == 1:
            retval += curLetter
        else:
            retval = retval + curLetter + str(count)
        print 'Message ' + retval

    return retval

compressedString(message)