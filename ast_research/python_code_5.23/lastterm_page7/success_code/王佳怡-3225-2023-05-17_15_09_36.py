def work(a) :
    import math
    return {i: math.factorial(i) for i in range(a + 1)}

	

a = int(input())
ans = work(a)
print(ans)

