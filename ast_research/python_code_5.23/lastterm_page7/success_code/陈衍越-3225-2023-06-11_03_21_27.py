def work(a) :
    dic={}
    for i in range(a+1):
        dic[i]=jc(i)
    return dic
    
    
def jc(n):
    if n==1 or n==0:
        return 1
    r=n*jc(n-1)
    return r
	

a = int(input())
ans = work(a)
print(ans)

