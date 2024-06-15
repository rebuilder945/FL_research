def work(a) :
    def jc(t):    
        x=1    
        for i in range(1,t+1,-1):
            if t==0:
                x==1
            else:
                x=x*i
        return x
    dic={}
    for n in range(0,a+1):
        dic["n"]=jc(n)
    
	

a = int(input())
ans = work(a)
print(ans)

