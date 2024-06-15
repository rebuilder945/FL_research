def calDegrees(nums):
    a = []
    for i in nums:
        x = nums.count(i)
        a.append(x)
    return max(a)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

