def work(a) :
    b=[]
    c=[]
    e=2
    for x in range(a):
        b.append(x)
        if x!=0:
            e=e*b[x]
            c.append(e)
        else:
            c.append(1)
    d=dict(zip(b,c))
    return d
	

a = int(input())
ans = work(a)
print(ans)

