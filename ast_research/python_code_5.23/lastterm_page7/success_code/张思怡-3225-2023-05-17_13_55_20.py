def work(a) :
    dict={}
    for x in range(a+1):
        dict[x]=dict.get(x,0)+jiechen(x)
    return dict
def jiechen(n):
    t=1
    for i in range(1,n+1):
        t=t*i     
    return t
	

a = int(input())
ans = work(a)
print(ans)

