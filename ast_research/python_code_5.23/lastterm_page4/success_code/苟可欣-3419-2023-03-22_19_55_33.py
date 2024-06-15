def calDegrees(nums):
    for x in nums:
        a=''.join(nums.count(x))
    return max(a)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

