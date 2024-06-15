c=eval(input())
k=[]
for x in c:
    if c.count(x)==1:
        k.append(x)
        print(k.sort())
    else:
        print(False)
    
