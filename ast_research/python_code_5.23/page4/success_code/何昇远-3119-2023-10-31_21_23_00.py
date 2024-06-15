a=eval(input())
a.reverse()
b=[]
for x in a:
    if x not in b:
        b.append(x)
        b.append(a.pop(a.index(x)))
b.reverse()
print(b)
