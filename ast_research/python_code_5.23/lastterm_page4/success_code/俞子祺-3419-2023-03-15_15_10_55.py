def calDegrees(nums):
      len=max(nums,key=nums.count)
      return len



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

