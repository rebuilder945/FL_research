def work(a) :
    m = {0:1}
    b=1
    for i in range(1,a):
        for j in range(i):
                b=b*(j+1)
        m[i]=b
    return m
	

a = int(input())
ans = work(a)
print(ans)

