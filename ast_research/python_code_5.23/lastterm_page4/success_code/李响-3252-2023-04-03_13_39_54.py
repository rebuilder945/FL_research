def Fibonacci(nums:list,n):
   for x in range(3,n+1):
      nums.append(nums[x-1-1],nums[x-1-2])
   return nums[-1]
   
   




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


