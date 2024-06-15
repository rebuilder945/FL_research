a=list(eval(input()))
b=max(a)
c=min(a)
m=[]
for x in a[0:]:
    if x==b or x==c:
        a.remove(x)
    else:
        m.append(x)
print(m)
