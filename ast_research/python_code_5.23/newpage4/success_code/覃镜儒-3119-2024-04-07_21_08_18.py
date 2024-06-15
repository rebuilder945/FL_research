i=eval(input())
i.reverse()
b=[]
for a in i:
    if a not in b:
        b.insert(0,a)
    else:
        pass
print(b)
