def work(a) :
    dic={}
    for i in range(a+1):
        ls=[s for s in range(i+1)]
        if i==0:
            dic[0]=1
        else:
            b=1
            for x in ls[1:]:   
                    b*=x
            dic[x]=b

    return dic
	

a = int(input())
ans = work(a)
print(ans)

