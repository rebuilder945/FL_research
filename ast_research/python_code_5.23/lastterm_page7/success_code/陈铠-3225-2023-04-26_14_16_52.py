def work(a) :
    d=[]
    d[0]=1
    for i in range(1,a+1):
        x=1
        for c in range(1,i+1):
            x*=c
        d[i]=x
    return d
	

a = int(input())
ans = work(a)
print(ans)

