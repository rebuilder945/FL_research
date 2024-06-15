def calDegrees(nums):
    import random
        x=random.choice(nums)
    count=nums.count(x)
    return(count)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

