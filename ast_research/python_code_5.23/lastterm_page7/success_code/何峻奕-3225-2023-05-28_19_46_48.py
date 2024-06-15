def work(a) :
    def jc(t):    
        if t==1:
            return 1
        r=n*jc(t-1)
        return r
    dic={}
    for n in range(0,a+1):
        dic["n"]=jc(n)
    
	

a = int(input())
ans = work(a)
print(ans)

