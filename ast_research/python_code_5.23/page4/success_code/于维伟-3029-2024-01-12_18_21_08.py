a=input().split(',')
b=map(int,input().split(','))
c=[]
for x in a:
    for y in b:
        d=[]
        d=d.append(x,y)
    c=c.append(d)
print(c)
