def calDegrees(nums):
    m =1
    for x in nums:
        c = nums.count(x)
        if c > m:
             m=c
    return c


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

