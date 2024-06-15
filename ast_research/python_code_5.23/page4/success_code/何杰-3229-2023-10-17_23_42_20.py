n=eval(input())
mn=[]
m=[]
for x in n:
    if n.count(x)==1:
        m.append(x)
if m!=[]:
    for x in n:
        if n.count(x)==1:
            mn.append(x)
            mn.sort()
    for x in mn:   
        if x==mn[-1]:
            a=""
        else:
            a=","
        print(x,end=a)
elif m==[]:
    print('False')
