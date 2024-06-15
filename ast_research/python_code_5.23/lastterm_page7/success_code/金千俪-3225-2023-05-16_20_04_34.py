def work(a) :
    fac=1
    dic={}
    for i in range(1,a+1):
        fac*=i
        dic[i]=fac
    return dic
        
	

a = int(input())
ans = work(a)
print(ans)

