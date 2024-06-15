def work(a) :
    dic={0:1}
    for x in range(1,a+1):
        m=1
        for i in range(1,x+1):
            m*=i
        dic[x]=m
    return dic
	

a = int(input())
ans = work(a)
print(ans)

