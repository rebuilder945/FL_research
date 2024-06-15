def work(a) :
def work(a):
    a1={}
    for x in range(a+1):
        a1[x]=dick(x)
    return a1
def dick(t):
    if t==0:
        return 1
    else:
        a1=[x for x in range(1,t+1)]
        v=1
        for t in a1:
            v=v*t
        return v
	

a = int(input())
ans = work(a)
print(ans)

