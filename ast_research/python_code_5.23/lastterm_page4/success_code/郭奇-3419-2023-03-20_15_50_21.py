def calDegrees(nums):
    """函数的功能：求列表中出现次数的最大值"""
    result = max(nums,key=lambda x:nums.count(x))
    return result



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

