# sum up all values in the list of lists that are
# greater than the first value in the lists of lists
# return -1 if the list of lists is empty 
# or no values are greater than the first value

def sumFirst( mat ):
    if len(mat) == 0:
        return -1
    has = 0
    sum = 0
    firstnum = mat[0][0]
    for i in mat:
        for j in i:
            if j > firstnum:
                has = 1
                sum += j
    if has:
        return sum
    return -1 


print ( sumFirst( [[1,2],[3,4,5]] ) )
print ( sumFirst( [[99,2,3],[3,4,5],[3,3]] ) )
print ( sumFirst( [[1,2,3],[3,4,5],[3,3]] ) )
print ( sumFirst( [[1]] ) )
print ( sumFirst( [[2],[3]] ) )
print ( sumFirst( [[1],[2],[3],[4],[5]] ) )
print ( sumFirst( [[1,2],[3,-4,5],[5,6,-7,8,9,0]] ) )
print ( sumFirst( [[7,2]] ) )
print ( sumFirst( [[2,2,2,2,2],[3,5,6,7,8,9]] ) )
print ( sumFirst( [[1],[2,0,-55],[3],[4,3,4],[5,3]] ) )
print( sumFirst( [] ))