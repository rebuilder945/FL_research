def work(a) :

    dic1={}
    for i in range(a+1):
        if i==0:
            dic1[i]=1
        else:
            x=1
            for n in range(1,i+1):
                x=x*n
            dic1[i]=x
    return dic1
	

a = int(input())
ans = work(a)
print(ans)

