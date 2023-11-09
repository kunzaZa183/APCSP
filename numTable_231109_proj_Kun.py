def numtable( m, n ):
    map = {}
    for i in range(1, m):
        map[i] = n * i
    return map
        
print(numtable(10, 5))
print(numtable(11, 8))

print(numtable(4, 17))
print(numtable(3, -18))