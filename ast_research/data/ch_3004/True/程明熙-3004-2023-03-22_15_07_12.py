a=eval(input())
c=[]
d=[]
for i in a:
    if i==1 or i==0:
        c.append(i)
    else:    
        for b in range(2,i):
            if i%b==0:
                
                c.append(i)

c.sort()
c=list(set(c))
for i in c:
    if i in a:
        a.remove(i)
print(a)
