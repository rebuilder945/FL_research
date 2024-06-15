def calDegrees(nums):
    import random
    count=nums.count(random(nums))
    return(count)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

