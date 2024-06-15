a=eval(input())
b=a.copy()
c=[]
for x in a:
    if x==0:
        b.remove(x) 
        c.append(x)
d=b+c        
print(d)
