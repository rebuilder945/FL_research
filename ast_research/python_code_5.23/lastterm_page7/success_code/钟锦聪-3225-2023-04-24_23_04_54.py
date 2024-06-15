def work(a) :
    dora = {}
    n=1
    dora[0]=1
    for i in range(1,a+1):
        n = n*i
        dora[i]=n
    return dora
	

a = int(input())
ans = work(a)
print(ans)

