a=eval(input())
b=[]
c=max(a)
d=min(a)
for i in a:
    if i==c or i==d:
        a.remove(i)
    else:
        b.append(i)
print(b)
