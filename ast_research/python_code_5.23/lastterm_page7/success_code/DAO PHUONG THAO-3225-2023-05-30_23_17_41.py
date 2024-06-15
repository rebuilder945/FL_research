def work(a) :
    d = {0: 1}
    factorial = 1
    for i in range(1, a+1):
        factorial *= i
        d[i] = factorial 
    return d

	

a = int(input())
ans = work(a)
print(ans)

