def work(a) :
    dict={0:0}
    for i in range(a+1):
        dict[i]=fac(i)
    return dict
def fac(n):
    if n<=1:
        return 1
    else:
        return n*fac(n-1)
	

a = int(input())
ans = work(a)
print(ans)

