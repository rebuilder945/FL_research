def calDegrees(nums):
      n=nums.count(x) for x in set(nums)
      return max(n)



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

