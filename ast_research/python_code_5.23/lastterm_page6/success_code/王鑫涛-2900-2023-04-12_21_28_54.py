n=eval(input())
a=[]
c=[]
d=[]
if n>1:
    for i in range(2,n+1):
        for x in range(2,i):
            if i%x==0:
                a.append(i)
                continue
    b=range(2,n+1)
    for y in b:
        if not y in a:
            c.append(y)
    for r in c:
        if r==eval(str(r)[::-1]):
            d.append(r)
    for t in range(len(d)):
        print('%d'%d[t],end=' ')
else:
    print("illegal input")

