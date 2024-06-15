def work(a) :
n=dict()
    for i in range(0,a+1):
        x=0
        y=1
        while i>x:
            x+=1
            y*=x
        n[i]=y
    return(n)
	

a = int(input())
ans = work(a)
print(ans)

