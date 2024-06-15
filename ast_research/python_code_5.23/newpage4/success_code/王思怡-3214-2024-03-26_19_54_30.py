a = list(eval(input()))
b = []
c = []
for x in a:
    if x != 0:
        b.append(x)
    else:
        c.append(x)
print(b+c)
