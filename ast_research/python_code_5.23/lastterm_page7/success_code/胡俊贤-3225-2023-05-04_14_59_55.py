def work(a) :
    d={}
    b=1
    for i in range(1,a+1):
        b*=i
        d[i]=b
    d[0]=1
    return d

	

a = int(input())
ans = work(a)
print(ans)

