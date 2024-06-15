def work(a) :
    b=[]
    c=[1]
    for x in range(a+1):
        b.append(x)
        c.append(c[x]*(x+1))
        
    d=dict(zip(b,c))
    return d
	

a = int(input())
ans = work(a)
print(ans)

