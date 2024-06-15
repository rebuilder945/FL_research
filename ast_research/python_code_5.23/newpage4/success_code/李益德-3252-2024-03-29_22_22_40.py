def Fibonacci(num,n):
    nums= list(num)
    for i in range(n-2):
        a =nums[i]+nums[i+1]
        nums.append(a)
    b=nums[n-1]
    return b




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


