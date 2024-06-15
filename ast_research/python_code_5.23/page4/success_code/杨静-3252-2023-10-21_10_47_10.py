def Fibonacci(num,n):
    for i in range(n-2):
        nums.append(nums[n-3]+nums[n-2])
    return nums[n-1]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


