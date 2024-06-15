def work(a) :

    factorials = {0: 1}
    factorial = 1
    for i in range(1, x+1):
        factorial *= i
        factorials[i] = factorial
    return factorials

	

a = int(input())
ans = work(a)
print(ans)

