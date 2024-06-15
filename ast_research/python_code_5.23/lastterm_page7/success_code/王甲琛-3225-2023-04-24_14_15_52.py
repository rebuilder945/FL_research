def work(a) :
    dic={}
    for i in range(a):
        b=1
        for x in range(i):
            b*=x+1
        dic[i]=b
    return(dic)
	

a = int(input())
ans = work(a)
print(ans)

