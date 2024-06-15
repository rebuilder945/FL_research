a=eval(input())
d=[]
for x in a:
    if x==2 or x==3:
        d.append(x)
    else:
        for n in range(3,x-1):
            results=x%n
            if results==0:
                break  
            else:
                d.append(x)     
b=[]
for i in d:
    if i not in b:
        b.append(i)
print(b)
