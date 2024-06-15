def calDegrees(nums):
    degrees = []
    for i in nums:
        degrees.append(nums.count(i))
    degrees.sort()
    return degrees[-1]
#return语句出现在了函数外部
nums = eval(input())
d = calDegrees(nums)  # 调用自定义函数
print(d)