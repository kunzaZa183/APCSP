#spiral matrix


def matrix( sz ):
  
    #make a new zero filled 2d array  
    arr = [[0 for i in range(sz)] for i in range(sz)]
    #create a spiral matrix
    x = 0; y = 0
    ct = 1
    moved = 1
    while moved:
        moved = 0
        while x < sz and y < sz and x >= 0 and y >= 0:
            if arr[x][y] != 0:
                break
            moved = 1
            arr[x][y] = ct
            ct += 1
            x += 1
        x -= 1
        y += 1
        while x < sz and y < sz and x >= 0 and y >= 0:
            if arr[x][y] != 0:
                break
            moved = 1
            arr[x][y] = ct
            ct += 1
            y += 1
        y -= 1
        x -= 1
        while x < sz and y < sz and x >= 0 and y >= 0:
            if arr[x][y] != 0:
                break
            moved = 1
            arr[x][y] = ct
            ct += 1
            x -= 1
        x += 1
        y -= 1
        while x < sz and y < sz and x >= 0 and y >= 0:
            if arr[x][y] != 0:
                break
            moved = 1
            arr[x][y] = ct
            ct += 1
            y -= 1
        y += 1
        x += 1
    return arr
  


def to_string( ann ) :

    res = ""
    for i in ann:
        for j in i:
            res = res + str(j) + "\t"
        res += "\n"
  
    return res



print ( to_string(matrix( 2 )) )
print ( to_string(matrix( 3 )) )
print ( to_string(matrix( 4 )) )
print ( to_string(matrix( 5 )) )
print ( to_string(matrix( 6 )) )