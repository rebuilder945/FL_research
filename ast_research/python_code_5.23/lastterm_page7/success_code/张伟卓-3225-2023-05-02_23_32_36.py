def work(a) :
    d={0:1}
    f=1
    for i in range(1,a+1):
        f*=i
        d[i]=f
    return d
	

a = int(input())
ans = work(a)
print(ans)

