def calDegrees(nums):
      counts={}
      for num in nums:
           counts[num]=counts.get(num,o)+1
           calDegrees=max(counts.values())
           return calDegrees


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

