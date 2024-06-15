a=eval(input())
b=a.copy()
c=[]
for i in a:
    if i==0:
        b.remove(i)
        c.append(i)
d=b+c
print(d)
