def Fibonacci(num,  n):
 nums = []
 if n < 3:
  return ("1")
 else:
  for i in range(n):
   nums[0],nums[1] = nums[1],nums[0]+nums[1]
   return (nums[1])





num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


