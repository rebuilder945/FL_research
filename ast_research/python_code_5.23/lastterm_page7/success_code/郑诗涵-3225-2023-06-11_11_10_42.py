def work(a) :
    b={0:1}
    if a==0:
        return b
    else:
        for x in range(1,a+1):
            b[x]=b[x-1]*x
        return b
	

a = int(input())
ans = work(a)
print(ans)

