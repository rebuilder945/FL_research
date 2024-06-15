def work(a) :
    b={}
    for i in range(a+1):
      b[i]=f(i)
    return b
def f(x):
    if x==0:
        return 1
    else:
        k=1
        for m in range(1,x+1):
            k*=m
        return k  
	

a = int(input())
ans = work(a)
print(ans)

