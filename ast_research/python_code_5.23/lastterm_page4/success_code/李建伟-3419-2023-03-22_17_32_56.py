def calDegrees(nums):
    lst1 = []
    for x in range(len(nums)):
        lst1.append(nums.count(nums[x]))
    n = max(lst1)
    return n


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

