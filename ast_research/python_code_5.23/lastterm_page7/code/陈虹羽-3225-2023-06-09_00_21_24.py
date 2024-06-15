def work(a) :
       c={}
    for i in range(a+1):
        if i==0 or i==1:
            c[i]=1
        else:
            d=1
            for x in range(1,i+1):
                d*=x
            c[i]=d
    return c
	

a = int(input())
ans = work(a)
print(ans)

