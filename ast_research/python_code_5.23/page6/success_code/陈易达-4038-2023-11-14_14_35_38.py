a = input()
n1 = 0
n2 = 0
n3 = 0
n4 = 0
for x in a:
    if x.isupper() or x.islower():
        n1 += 1
    elif x.isspace():
        n2 += 1
    elif x.isdigit():
        n3 += 1
    else:
        n4 += 1
print(n1,n2,n3,n4)
