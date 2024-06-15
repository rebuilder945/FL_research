def Fibonacci(nums:list, n):
    for x in range(3:n+1):
     nums.append(nums[x-2]+nums[x-3])
     return nums[-1]





num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


