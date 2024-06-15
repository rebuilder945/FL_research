def work(a) :
    dic={0:1}
    b=1
    for x in range(1,a+1):
        b=b*x
        dic[x]=b
    return(dic)
	

a = int(input())
ans = work(a)
print(ans)

