def calDegrees(nums):
    D=0
    for i in nums:
        a=nums.count(i)
        if a > D:
            D=a
    return D


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

