s = input()
a,b,c,d = 0,0,0,0
for x in s:
    if x.isalpha:
        a = a + 1
    elif x.isspace:
        b = b + 1
    elif x.isdight:
        c = c + 1
    else:
        d = d + 1
print(a,b,c,d)

