def calDegrees(nums):
    count = []
    for i in nums:
        count.append(nums.count(i))
    return max(count)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

