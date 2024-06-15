def calDegrees(nums):
    d=max(nums,key=nums.count)
    return d 


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

