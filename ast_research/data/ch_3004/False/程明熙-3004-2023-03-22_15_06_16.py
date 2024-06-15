a=eval(input())
c=[]
d=[]
for i in a:
    if i==1:
        c.append(1)
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
