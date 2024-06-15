def work(a) :
    def jc(t):    
       if t==1:
            return 1
        r=n*jc(t-1)
        return r
    dic={}
    dic[0]=1 
    for n in range(1,a+1):
        dic[n]=jc(n)
    
	

a = int(input())
ans = work(a)
print(ans)

