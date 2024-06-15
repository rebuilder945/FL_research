a=eval(input())
b=[]
for x in a:
    c=x
    a.remove(x)
    if c in a:
        continue
    else:
        b.append(c)
print(b)


