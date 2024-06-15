def calDegrees(nums):
for x in nums:
nums.sort(key=nums.count([0]))
nums.reverse()
e = nums.count([0])
return e
      



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

