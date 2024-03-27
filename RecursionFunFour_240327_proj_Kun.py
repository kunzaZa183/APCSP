def countodd(num:str):
    if len(num) == 0:
        return 0
    if (int(num[0])) %2 ==1:
        return  int(num[0]) + countodd(num[1:])
    return countodd(num[1:])

print(countodd("3212123"))
print(countodd("12345"))
print(countodd("777"))
print(countodd("33"))
print(countodd("0"))
print(countodd("222"))