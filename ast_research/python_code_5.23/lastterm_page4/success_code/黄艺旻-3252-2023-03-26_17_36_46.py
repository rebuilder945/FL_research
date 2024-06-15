def Fibonacci(nums,n):
    a = nums
    for i in range(2,n):
        a.append(a[-1]+a[-2])
        return a[-1]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


