def calDegrees(nums):
    a=max(set(nums))
    b=a.count(nums)
    return b


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

