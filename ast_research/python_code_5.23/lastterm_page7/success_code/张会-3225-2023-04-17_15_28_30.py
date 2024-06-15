def work(a) :
    m = {0:1}
    b=1
    for i in range(1,a+1):
        for j in range(i-1):
                b=b*(j+1)
        m[i]=b
    return m
	

a = int(input())
ans = work(a)
print(ans)

