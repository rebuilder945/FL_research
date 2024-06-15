def calDegrees(nums):
    for x in nums:
        a = max(nums.count(x))
    return(a)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

