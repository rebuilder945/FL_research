def work(a) :
    dic={}
    for i in range(a+1):
        if i == 0:
            dic[i]=1
        else:
            n=1
            for x in range(1,i+1):
                n*=x
            dic[i]=n
    return dic
	

a = int(input())
ans = work(a)
print(ans)

