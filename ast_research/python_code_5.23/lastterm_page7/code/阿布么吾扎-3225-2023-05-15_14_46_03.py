def work(a) :
     ans={}
    if a==0:
        ans[a]=1
    else:
        for i in range(0,a+1):
            b=1
            b=b*i
        ans[a]=b
    return ans
    
	

a = int(input())
ans = work(a)
print(ans)

