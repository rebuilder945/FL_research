n,m=input().split()
n,m=eval(n),eval(m)
a=[]
b=[]
for i in range(n,m):
    a.append(i)
if len(a)<3:
    print("illegal input")
elif len(a)>=3:
    for q in a:
        for w in a:
            for e in a:
                if q!=w and w!=e and e!=q:
                   t=100*q+10*w+e
                   b.append(t)
    x=b
    print(*x,sep=" ")                


