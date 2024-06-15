def work(a) :
    import math
    dic={}
    for i in range(0,a+1):
        dic[i]=math.factorial(i)
    return dic
	

a = int(input())
ans = work(a)
print(ans)

