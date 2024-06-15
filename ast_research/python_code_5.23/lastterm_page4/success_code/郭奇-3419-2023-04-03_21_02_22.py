def calDegrees(nums):
      result = nums.count(max(nums,key=nums.count))
      return result



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

