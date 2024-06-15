def work(a) :
ans = {0: 1}
    factorial = 1
    for num in range(1, a+1):
        factorial *= num
        ans[num] = factorial
    return ans
	

a = int(input())
ans = work(a)
print(ans)

