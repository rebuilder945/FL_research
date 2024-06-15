a=input().split()
b=eval(input())
c=[]
for n in a:
    d=[]
    d.append(n)
    d.append(b[a.index(n)])
    c.append(d)
print(c)



