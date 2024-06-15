def maxsum(nums):
    nums.sort()
    pairs = []
    for i in range(0, len(nums), 2):
        pairs.append([nums[i], nums[i+1]])
    return pairs




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

