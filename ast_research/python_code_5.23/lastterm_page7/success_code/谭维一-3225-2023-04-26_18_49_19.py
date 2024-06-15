def work(a) :
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)

    factorial_dict = {}
    for i in range(a+1):
        factorial_dict[i] = factorial(i)
    return factorial_dict

	

a = int(input())
ans = work(a)
print(ans)

