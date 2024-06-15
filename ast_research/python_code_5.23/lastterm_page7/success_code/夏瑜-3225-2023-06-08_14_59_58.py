def work(a) :
    dic={}
    for i in range(0,a+1):
        dic[i]=jiecheng(i)
    return dic
def jiecheng(n):
    if n==0:
        return(1)
    else:
        r=n*jiecheng(n-1)
        return r
                
	

a = int(input())
ans = work(a)
print(ans)

