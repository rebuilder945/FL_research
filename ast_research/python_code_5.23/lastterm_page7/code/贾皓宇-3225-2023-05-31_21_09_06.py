def work(a) :
s=1
    p={}
    for x in range(1,a+1):
        s=s*x
        p[x]=s
    return p
	

a = int(input())
ans = work(a)
print(ans)

