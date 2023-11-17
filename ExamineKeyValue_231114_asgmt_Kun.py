""" To examine every key and every value use the .items function"""
dictionary = {0:"zero", 1:"one", 2:"two"}
for i in dictionary.items():
    print(i[0],i[1])
""" To check if a key already exists in a dictionary, use the keyword in."""
print(0 in dictionary)
print(3 in dictionary)