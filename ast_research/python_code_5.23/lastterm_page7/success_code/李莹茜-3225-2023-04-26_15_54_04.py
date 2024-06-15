def work(a) :
    dic={}
    import math
    for i in range(a+1):
        b=math.factorial(i)
        dic[i]=b
    return dic
	

a = int(input())
ans = work(a)
print(ans)

