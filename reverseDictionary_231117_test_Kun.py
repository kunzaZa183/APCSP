def reverse(dictionary:dict):
    returndict = {}
    for (a,b) in dictionary.items():
        if b in returndict:
            returndict[b].append(a)
        else:
            returndict[b] = [a]
    return returndict

number = int(input("Enter the number of values: "))
dictionary = {}
for i in range(number):
    a,b = map(int,input("Input two values seperated by spaces: ").split())
    dictionary[a] = b
print(reverse(dictionary))