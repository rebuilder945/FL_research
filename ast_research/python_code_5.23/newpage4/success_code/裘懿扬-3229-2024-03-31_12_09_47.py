a=list(eval(input()))
b=[]
for i in a:
    if i not in b:
        b.append(i)
    elif i in b:
        b.remove(i)
b.sort()
c=','.join(str(x) for x in b)
print(c)
