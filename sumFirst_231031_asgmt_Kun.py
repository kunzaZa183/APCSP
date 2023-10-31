def go(lst):
    if len(lst) == 0:
        return -1
    have = False
    for i in lst:
        if i > lst[0]:
            have = True
    if not have:
        return -1
    sum = 0
    for i in lst:
        if i > lst[0]:
            sum += i
    return sum


print ( go( [-99,1,2,3,4,5,6,7,8,9,10,5] ) )
print ( go( [10,9,8,7,6,5,4,3,2,1,-99] ) )
print ( go( [10,20,30,40,50,-11818,40,30,20,10] ) )
print ( go( [32767] ) )
print ( go( [255,255] ) )
print ( go( [9,10,-88,100,-555,2] ) )
print ( go( [10,10,10,11,456] ) )
print ( go( [-111,1,2,3,9,11,20,1] ) )
print ( go( [9,8,7,6,5,4,3,2,0,-2,6] ) )
print ( go( [12,15,18,21,23,1000] ) )
print ( go( [250,19,17,15,13,11,10,9,6,3,2,1,0] ) )
print ( go( [9,10,-8,10000,-5000,-3000] ) )


