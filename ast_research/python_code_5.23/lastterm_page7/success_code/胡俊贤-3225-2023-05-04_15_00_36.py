def work(a) :
    d={}
    d[0]=1
    b=1
    for i in range(1,a+1):
        b*=i
        d[i]=b
    return d

	

a = int(input())
ans = work(a)
print(ans)

