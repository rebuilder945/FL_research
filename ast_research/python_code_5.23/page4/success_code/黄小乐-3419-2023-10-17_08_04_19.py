def calDegrees(nums):
    import random
    r=random.randint(nums)
    count=nums.count(r)
    return(count)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

