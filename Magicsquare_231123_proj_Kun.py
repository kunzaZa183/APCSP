# Magic Square
# Is it a magic square?


def go(sz, ln):
    # make a new zero filled 2d array
    rows, cols = (sz, sz)
    magic = [[0 for i in range(cols)] for j in range(rows)]

    # load in all of the values from ln
    # into the list of lists
    # nested loops
    ct = 0
    for i in range(sz):
        for j in range(sz):
            magic[i][j] = int(ln[ct])
            ct += 1
    return magic


def isMagicSquare(mat):
    x = sumRow(mat, 0)
    # check all rows
    for i in range(len(mat)):
        if x != sumRow(mat, i):
            return "NOT A MAGIC SQUARE"
    # check all cols
    for i in range(len(mat)):
        if x != sumCol(mat, i):
            return "NOT A MAGIC SQUARE"
    # check the down diag
    if x != sumUpDiag(mat):
        return "NOT A MAGIC SQUARE"
    # check the up diag
    if x != sumDownDiag(mat):
        return "NOT A MAGIC SQUARE"
    return "MAGIC SQUARE"


def sumRow(mat, r):
    sum = 0
    for i in range(len(mat)):
        sum += mat[r][i]
    return sum


def sumCol(mat, c):
    sum = 0
    # sum up col c
    for i in range(len(mat)):
        sum += mat[i][c]
    return sum


def sumDownDiag(mat):
    sum = 0
    # sum up the down diag
    for i in range(len(mat)):
        sum += mat[i][len(mat) - i - 1]
    return sum


def sumUpDiag(mat):
    sum = 0
    # sum the up diag
    for i in range(len(mat)):
        sum += mat[i][i]
    return sum


def to_string(ann):
    # print out the list of lists
    res = ""
    for r in range(0, len(ann)):
        for c in range(0, len(ann)):
            res = res + str(ann[r][c]) + " "
        res = res + "\n"

    return res


f = open("magic1_231123_proj_Kun.dat", "r")

times = int(f.readline())


# read in the data file
for x in range(0, times):
    sz = int(f.readline())
    line = f.readline().split()

    # call go to make a new magic[]
    mat = go(sz, line)
    # print the magic square
    print(to_string(mat), end = "")
    # check the magic square
    print(isMagicSquare(mat))
    print()
