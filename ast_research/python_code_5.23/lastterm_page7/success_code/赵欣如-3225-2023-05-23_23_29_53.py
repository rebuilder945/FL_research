def work(a) :
    dic={}
    dic[0]=1
    for x in range(1,a+1):
        b=1
        for a in range(1,x+1):
            b*=a
        dic[x]=b
    return(dic)

	

a = int(input())
ans = work(a)
print(ans)

