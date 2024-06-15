a=input()
b=list(a.lower())
c={}
for i in b:
    c[i]=b.count(i)
print(c)
