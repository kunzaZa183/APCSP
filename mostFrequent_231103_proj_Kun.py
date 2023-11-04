def mostFrequent( incomingList :list):
    maxcount = 0
    maxnum = -1
    for i in incomingList:
        if incomingList.count(i)>maxcount:
            maxcount = incomingList.count(i)
            maxnum = i
    return maxnum


print ( mostFrequent( [-99,1,2,3,4,5,6,6,6,6,6,7,8,9,10,12345,5,5,5,5] ) )
print ( mostFrequent( [10,9,8,7,6,5,4,3,2,1,-99] ) )
print ( mostFrequent( [10,20,30,40,50,10,10,40,30,20,10] ) )
print ( mostFrequent( [32767] ) )
print ( mostFrequent( [255,255] ) )
print ( mostFrequent( [9,10,-88,100,-555,1000] ) )
print ( mostFrequent( [10,10,10,11,456,10,10,2,2,2,2,2,2,2] ) )
print ( mostFrequent( [-111,1,2,3,9,11,20,30] ) )
print ( mostFrequent( [9,8,7,6,5,4,3,2,0,-2,-989] ) )
print ( mostFrequent( [12,12,15,18,21,23,1000] ) )
print ( mostFrequent( [250,19,17,15,13,13,13,13,11,10,9,6,3,2,1,1] ) )
print ( mostFrequent( [9,10,-8,10000,-5000,1000] ) )