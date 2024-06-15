def work(a) :
    ans = {0: 1}
    factorial = 1
    for i in range(1, a+1):
        factorial *= i
        ans[i] = factorial
    return ans
	

a = int(input())
ans = work(a)
print(ans)

