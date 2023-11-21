mat = [[5,7,9,2,1,9],
       [5,3,4,0,0],
       [3,7,0,8,9],
       [0,0,5,5,5,5,5,5]]

count = 0
for row in mat :
    for item in row :
        if( item == 5 ):
            count = count + 1
print( count )

count = 0
for row in mat :
    for item in row :
        if( item == 12 ):
            count = count + 1
print( count )

count = 0
for row in mat :
    for item in row :
        if( item == 7 ):
            count = count + 1
print( count )

count = 0
for row in mat :
    for item in row :
        if( item == 0 ):
            count = count + 1
print( count )