def calDegrees(nums):
     lstA=[nums.count(x) for x in nums]
     return(max(lstA))


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

