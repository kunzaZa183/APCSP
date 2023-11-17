"""Check is the values are unique"""
def is_1_to_1(dictionary):
    #sort all the values and store in a list
    lst = sorted(dictionary.values())

    #check if adjacent values are the same
    for i in range(len(lst) - 1):
        if lst[i] == lst[i + 1]:
            return False
    return True
dict1 = {"one":"1", "two":"2", "three":"3"}
dict2 = {"Stars":"2", "Bar":"2"}
dict3 = {"APCSP":"easy", "AP Stats":"easy", "AP World":"difficult"}
dict4 = {"Elementary":"5", "Middle School":"3", "High School":"4"}
dict5 = {"Oly":"The universe, the meaning of life", "Kun":"So you see,", "Punn":"German"}

print(is_1_to_1(dict1))
print(is_1_to_1(dict2))
print(is_1_to_1(dict3))
print(is_1_to_1(dict4))
print(is_1_to_1(dict5))