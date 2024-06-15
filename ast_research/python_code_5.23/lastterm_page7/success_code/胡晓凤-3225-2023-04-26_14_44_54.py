def work(a) :
    d={}
    for i in range(0,a+1):
        s1=i
        if i==0:
            d[s1]=1
        elif i!=0:
            for x in range(1,i+1):
                s=1
                s*=x
                x=x+1
            d[s1]=s
    return d
	

a = int(input())
ans = work(a)
print(ans)

