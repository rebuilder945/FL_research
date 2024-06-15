def work(a) :
    dic={0:1}
    if a!=0:
        for i in range(1,a+1):
            s=1
            for m in range(1,i+1):
                s=s*m
            dic[i]=s
    else:
        dic=dic
    return(dic)
	

a = int(input())
ans = work(a)
print(ans)

