def maxsum(nums): 
 nums.sort() # 将列表按照升序排序
  n = len(nums) // 2 # 计算n的值 
  min_sum = 0 
   for i in range(n):
      min_sum += nums[i*2] # 每一对的最小值是偶数索引位置的数 
   return min_sum





nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

