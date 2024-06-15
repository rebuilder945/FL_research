def calDegrees(nums):
      n=nums.count(max(nums,key=nums.count))
      return n


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

