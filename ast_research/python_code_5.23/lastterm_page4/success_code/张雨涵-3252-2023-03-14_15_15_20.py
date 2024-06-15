def Fibonacci(num,  n):
    for i in range(2,n):
        nums = num.copy()
        x = int(nums[i-1])+int(nums[i-2])
        num.append(x)
    return(num[n-1])




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


