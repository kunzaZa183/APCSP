"""If a key already exists in a dictionary, the corresponding value will be replaced"""
dictionary = {0:"zero", 1:"one", 2:"two"}
dictionary.update({1:"something"})
print(dictionary)
"""If a value already exists, then it doesn't really matter becasue a new key will be created with that value anyways."""
dictionary.update({3:"something"})
print(dictionary)