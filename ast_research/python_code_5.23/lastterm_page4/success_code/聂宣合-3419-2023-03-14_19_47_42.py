def calDegrees(nums):
    nums=max(nums,key=nums.count)
    return(nums)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

