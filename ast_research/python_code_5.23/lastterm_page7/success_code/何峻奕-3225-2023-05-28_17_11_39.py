def work(a) :
    def jc(t):    
        x=1    
        for i in range(0,t+1,-1):
            x=x*i
        return x
    dic={}
    for n in range(0,a+1):
        if n==0:
            jc(0)==1
        dic["n"]=jc(n)
    
	

a = int(input())
ans = work(a)
print(ans)

