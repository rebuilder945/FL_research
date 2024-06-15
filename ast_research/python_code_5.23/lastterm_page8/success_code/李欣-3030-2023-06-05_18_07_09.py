name=list((input()).split(','))
score=list((input()).split(','))
score=[int(x) for x in score]
a=[]
for x in name:
    h=[]
    for y in score:
        if name.index(x)==score.index(y):
            h.append(x)
            h.append(y)
    a.append(h)
for i in a:
    i[0],i[1]=i[1],i[0]
b=sorted(a)
for i in b:
    i[0],i[1]=i[1],i[0]
print(b)
