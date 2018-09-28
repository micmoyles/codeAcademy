def countSwaps(a):
    i = j = count = 0
    while not checkSort(a):
        for j in xrange(0,len(a)-1):
            if a[j] > a[j+1]:
                count+=1
                #print('Looking at %d' % a[j])
                #swap
                #print('Swapping %d and %d' % (a[j],a[j+1]) )
                smaller = a[j+1]
                larger  = a[j]
                a[j]    = smaller
                a[j+1]  = larger
    print('Array is sorted in %d swaps.' % count)
    print('First Element: %d' % a[0])
    print('Last Element: %d' % a[len(a)-1])
def checkSort(a):
    for i in xrange(len(a)-1):
        if a[i] > a[i+1]:
            return False
    return True