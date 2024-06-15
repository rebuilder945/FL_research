def work(a) :
    xx={}
    for i in range(a+1):
        if i == 0:
            xx.setdefault(i,1)
        else:
            xx.setdefault(i,i*xx[i-1])
    return xx
	

a = int(input())
ans = work(a)
print(ans)

