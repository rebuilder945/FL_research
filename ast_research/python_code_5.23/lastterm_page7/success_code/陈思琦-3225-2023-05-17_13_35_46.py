def work(a) :
    dic={}
    dic[0]=1
    x=1
    for i in range(1,a+1):
        x=x*i
        dic[i]=x
    return dic
	

a = int(input())
ans = work(a)
print(ans)

