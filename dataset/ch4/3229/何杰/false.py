n=eval(input())
i=0
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
    an1=str(mn)
    an=an1[1:-1]
    print(an)
elif m==[]:
    print('False')
