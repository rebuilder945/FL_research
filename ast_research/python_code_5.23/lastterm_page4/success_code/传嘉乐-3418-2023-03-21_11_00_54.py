def maxsum(nums):
   nums.sort()
   a=0
   for i in range(0,len(nums),2):
      a+=i
   return a




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

