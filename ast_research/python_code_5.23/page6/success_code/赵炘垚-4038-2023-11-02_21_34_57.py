s = input()
a = 0
b = 0
c = 0
d = 0
for i in s:
    if i.isalpha():
        a += 1
    elif i.isnumeric():
        b += 1
    elif i ==" ":
        c += 1
    else:
        d += 1

print(a,c,b,d)
