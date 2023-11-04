def noRepeats( incomingList :list):
    incomingList.sort()
    for i in range(len(incomingList) - 1):
        if incomingList[i] == incomingList[i+1]:
            return False
    return True


print ( noRepeats( [-99,1,2,3,4,5,6,6,6,6,6,7,8,9,10,12345,5,5,5,5] ) )
print ( noRepeats( [10,9,8,7,6,5,4,3,2,1,-99] ) )
print ( noRepeats( [10,20,30,40,50,10,10,40,30,20,10] ) )
print ( noRepeats( [32767] ) )
print ( noRepeats( [255,255] ) )
print ( noRepeats( [9,10,-88,100,-555,1000] ) )
print ( noRepeats( [10,10,10,11,456,10,10,2,2,2,2,2,2,2] ) )
print ( noRepeats( [-111,1,2,3,9,11,20,30] ) )
print ( noRepeats( [9,8,7,6,5,4,3,2,0,-2,-989] ) )
print ( noRepeats( [12,12,15,18,21,23,1000] ) )
print ( noRepeats( [250,19,17,15,13,13,13,13,11,10,9,6,3,2,1,1] ) )
print ( noRepeats( [9,10,-8,10000,-5000,1000] ) )