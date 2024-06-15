def Fibonacci(nums:list,n):
    a = nums
    for i in range(3,n+1):
        a.append(a[i-1]+a[i-2])
        return a[-1]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


