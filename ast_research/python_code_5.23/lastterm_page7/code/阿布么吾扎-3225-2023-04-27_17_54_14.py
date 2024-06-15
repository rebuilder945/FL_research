def work(a) :
     dic={}
    if a==0:
        dic[a]=1
    else:
        for i in range(0,a+1):
            b=1
            b=b*i
        dic[a]=b
    return dic
    
	

a = int(input())
ans = work(a)
print(ans)

