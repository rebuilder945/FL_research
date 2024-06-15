def work(a) :
    dic={}
    if a==0:
        dic[0]=1
    else:
        t=1
        dic[0]=1
        for i in range(1,a+1):
            t=t*i
            dic[i]=t
    return dic
	

a = int(input())
ans = work(a)
print(ans)

