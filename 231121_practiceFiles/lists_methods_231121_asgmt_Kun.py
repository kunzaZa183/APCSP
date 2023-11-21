mat = [[5,7,9,2,1,9],
       [],
       [0,0,]]

print(mat)

mat[1].append(4)
mat.append([7,7,7])

print(mat)

mat.insert(1,[3])

print(mat)

mat.pop(0)

print( mat )

mat[2].remove(0)

print( mat )



mat.insert(3, [3, 8, 9])

print(mat)

mat.pop(1)

print( mat )

mat[0].remove(3)

print( mat )


"""

[[5, 7, 9, 2, 1, 9], [], [0, 0]]
[[5, 7, 9, 2, 1, 9], [4], [0, 0], [7, 7, 7]]
[[5, 7, 9, 2, 1, 9], [3], [4], [0, 0], [7, 7, 7]]
[[3], [4], [0, 0], [7, 7, 7]]
[[3], [4], [0], [7, 7, 7]]


"""
