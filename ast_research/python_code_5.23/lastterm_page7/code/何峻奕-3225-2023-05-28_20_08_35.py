def work(a) :
    dic={}
    def jc(t):    
       if t==1:
            return 1
        r=t*jc(t-1)
        return r
    for i in range(0,a+1):
        if i==0:
            dic[0]=1
        else:
            dic[i]=jc(i)
    return dic
    
	

a = int(input())
ans = work(a)
print(ans)

