def work(a) :
    poi={}
    for x in range(a+1):
        if x==0:
            poi[x]=1
        q=1
        for t in range(1,x):
            q*=t
        poi[x]=q

	

a = int(input())
ans = work(a)
print(ans)

