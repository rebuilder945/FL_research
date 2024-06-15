def work(a) :
    res = {}
    factorial = 1
    for i in range(a+1):
        if i == 0:
            res[i] = 1
        else:
            factorial *= i
            res[i] = factorial
    return res

	

a = int(input())
ans = work(a)
print(ans)

