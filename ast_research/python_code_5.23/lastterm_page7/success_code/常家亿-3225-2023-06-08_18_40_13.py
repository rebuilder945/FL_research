def work(a) :
    dic ={}
    for x in range(0,a+1):
        t = 1
        for i in range(1,x+1):
            t *= i
        dic[x]=t
    return dic
	

a = int(input())
ans = work(a)
print(ans)

