def work(a) :
    import math
    d={}
    for i in range(a+1):
        d[i]=math.factorial(i)
    return d
	

a = int(input())
ans = work(a)
print(ans)

