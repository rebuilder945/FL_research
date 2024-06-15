def maxsum(nums):
      nums.sorted()
      sum=0
      for i in range(0,len(nums),2):
            sum+=nums[i]
print(sum)
            
            




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

