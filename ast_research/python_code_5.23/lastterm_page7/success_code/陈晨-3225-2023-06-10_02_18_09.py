def work(a) :
    dic={0:1}
    for x in range(1,a+1):
        x1=1
        for k in range(1,x+1):
            x1*=k
        dic[x]=x1
    return dic

	

a = int(input())
ans = work(a)
print(ans)

