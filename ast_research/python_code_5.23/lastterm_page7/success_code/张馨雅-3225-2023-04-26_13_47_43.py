def work(a) :
    dic={}
    for i in range(0,a+1):
        if i==0:
            m=1
        else:
            m=jie(i)
        dic[i]=m
    return dic
def jie(n):
    a=1
    for i in range(1,n+1):
        a*=i
    return a
	

a = int(input())
ans = work(a)
print(ans)

