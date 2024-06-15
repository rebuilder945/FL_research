def work(a) :

    result = {}
    for i in range(a+1):
        result[i] = factorial(i)
    return result
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
	

a = int(input())
ans = work(a)
print(ans)

