def work(a) :
    dic={}
    for x in range(a+1):
        i=1
        for m in range(1,x+1):
            i=i*m
        dic[x]=i
    return(dic)

	

a = int(input())
ans = work(a)
print(ans)

