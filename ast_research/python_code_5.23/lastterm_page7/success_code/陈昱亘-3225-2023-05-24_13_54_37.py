def work(a) :
    dic={}
    for i in range(a+1):
        if i==0:
            dic[i]=1
        else:
            dic[i]=1
            for k in range(i):
                dic[i]*=(k+1)
    return dic
	

a = int(input())
ans = work(a)
print(ans)

