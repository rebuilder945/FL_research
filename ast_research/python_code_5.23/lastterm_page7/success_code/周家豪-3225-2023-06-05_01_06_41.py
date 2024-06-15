def work(a) :
    dic={0:1}
    for i in range(a+1):
        a0=1
        for x in range(1,i+1):
            a0*=x
            dic[x]=a0
    return dic
	

a = int(input())
ans = work(a)
print(ans)

