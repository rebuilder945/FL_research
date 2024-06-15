def maxsum(nums):
    nums.sort()
    min = 0
    for i in range(0,len(nums),2):
        min += int(nums[i])
    return min




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

