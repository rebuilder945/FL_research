def work(a) :
    c={}
    d=1
    c[0]=1
    for b in range(1,a+1):
        for i in range(1,b):
            d*=i
        c[b]=d
    

    return c
	

a = int(input())
ans = work(a)
print(ans)

