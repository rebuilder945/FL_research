a = input()
b = [0,0,0,0,0]
c = "~!@#$%^&*()_=-/,.?<>;:[]{}|\""
if len(a) >= 8:
        b[3] += 1
for i in a:
    if i.isdigit():
        b[0] += 1
    elif i.islower():
        b[1] += 1
    elif i.isupper():
        b[2] += 1
    elif i in c:
        b[4] += 1
s = 0
for i in b:
    if i > 0:
        s = s+1
print(s)

