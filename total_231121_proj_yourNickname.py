# sum up all values in ann
# return the sum of all values in ann

def sumMatrix(mat):
    sum = 0
    for i in mat:
        for j in i:
            sum += j
    return sum


print ( sumMatrix( [[1,2],[3,4,5]] ) )
print ( sumMatrix( [[99,2,3],[3,4,5],[3,3]] ) )
print ( sumMatrix( [[1,2,3],[3,4,5],[3,3]] ) )
print ( sumMatrix( [[1]] ) )
print ( sumMatrix( [[2],[3]] ) )
print ( sumMatrix( [[1],[2],[3],[4],[5]] ) )
print ( sumMatrix( [[1,2],[3,-4,5],[5,6,-7,8,9,0]] ) )
print ( sumMatrix( [[7,2]] ) )
print ( sumMatrix( [[2,2,2,2,2],[3,5,6,7,8,9]] ) )
print ( sumMatrix( [[1],[2,0,-55],[3],[4,3,4],[5,3]] ) )
