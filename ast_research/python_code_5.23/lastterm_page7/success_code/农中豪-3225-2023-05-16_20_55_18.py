def work(a) :
    b={}
    c=1
    for i in range(1,a+1):
        c*=i
        b[i-1]=c
    return(b)
	

a = int(input())
ans = work(a)
print(ans)

