mat = [[5,7,9,2,1,9],
       [5,3,4,0,0],
       [3,7,0,8,9],
       [0,0,]]

count = 0
for r in range( 0 , len(mat), 1 ):
    for c in range( 0, len(mat[r]), 1 ) :
        if mat[r][c] == 5 :
            count = count + 1

print( count )


count = 0
for r in range( 0 , len(mat), 1 ):
    for c in range( 0, len(mat[r]), 1 ) :
        if mat[r][c] == 0 :
            count = count + 1

print( count )

count = 0
for r in range( 0 , len(mat), 1 ):
    for c in range( 0, len(mat[r]), 1 ) :
        if mat[r][c] == 1 :
            count = count + 1

print( count )

count = 0
for r in range( 0 , len(mat), 1 ):
    for c in range( 0, len(mat[r]), 1 ) :
        if mat[r][c] == 12 :
            count = count + 1

print( count )