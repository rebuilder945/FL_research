def calDegrees(nums):
   count = {} for num in nums:
   if num in count: count[num] += 1 
   else: count[num] = 1 max_freq = max(count.values()) return max_freq


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

