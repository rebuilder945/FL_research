a=eval(input())
b=0
c=[]
for x in a:
    if a.count(x)==1:
        b+=1
    else:
        pass
if b!=0:
    for x in a:
        if a.count(x)==1:
            c.append(x)
        else:
            pass    
    c.sort()
    for x in c:
        if x==c[-1]:
            print(x)
        else:
            print(x,end=",")
else:
    print("False")
