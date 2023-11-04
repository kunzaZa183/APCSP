def getLast( incomingList ):
    finalList = []
    for i in incomingList:
        if i > incomingList[-1]:
            finalList.append(i)
    return finalList


print ( getLast( [-99,1,2,3,4,5,6,7,8,9,10,5] ) )
print ( getLast( [10,9,8,7,6,5,4,3,2,1,-99] ) )
print ( getLast( [10,20,30,40,50,-11818,40,30,20,10] ) )
print ( getLast( [32767] ) )
print ( getLast( [255,255] ) )
print ( getLast( [9,10,-88,100,-555,2] ) )
print ( getLast( [10,10,10,11,456] ) )
print ( getLast( [-111,1,2,3,9,11,20,1] ) )
print ( getLast( [9,8,7,6,5,4,3,2,0,-2,6] ) )
print ( getLast( [12,15,18,21,23,1000] ) )
print ( getLast( [250,19,17,15,13,11,10,9,6,3,2,1,0] ) )
print ( getLast( [9,10,-8,10000,-5000,-3000] ) )

