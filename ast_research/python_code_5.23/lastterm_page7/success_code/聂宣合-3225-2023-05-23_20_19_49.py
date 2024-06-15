def work(a) :
    ans={}
    for i in range(a+1):
        x=1
        for b in range(1,i+1):
            x=x*b
            
        ans[i]=x
        
    return ans
        
	

a = int(input())
ans = work(a)
print(ans)

