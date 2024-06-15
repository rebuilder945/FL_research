def calDegrees(nums):
      counts={}
      for num in nums:
           counts[num]=counts.get(num,0)+1
           d=max(counts.values())
           return d


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

