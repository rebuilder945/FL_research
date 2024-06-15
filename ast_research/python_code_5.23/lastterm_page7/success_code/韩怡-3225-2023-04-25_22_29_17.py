def work(a) :
    x={}
    for i in range(a+1):
        x[i]=f(i)
    return x
def f(x):
    s=1
    for i in range(1,x+1):
        s=s*i
    return s
	

a = int(input())
ans = work(a)
print(ans)

