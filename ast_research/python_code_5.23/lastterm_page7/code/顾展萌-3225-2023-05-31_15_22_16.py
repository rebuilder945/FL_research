def work(a) :
fac = 1
    res = {0: 1}
    for i in range(1, a+1):
        fac *= i
        res[i] = fac
    return res

	

a = int(input())
ans = work(a)
print(ans)

