def calDegrees(nums):
    nums  =  eval(input())
    import random
    n=random.sample(nums,1)
    count=nums.count(n)
    return(count)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

