def Fibonacci(nums:list, n):
     nums.append(nums[n-1-1]+nums[n-1-2])
     return nums[-1]





num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


