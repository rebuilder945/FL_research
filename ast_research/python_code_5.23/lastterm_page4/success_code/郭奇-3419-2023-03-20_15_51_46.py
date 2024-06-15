def calDegrees(nums):
    result = max(nums,key=lambda x:nums.count(x))
    return result



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

