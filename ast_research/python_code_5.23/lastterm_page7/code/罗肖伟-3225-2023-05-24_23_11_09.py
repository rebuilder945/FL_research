def work(a) :
dic={}
    ls=[i for i in range(a+1)]
    for x in ls:
        if x==0:
            dic[0]=1
        else:
            dic[x]=y(x)
    return dic
def y(x):
    if x==1:
        return 1
    else:
        return y(x-1)*x  
	

a = int(input())
ans = work(a)
print(ans)

