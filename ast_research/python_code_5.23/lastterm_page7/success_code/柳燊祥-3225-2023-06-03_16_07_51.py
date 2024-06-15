def work(a) :
    res={}
    fac=1
    for i in range(0,a+1):
        if i==0:
            res[i]=1
        else:
            fac*=i
            res[i]=fac
        return res
	

a = int(input())
ans = work(a)
print(ans)

