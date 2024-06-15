a=eval(input())
b=range(1,max(a)+1)
c=0
e=[]
for x in a:
    for y in b:
        if x%y==0:
            c+=1
        else:
            pass
    if  c==2:
        e.append(x)
        c=0
    else:
        c=0
print(e)

