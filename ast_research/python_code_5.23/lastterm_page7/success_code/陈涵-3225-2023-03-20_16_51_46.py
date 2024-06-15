def work(a) :
    import math
    num=[(i,math.factorial(i)) for i in range(0,a+1)]
    dic=dict(num)
    return dic
	

a = int(input())
ans = work(a)
print(ans)

