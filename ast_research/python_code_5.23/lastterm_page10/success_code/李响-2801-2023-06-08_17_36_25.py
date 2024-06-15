a = input()
b = [0,0,0,0,0]
c = "~!@#$%^&*()_=-/,.?<>;:[]{}|\""
for i in a:
    if a[i].isdigit():
        b[0] += 1
    elif a[i].islower():
        b[1] += 1
    elif a[i].isupper():
        b[2] += 1
    elif len(a) >= 8:
        b[3] += 1
    elif a[i] in c:
        b[4] += 1
s = 0
for i in b:
    if b[i] > 0:
        s = s+1
print(s)

