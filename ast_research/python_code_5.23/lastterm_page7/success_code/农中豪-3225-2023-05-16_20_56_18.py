def work(a) :
    b={}
    b[0]=1
    c=1
    for i in range(1,a+1):
        c*=i
        b[i]=c
    return(b)
	

a = int(input())
ans = work(a)
print(ans)

