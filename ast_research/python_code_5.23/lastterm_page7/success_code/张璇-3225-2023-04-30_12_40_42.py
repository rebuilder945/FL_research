def work(a) :
    c={}
    c[0]=1
    for x in range(1,a):
        c[x]=x*c[x-1]
    return c
	

a = int(input())
ans = work(a)
print(ans)

