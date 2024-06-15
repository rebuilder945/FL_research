def calDegrees(nums):
    a=0
    for i in nums:
        if  nums.count(i)>a:
            a=num.count(i)
    return a
       



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

