def work(a) :
    def jc(t):    
       if t==1:
            return 1
        r=t*jc(t-1)
        return r
    dic={}
    for n in range(0,a+1):
        if n==0:
            dic[0]=1
        else:
        dic[n]=jc(n)
    
	

a = int(input())
ans = work(a)
print(ans)

