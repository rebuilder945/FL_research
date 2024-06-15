a = list(eval(input()))
b = a.copy()
b.sort()
c=[]
for i in a:
    if i!=b[0] and i!=b[-1]:
        c.append(i)

print(c)
