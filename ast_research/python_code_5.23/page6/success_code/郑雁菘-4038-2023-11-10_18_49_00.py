A = input()
a,b,c,d = 0,0,0,0
for i in A:
    if "a" <= i <= "z" or "A" <= i <= "Z":
        a += 1
    elif 0 <= int(i) <= 10:
        b += 1
    elif i ==" ":
        c += 1
    else:
        d += 1
print(a,b,c,d)
