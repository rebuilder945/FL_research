def work(a) :
    dic={0:1}
    for i in range(1,a+1):
        i=b
        for x in range(1,i):
            i*=x
        dic[b]=i
    return dic
    
	

a = int(input())
ans = work(a)
print(ans)

