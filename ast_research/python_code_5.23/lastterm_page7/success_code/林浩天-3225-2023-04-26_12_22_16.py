def work(a) :


    import math
    dic = {}
    for i in range(a+1):
        dic[i] = math.factorial(i)

	

a = int(input())
ans = work(a)
print(ans)

