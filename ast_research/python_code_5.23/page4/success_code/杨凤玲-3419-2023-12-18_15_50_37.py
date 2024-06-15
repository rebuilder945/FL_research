def calDegrees(nums):
    for i in nums:
        b=nums.count(i)
        c=0
        if b>c:
            c=b
    return c

 


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

