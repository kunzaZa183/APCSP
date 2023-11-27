#change filename
filename = "ratings.txt"

alltokens = open(filename, "r").read().split("\n")

# Data cleanup
alltokens.pop()
for i in range(len(alltokens)):
    while alltokens[i][-1] == " ":
        alltokens[i] = alltokens[i][0:-1]

# Create list of names
allnames = set()
for i in range(0, len(alltokens), 3):
    allnames.add(alltokens[i])
allnames = list(allnames)

# Create list of books
allbooks = set()
for i in range(1, len(alltokens), 3):
    allbooks.add(alltokens[i])
allbooks = list(allbooks)

# Create ratings matrix
ratings = [[0 for i in range(len(allbooks))] for j in range(len(allnames))]

# Add values to ratings matrix
for i in range(0, len(alltokens), 3):
    xval = allnames.index(alltokens[i])
    yval = allbooks.index(alltokens[i + 1])
    ratings[xval][yval] = float(alltokens[i + 2])

# Create average list
averages = []
for i in range(len(allbooks)):
    sum = 0
    ct = 0
    for j in range(len(allnames)):
        sum += ratings[j][i]
        if ratings[j][i] != 0:
            ct += 1
    averages.append((sum / ct, allbooks[i]))
averages.sort(reverse=True)

# Introduction
print(
    """Welcome to the ICS AP CA Principles Book Recommendation System.
Type the word in the left column to do the action on the right.

recommend : recommend books for a particular user
averages : output the average ratings of all books in the system
quit : exit the program
"""
)


def printlist(lst):
    for a, b in lst:
        print(b, a)


while True:
    command = input("Next Task? ")
    if command == "quit":
        exit()
    if command == "averages":
        printlist(averages)
    elif command == "recommend":
        name = input("\nUser? ")
        if allnames.count(name) == 0:
            print()
            printlist(averages)
        else:
            similarList = []
            index = allnames.index(name)
            for i in range(len(allnames)):
                if i != index:
                    val = 0
                    for j in range(len(allbooks)):
                        val += ratings[index][j] * ratings[i][j]
                    similarList.append((val, i))
            similarList.sort(reverse=True)

            while len(similarList) > 3:
                similarList.pop()

            bookList = []
            for i in range(len(allbooks)):
                sum = 0
                ct = 0
                for val, index in similarList:
                    if ratings[index][i] != 0:
                        ct += 1
                        sum += ratings[index][i]
                if ct > 0:
                    bookList.append((sum / ct, allbooks[i]))
            bookList.sort(reverse=True)
            print()
            for a, b in bookList:
                if a <= 0:
                    break
                print(b, a)
    print()
