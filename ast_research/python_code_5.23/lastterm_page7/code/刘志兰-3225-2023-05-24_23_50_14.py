def work(a) :
    res={}
    fact=1
    for i in range(a+1):
        if i==0:
            res[i]=1
        else:
            fact*=i
        res[i]=fact
return res
        
	

a = int(input())
ans = work(a)
print(ans)

