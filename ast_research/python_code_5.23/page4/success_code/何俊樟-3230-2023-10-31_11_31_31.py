a=eval(input())
a.sort()
b=a.copy()
for x in b:
    if a.count(x)>1:
        for y in range(a.count(x)-1):
            a.remove(x)
    else:
        pass
c=str(a[0])
for x in range(len(a)-1):
    d=a[x+1]
    e=c+str(d)
print(e)
    
    
    
