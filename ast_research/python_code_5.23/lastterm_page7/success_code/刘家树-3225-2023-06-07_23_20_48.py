def work(a) :
    d={0:1}
    for i in range(1,a+1):
        s=1
        for x in range(1,i+1):
            s=s*x
        d[i]=s
    return d

	

a = int(input())
ans = work(a)
print(ans)

