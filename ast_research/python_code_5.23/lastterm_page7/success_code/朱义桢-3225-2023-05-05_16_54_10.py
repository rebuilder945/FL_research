def work(a) :
    b={}
    b[0]=1
    for i in range(1,a+1):
        c=1
        for x in range(1,i+1):
            c*=x
        b[i]=c
    return(b)
	

a = int(input())
ans = work(a)
print(ans)

