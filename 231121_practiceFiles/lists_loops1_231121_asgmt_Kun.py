mat = [[5,7,9,2,1,9],
       [5,3,4,0,0],
       [3,7,0,8,9],
       [0,0,]]

for r in range( 0 , len(mat), 1 ):
    for c in range( 0, len(mat[r]), 1 ) :
        print( mat[r][c] , end=" " )
    print()

s = 0
for r in mat:
    for e in r:
        s += e
print("Sum of all elements in the matrix:", s)

for i, r in enumerate(mat):
    z = r.count(0)
    print(f"Row {i+1} has {z} zero(s)")

m = float('-inf')
for r in mat:
    for e in r:
        if e > m:
            m = e
print("The maximum value in the matrix is:", m)

