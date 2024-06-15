def calDegrees(nums):
    nums = {}
    for i in eval(input()):
        if i not in nums:
            nums[i] = 1
        else:
            nums[i] += 1
    return max(nums.values())



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

