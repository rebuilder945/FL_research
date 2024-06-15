def maxsum(nums):
 sum=0
 nums.sort
 
 
 for i in range(len(sums)):
  if i%2==0:
   sum+=i   
 return sum;     




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

